/*
  Eric Villasenor
  evillase@gmail.com

  datapath contains register file, control, hazard,
  muxes, and glue logic for processor
*/

// data path interface
`include "datapath_cache_if.vh"
`include "register_file_if.vh"
`include "control_unit_if.vh"
`include "alu_if.vh"
`include "cache_control_if.vh"
`include "forwarding_unit_if.vh"
`include "store_forwarding_if.vh"

// alu op, mips op, and instruction type
`include "cpu_types_pkg.vh"

module datapath (
  input logic CLK, nRST,
  datapath_cache_if.dp dpif
);
   // import types
   import cpu_types_pkg::*;

   // pc init
   parameter PC_INIT = 0;

   //Interfaces
   alu_if aluif();
   register_file_if rfif();
   control_unit_if cuif();
   forwarding_unit_if fuif();
   store_forwarding_if sfif();
   
   
   //interface signals
   word_t pc_next, pc;
   logic      d_ihit, d_dhit;

   logic bubble_lw_f; //This signal name stands for bubble-during-load-opn-wrt-forwarding

   //branch-jump signal declaraions
   logic branch_taken, bne_taken, beq_taken;
   word_t pc_branch_mux; //this will store the output of the mux deciding between pc_plus_4_M or whatever is due to the branch
   word_t pc_when_branch; //the pc next value when there is a banch
   word_t jr_output; //the pc next value when there is a jr
   logic jal_or_j;
   logic [27:0] intermediate_jump_op;
   word_t jump_address;
   word_t pc_next_branch_jump;
   logic 	jump_taken;

   logic branch_or_jump;
   //end of branch-jump signal declaraions
   
   alu ALU (aluif);
   register_file REGISTER_FILE (CLK, nRST, rfif);
   control_unit CONTROL_UNIT (cuif);
   program_counter PROGRAM_COUNTER (.CLK(CLK), .nRST(nRST), .pc_EN( (d_ihit & ~d_dhit & ~cuif.halt) || branch_or_jump), .pc_in(pc_next), .pc_out(pc)); //the pc_EN may also be dependent on ~d_hit based on historical experience

   //forwarding unit code
   forwarding_unit FORWARDING_UNIT (fuif);

   //store forwarding code
   store_forwarding STORE_FORWARDING (sfif);

   logic predicted, predicted_D, predicted_EX, predicted_M;
   
   
      
   //Signals in datapath
   //Fetch
   word_t pc_plus_4;//pc + 4
   word_t instruction;//the instruction loaded from the memory
   logic      en_D; //enable for IF/ID latch
   
   //Decode
   logic      j, jal, jr, beq, bne, cu_halt, RegWrite, dR_REQ, dW_REQ, RegDst, ExtOp, ShiftOp, ALUSrc, MemToReg, lui; //control unit signals
   aluop_t ALUOp; //control unit
   word_t instruction_D; //the instruction latched to the IF/ID latch, goes into the control unit
   opcode_t op_D;
   word_t pc_plus_4_D;
      
   //Execute
   logic j_EX, jal_EX, jr_EX, beq_EX, bne_EX, cu_halt_EX, RegWrite_EX, dREN_EX, dWEN_EX, RegDst_EX, ExtOp_EX, ShiftOp_EX, MemToReg_EX, lui_EX, ALUSrc_EX; //control
   aluop_t ALUOp_EX; //control
   word_t rdata1_EX, rdata2_EX; //register file
   logic [15:0] imm_EX; //imm
   regbits_t rt_EX, rs_EX, rd_EX; //instruction[20:11]
   logic 	en_EX; //enable for ID/EX latch
   word_t instruction_EX;
   

   word_t shamt_extended; //output of shamt extender
   word_t sign_ext; //output of sign extender
   word_t ALUSrc_output; //ALUSrc mux output
   word_t shiftOp_output; //ShiftOp mux output
   regbits_t RegDst_output; //RegDst mux output
   regbits_t wsel_EX; //JAL mux output

   word_t sw_forwarding_output;

   opcode_t op_EX;
   
   word_t pc_plus_4_EX;
   
   //Memory
   logic dWEN_M, dREN_M, halt_M, regWrite_M, memToReg_M, lui_M, beq_M, bne_M, j_M, jr_M, jal_M; //control signals passed through
   logic zero_M;
   word_t porto_M, rdata2_M;
   word_t sign_ext_M;
   word_t rdata1_M; //exclusively for the jr case
   word_t instruction_M; //to calculate the jump address in the MEM stage
   

   regbits_t wsel_M; //portO of ALU, rdat2 of register file, jal mux output passed through
   logic [15:0] imm_M; //imm passed through
   logic en_M; //enable for EX/MEM latch

   opcode_t op_M;
   
   word_t pc_plus_4_M;
      
   //Write Back
   logic memToReg_WB, lui_WB, regWrite_WB, jal_WB; //control signals passed through , wsel = jal mux output passed through
   regbits_t wsel_WB;
   word_t porto_WB, dmemload_WB; //portO of ALU, dmemload from cache
   logic [15:0] imm_WB; //imm
   word_t memToReg_out; //memToReg mux output
   word_t jalWB_out; //jal mux output
   word_t wdat_WB; //output of lui mux
   logic en_WB; //enable for MEM/WB latch
   logic halt_WB; //halt signal passed through

   opcode_t op_WB;
   word_t pc_plus_4_WB;
   
   //--------FETCH------------------------------------------------------------------------
   //Signals denoted '_D'

   //btb code
   btbset_t btbframes; //the branch target bufer
   logic btbhit;
   word_t jump_add;
   btb BTB (.CLK(CLK), .nRST(nRST), .pc(pc), .btbframes(btbframes), .btbhit(btbhit), .jump_add(jump_add), .predicted(predicted)); //based on he btbhit value returned, we will decide the pc_next value
   //end of btb code
   
   
   assign pc_plus_4 = pc + 4;
   
   assign pc_next = (predicted == 1'b1 && branch_or_jump == 1'b0) ? jump_add : ( (branch_or_jump == 1'b1) ? pc_next_branch_jump : pc_plus_4); //subject to change in later pipeline additions -> maybe need some modifications later
  
   assign dpif.imemREN = 1; //iREN always 1
   assign dpif.imemaddr = pc;   
   assign d_dhit = dpif.dhit; //dhit
   assign d_ihit = dpif.ihit; //ihit
   assign instruction = dpif.imemREN ? dpif.imemload : 0; //the instruction that is initially fetched from the IRAM - this will be latched to the IF/ID latch
   assign en_D = d_ihit; 
   
   always_ff @(negedge nRST, posedge CLK)
     begin
	if (~nRST)
	  begin
	     instruction_D <= 0; //make it zero upon reset
	     op_D <= HALT;
	     pc_plus_4_D <= 0;	   
	     predicted_D <= 0;
	     
	  end
	else
	  begin
	     if (branch_or_jump) //this is for the bubble in D, EX, M stages following a branch or a jump
	       begin
		  instruction_D <= 32'b0;
		  op_D <= RTYPE;
		  pc_plus_4_D <= pc_plus_4;
		  predicted_D <= 0; //might have to come back to his later
	       end	     
	     else if (en_D)
	       begin
		  instruction_D <= instruction;
		  op_D <= opcode_t'(instruction[31:26]);
		  pc_plus_4_D <= pc_plus_4;
		  predicted_D <= predicted;
		  
	       end
	     else if (bubble_lw_f && d_dhit && ~d_ihit) //this is the extra stall stage following a lw in the mem stage that will produce a hazard with the following instruction in the EX stage
	       begin
		  instruction_D <= instruction_D;
		  op_D <= opcode_t'(instruction_D[31:26]);
		  pc_plus_4_D <= pc_plus_4_D;
		  predicted_D <= predicted_D;
		  
	       end
	     else if (d_dhit && ~d_ihit) //for the purposes of inserting a bubble right after a load word in MEM, since no instruction will have been fetched now. Instruction will onl be fetched in the next ifetch.
	       begin
		  instruction_D <= 32'b0;
		  op_D <= RTYPE;
		  pc_plus_4_D <= /*pc_plus_4*/32'h00000000;	
	   	  predicted_D <= 0;
		  
	       end
	  end // else: !if(~nRST)
     end // always_ff @ (negedge nRST, posedge CLK)

   //-------END OF FETCH--------------------------------------------------------------------

   
   //-----------DECODE--------------------------------------------------------------------

   assign cuif.imemload = instruction_D;

   assign rfif.WEN = regWrite_WB; //From Write Back
   assign rfif.rsel1 = instruction_D[25:21];
   assign rfif.rsel2 = instruction_D[20:16];
   assign rfif.wsel = wsel_WB; //fom Write Back
   assign rfif.wdat = wdat_WB; //from Write Back

   assign en_EX = (d_ihit || d_dhit);

   logic was_forwarding; //to handle the forwarding value being lost due to insertion of bubble after lw stage. WB-EX forwarding being lost due to lw being in the MEM stage.
   //logic was_forwarding_latch;

   always @ (posedge CLK, negedge nRST)
     begin
	if (~nRST)
	  begin
	     j_EX <= 0;
	     jal_EX <= 0;
	     jr_EX <= 0;
	     beq_EX <= 0;
	     bne_EX <= 0;
	     cu_halt_EX <= 0;
	     RegWrite_EX <= 0;
	     dREN_EX <= 0;
	     dWEN_EX <= 0;
	     RegDst_EX <= 0;
	     ExtOp_EX <= 0;
	     ShiftOp_EX <= 0;
	     MemToReg_EX <= 0;
	     lui_EX <= 0;
	     ALUSrc_EX <= 0;
	     ALUOp_EX <= ALU_SLL;
	     rdata1_EX <= 0;
	     rdata2_EX <= 0;
	     imm_EX <= 0;
	     rt_EX <= 0;
	     rs_EX <= 0;
	     rd_EX <= 0;
	     op_EX <= HALT;
	     pc_plus_4_EX <= 0;	    
	     instruction_EX <= 0;
	     predicted_EX <= 0;
	     
 	     
	  end // if (~nRST)
	else
	  //new part
	  if (branch_or_jump) begin //this is for the bubble in D, EX, M stages following a branch or a jump
	     j_EX <= 0;
	     jal_EX <= 0;
	     jr_EX <= 0;
	     beq_EX <= 0;
	     bne_EX <= 0;
	     cu_halt_EX <= 0;
	     RegWrite_EX <= 0;
	     dREN_EX <= 0;
	     dWEN_EX <= 0;
	     RegDst_EX <= 0;
	     ExtOp_EX <= 0;
	     ShiftOp_EX <= 0;
	     MemToReg_EX <= 0;
	     lui_EX <= 0;
	     ALUSrc_EX <= 0;
	     ALUOp_EX <= ALU_SLL;
	     rdata1_EX <= 0;
	     rdata2_EX <= 0;
	     imm_EX <= 0;
	     rt_EX <= 0;
	     rs_EX <= 0;
	     rd_EX <= 0;
	     op_EX <= RTYPE;
	     pc_plus_4_EX <= 0;	    
	     instruction_EX <= 0;
	     predicted_EX <= 0;
	     
	    end
	  else if ( d_dhit & bubble_lw_f ) begin //this is the extra stall stage following a lw in the mem stage that will produce a hazard with the following instruction in the EX stage
	     j_EX <= j_EX;
	     jal_EX <= jal_EX;
	     jr_EX <= jr_EX;
	     beq_EX <= beq_EX;
	     bne_EX <= bne_EX;
	     cu_halt_EX <= cu_halt_EX;
	     RegWrite_EX <= RegWrite_EX;
	     dREN_EX <= dREN_EX;
	     dWEN_EX <= dWEN_EX;
	     RegDst_EX <= RegDst_EX;
	     ExtOp_EX <= ExtOp_EX;
	     ShiftOp_EX <= ShiftOp_EX;
	     MemToReg_EX <= MemToReg_EX;
	     lui_EX <= lui_EX;
	     ALUSrc_EX <= ALUSrc_EX;
	     ALUOp_EX <= ALUOp_EX;
	     rdata1_EX <= (was_forwarding == 1'b1) ? aluif.portA : rdata1_EX;
	     rdata2_EX <= (was_forwarding == 1'b1) ? aluif.portB : rdata2_EX;
	     imm_EX <= imm_EX;
	     rt_EX <= rt_EX;
	     rs_EX <= rs_EX; //somehow the rs_EX values are messed up! eg: they become -ve
	     rd_EX <= rd_EX;
	     op_EX <= op_EX;
	     pc_plus_4_EX <= pc_plus_4_EX;
	     instruction_EX <= instruction_EX;
	     predicted_EX <= predicted_EX;
	     
	  end
	  
	  else if ( en_EX ) begin
	     j_EX <= cuif.j;
	     jal_EX <= cuif.jal;
	     jr_EX <= cuif.jr;
	     beq_EX <= cuif.beq;
	     bne_EX <= cuif.bne;
	     cu_halt_EX <= cuif.halt;
	     RegWrite_EX <= cuif.RegWrite;
	     dREN_EX <= cuif.dR_REQ;
	     dWEN_EX <= cuif.dW_REQ;
	     RegDst_EX <= cuif.RegDst;
	     ExtOp_EX <= cuif.ExtOp;
	     ShiftOp_EX <= cuif.ShiftOp;
	     MemToReg_EX <= cuif.MemToReg;
	     lui_EX <= cuif.lui;
	     ALUSrc_EX <= cuif.ALUSrc;
	     ALUOp_EX <= cuif.ALUOp;
	     rdata1_EX <= rfif.rdat1;
	     rdata2_EX <= rfif.rdat2;
	     imm_EX <= instruction_D[15:0];
	     rt_EX <= instruction_D[20:16];
	     rs_EX <= instruction_D[25:21]; //somehow the rs_EX values are messed up! eg: they become -ve
	     rd_EX <= instruction_D[15:11];
	     op_EX <= op_D;
	     pc_plus_4_EX <= pc_plus_4_D;
	     instruction_EX <= instruction_D;
	     predicted_EX <= predicted_D;
	     
	     
	  end // else if ( en_EX )
     end // always @ (posedge CLK, negedge nRST)

   //--------END OF DECODE--------------------------------------------------------------------------------------

   //----------EXECUTE-----------------------------------------------------------------------------------------

   
   word_t dmemload_M; //this is for the very specific case of stre forwarding when a load is followed by a store, and rd_M == rt_EX leading the value of the store forwarding to be dependent on the dmemload from RAM instead of porto_M
   assign dmemload_M = dpif.dmemload;
   
   //Shamt Extender
   assign shamt_extended = {27'b0, imm_EX[10:6]};

   //Sign Extender
   assign sign_ext = (ExtOp_EX) ? {{16{imm_EX[15]}}, imm_EX} : {16'b0, imm_EX}; //the rhs is the zero-extension, the lhs is the sign extension

   //AlUSrc Mux
   assign ALUSrc_output = ALUSrc_EX ? sign_ext : rdata2_EX;

   //ShiftOP MUX
   assign shiftOp_output = ShiftOp_EX ? shamt_extended : ALUSrc_output;
   
   //ALU
   assign aluif.aluOP = ALUOp_EX;
   assign aluif.portA = (fuif.forward_A == 2'b00 ? rdata1_EX : (fuif.forward_A == 2'b01 ? (lui_M == 1'b1 ? {imm_M, 16'b0} : porto_M) : wdat_WB) ); //forwarding unit....if there is a lw operation in the MEM stage, there CANNOT be a forwarding at that instant. used for the lw hazards in mem stage in fowarding unit.
   assign aluif.portB = (fuif.forward_B == 2'b00 ? shiftOp_output : (fuif.forward_B == 2'b01 ? (lui_M == 1'b1 ? {imm_M, 16'b0} : porto_M) : wdat_WB) ); //forwarding unit....if there is a lw operation in the MEM stage, there CANNOT be a forwarding at that instant. used for the lw hazards in mem stage in fowarding unit.
   
   assign was_forwarding = ( (fuif.forward_A != 2'b00) || (fuif.forward_B != 2'b00) ) && dREN_M == 1'b1; //basicall if there was a forwarding between the WB and the EX states while there was a load in the 

   
   //RegDst Mux
   assign RegDst_output = RegDst_EX ? rd_EX : rt_EX;

   //JAL Mux
   assign wsel_EX = jal_EX ? 31 : RegDst_output;

   //forwarding unit argument assignments
   assign fuif.WEN_M = regWrite_M;
   assign fuif.WEN_WB = regWrite_WB;
   assign fuif.rs_EX = rs_EX;
   assign fuif.rt_EX = rt_EX;
   assign fuif.wsel_M = wsel_M;
   assign fuif.wsel_WB = wsel_WB;
   assign fuif.is_ITYPE = (~(op_EX == RTYPE)) ? 1 : 0; //if the instruction in the EX stage is not an R-Type, then forwardB will always be 0
   assign fuif.dREN_M = dREN_M;
   assign fuif.is_bne_or_beq_M = (beq_EX == 1'b1) || (bne_EX == 1'b1);
   assign bubble_lw_f = fuif.bubble_lw_f; //this signal will stall all the latches preceding the MEM latch for an extra clock cycle. Futhermore, this signal signals the insertion of a bubble into the MEM stage and the propagaion of the MEM stage essentially meaning that the LW operation from the MEM stage will be the only one allowed to move through and then causing a data hazard with the oiginal MEM-EX hazard that is now resolvable since we will have gotten the correct value into the register.


   //store forwarding assignments
   assign sfif.dWEN_EX = dWEN_EX;
   assign sfif.rt_EX = rt_EX;
   assign sfif.rd_M = wsel_M;
   assign sfif.rd_WB = wsel_WB;

   //assign sw_forwarding_output = (sfif.forwarding_required == 2'b01 && dREN_M == 1'b1) ? dmemload_M : ( (sfif.forwarding_required == 2'b00) ? rdata2_EX : ( (sfif.forwarding_required == 2'b01) ? porto_M : ( (sfif.forwarding_required == 2'b10) ? wdat_WB : rdata2_EX))); //newly added code - (sfif.forwarding_required == 2'b01 && dREN_M == 1'b1) ? dmemload_M :  -> before

   assign sw_forwarding_output = (sfif.forwarding_required == 2'b01 && dREN_M == 1'b1) ? dmemload_M : ( (sfif.forwarding_required == 2'b00) ? rdata2_EX : ( (sfif.forwarding_required == 2'b01) ? (lui_M == 1'b1 ? {imm_M, 16'b0} : porto_M) : ( (sfif.forwarding_required == 2'b10) ? wdat_WB : rdata2_EX))); //newly added code - (sfif.forwarding_required == 2'b01 && dREN_M == 1'b1) ? dmemload_M. Also newly added code while debugging sungs test file allop_s - (lui_M == 1'b1 ? {imm_M, 16'b0} : porto_M). -> new code
   
  
   
   
   
   //MEM stage enabler logic
   assign en_M = d_ihit | d_dhit;
   

   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (~nRST)
	  begin
	     j_M <= 0;
	     jal_M <= 0;
	     jr_M <= 0;
	     beq_M <= 0;
	     bne_M <= 0;
	     dWEN_M <= 0;
	     dREN_M <= 0;
	     halt_M <= 0;
	     regWrite_M <= 0;
	     porto_M <= 0;
	     rdata2_M <= 0;
	     memToReg_M <= 0;
	     lui_M <= 0;
	     imm_M <= 0; //will use this now 
	     wsel_M <= 0;
	     op_M <= HALT;
	     pc_plus_4_M <= 0;
	     zero_M <= 0;
	     sign_ext_M <= 0;
	     rdata1_M <= 0;
	     instruction_M <= 0;
	     predicted_M <= 0;
	     
	  end // if (~nRST)
	else begin
	   if (branch_or_jump) begin //this is for the bubble in D, EX, M stages following a branch or a jump   
	      /*j_M <= j_M;
	      jal_M <= jal_M;
	      jr_M <= j_M;
	      beq_M <= beq_M;
	      bne_M <= bne_M;
	      dWEN_M <= dWEN_M;
	      dREN_M <= dREN_M;
	      halt_M <= halt_M;
	      regWrite_M <= regWrite_M;
	      porto_M <= porto_M;
	      rdata2_M <= rdata2_M;
	      memToReg_M <= memToReg_M;
	      lui_M <= lui_M;
	      imm_M <= imm_M;
	      wsel_M <= wsel_M;
	      jal_M <= jal_M;
	      op_M <= op_M;
	      pc_plus_4_M <= pc_plus_4_M;
	      zero_M <= zero_M;
	      sign_ext_M <= sign_ext_M;
	      rdata1_M <= rdata1_M;
	      instruction_M <= instruction_M;*/
	      j_M <= 0;
	      jal_M <= 0;
	      jr_M <= 0;
	      beq_M <= 0;
	      bne_M <= 0;
	      dWEN_M <= 1'b0;
	      dREN_M <= 1'b0;
	      halt_M <= 1'b0;
	      regWrite_M <= 1'b0;
	      porto_M <= 5'b00000;
	      rdata2_M <= 32'h00000000;
	      memToReg_M <= 1'b0;
	      lui_M <= 1'b0;
	      imm_M <= 16'h0000; //will use this now
	      wsel_M <= 5'b00000;
	      jal_M <= 1'b0;
	      op_M <= opcode_t'(6'b000000);
	      pc_plus_4_M <= 32'h00000000;
	      zero_M <= 0;
	      sign_ext_M <= 0;
	      rdata1_M <= 0;
	      instruction_M <= 0;
	      predicted_M <= 0;
	      
	     end
	   
	   //new part - just bubble out the whole MEM stage
	   else if ( d_dhit & bubble_lw_f ) begin //this is the extra bubble stage following a lw in the mem stage that will produce a hazard with the following instruction in the EX stage. Bubble will be poduced in the MEM stage
	      j_M <= 0;
	      jal_M <= 0;
	      jr_M <= 0;
	      beq_M <= 0;
	      bne_M <= 0;
	      dWEN_M <= 1'b0;
	      dREN_M <= 1'b0;
	      halt_M <= 1'b0;
	      regWrite_M <= 1'b0;
	      porto_M <= 5'b00000;
	      rdata2_M <= 32'h00000000;
	      memToReg_M <= 1'b0;
	      lui_M <= 1'b0;
	      imm_M <= 16'h0000; //will use this now
	      wsel_M <= 5'b00000;
	      jal_M <= 1'b0;
	      op_M <= opcode_t'(6'b000000);
	      pc_plus_4_M <= 32'h00000000;
	      zero_M <= 0;
	      sign_ext_M <= 0;
	      rdata1_M <= 0;
	      instruction_M <= 0;
	      predicted_M <= 0;
	      
	      
	   end
	  
	   else if ( en_M /*& ~dpif.halt*/) begin
	      j_M <= j_EX;
	      jal_M <= jal_EX;
	      jr_M <= jr_EX;
	      beq_M <= beq_EX;
	      bne_M <= bne_EX;
	      dWEN_M <= dWEN_EX;
	      dREN_M <= dREN_EX;
	      halt_M <= cu_halt_EX;
	      regWrite_M <= RegWrite_EX;
	      porto_M <= aluif.portO;
	      rdata2_M <= sw_forwarding_output;
	      memToReg_M <= MemToReg_EX;
	      lui_M <= lui_EX;
	      imm_M <= imm_EX;  //will use this now
	      wsel_M <= wsel_EX;
	      jal_M <= jal_EX;
	      op_M <= op_EX;
	      pc_plus_4_M <= pc_plus_4_EX;
	      zero_M <= aluif.zFlag; //the zero flag for branch resolution
	      sign_ext_M <= sign_ext << 2; //might cause an error -> for debugging search.asm, not using this signal anywhere. instead will use imm_M
	      
	      //rdata1_M <= rdata1_EX; // -> before
	      rdata1_M <= (jr_EX == 1 && fuif.forward_A == 2'b10) ? wdat_WB : ( (jr_EX == 1 && fuif.forward_A == 2'b01) ? porto_M : rdata1_EX);
	      //end of new code
	      
	      instruction_M <= instruction_EX;
	      predicted_M <= predicted_EX;
	      
	      
	   end // else if ( en_M )
	end // else: !if(~nRST)
     end // always_ff @


   //--------END OF EXECUTE----------------------------------------------------------------
   
   //---------MEMORY-----------------------------------------------------------------------

   /*word_t sign_ext_M_2;*/

   //logic halt_WB;
   
   //Cache
   assign dpif.dmemstore = rdata2_M;
   assign dpif.dmemaddr = porto_M;
   assign dpif.halt = halt_WB;
   assign dpif.dmemREN = dREN_M;
   assign dpif.dmemWEN = dWEN_M;

   //now the muxes for the branch taken or not, or the jumps
   
   assign beq_taken = zero_M && beq_M; //to check if the branch is due to beq or bne
   assign bne_taken = (~zero_M) && bne_M; //to check if the branch is due to beq or bne
   assign branch_taken = beq_taken || bne_taken;

   /*assign sign_ext_M_2 = sign_ext_M << 2;*/

   //for debugging search.asm purposes - new lines of code
   word_t imm16_sign_extended_1, imm16_sign_extended;
   assign imm16_sign_extended_1 = {{16{imm_M[15]}}, imm_M};
   //now shift left by 2
   assign imm16_sign_extended = imm16_sign_extended_1 << 2;
   //end of new lines of code for debugging search.asm purposes
   
   assign pc_when_branch = /*sign_ext_M_2*/ imm16_sign_extended + pc_plus_4_M; //where the change was made -> new code added for debugging search.asm
   assign pc_branch_mux = (branch_taken == 1'b1) ? pc_when_branch : pc_plus_4_M;
   ////end of the branch logic

   //jr logic
   
   assign jr_output = (jr_M == 1'b1) ? rdata1_M : pc_branch_mux;
   //end of jr logic

   ///j and jal logic
  
   assign jal_or_j = jal_M || j_M;
   
   assign intermediate_jump_op = instruction_M[25:0] << 2;
  
   assign jump_address = {pc_plus_4_M[31:28], intermediate_jump_op};
  
   assign pc_next_branch_jump = (jal_or_j == 1'b1) ? jump_address : jr_output;

  
   assign jump_taken = jal_or_j || jr_M;
   
   assign branch_or_jump = (branch_taken && ~predicted_M) || (~branch_taken && predicted_M) || jump_taken; //changing the flush logic


   //here we will write the btb code
   //1. check if the branch insruction address exists in the BTB
   logic does_exist;
   word_t branch_address;
   assign branch_address = pc_plus_4_M - 4;
   logic [27:0] tag_to_match;
   assign tag_to_match = branch_address[31:4];
   logic [1:0] 	get_index;
   assign get_index = branch_address[3:2];
   assign does_exist = ( ( (beq_M == 1'b1) || (bne_M == 1'b1) ) && ( (btbframes.frameblocks[get_index].valid == 1'b1) && (btbframes.frameblocks[get_index].tag == tag_to_match) ) );
   logic 	next_valid_bit;

   //end of 1

   //2. check if there was a mispediction in the F stage, which would mean that does_exist = 1, curr_state = 00||01 and branch_taken = 0, or does_exist = 1, curr_state = 10||11 and branch_taken = 1
   //flip flop logic for assigning next state only
   always_ff @(posedge CLK, negedge nRST)
     begin
	if (!nRST)
	  begin
	     btbframes.frameblocks[0].valid <= 0;
	     btbframes.frameblocks[1].valid <= 0;
	     btbframes.frameblocks[2].valid <= 0;
	     btbframes.frameblocks[3].valid <= 0;
	     //the other fields wouldn't matter since valid bit is set to 0
	  end
	else if ((does_exist == 1'b0 && ( (beq_M == 1'b1) || (bne_M == 1'b1) )) && d_ihit)
	  begin
	     btbframes.frameblocks[get_index].valid <= 1;
	     btbframes.frameblocks[get_index].tag <= tag_to_match;
	     btbframes.frameblocks[get_index].jump_add <= pc_when_branch;
	     btbframes.frameblocks[get_index].curr_state <= 2'b00; //set default value of the state to 00 - ST
	  end
	else if ((does_exist == 1'b1 && (branch_taken == 1'b1)) && d_ihit)
	  begin
	     //there was a mispediction where in the F stage we predicted not taken when it should have been taken
	     if (btbframes.frameblocks[get_index].curr_state == 2'b10) //WNT
	       begin
		  btbframes.frameblocks[get_index].curr_state <= 2'b01;
	       end
	     else if (btbframes.frameblocks[get_index].curr_state == 2'b11) //WNT
	       begin
		  btbframes.frameblocks[get_index].curr_state <= 2'b10;
	       end
	     else if (btbframes.frameblocks[get_index].curr_state == 2'b01) //WNT
	       begin
		  //correct pediction
		  btbframes.frameblocks[get_index].curr_state <= 2'b00;
	       end
	  end // if (does_exist == 1'b1 && (branch_taken == 1'b1))
	else if ((does_exist == 1'b1 && (branch_taken == 1'b0)) && d_ihit)
	  begin
	     //there was a mispediction where in the F stage we predicted taken when it should not have been taken
	     if (btbframes.frameblocks[get_index].curr_state == 2'b00) //WNT
	       begin
		  btbframes.frameblocks[get_index].curr_state <= 2'b01;
	       end
	     else if (btbframes.frameblocks[get_index].curr_state == 2'b01) //WNT
	       begin
		  btbframes.frameblocks[get_index].curr_state <= 2'b10;
	       end
	     else if (btbframes.frameblocks[get_index].curr_state == 2'b10) //WNT
	       begin
		  //correct pediction
		  btbframes.frameblocks[get_index].curr_state <= 2'b11;
	       end
	  end // if (does_exist == 1'b1 && (branch_taken == 1'b1))
	else
	  begin
	     /*
	     btbframes.frameblocks[0].curr_state <= btbframes.frameblocks[0].curr_state;
	     btbframes.frameblocks[1].curr_state <= btbframes.frameblocks[1].curr_state;
	     btbframes.frameblocks[2].curr_state <= btbframes.frameblocks[2].curr_state;
	     btbframes.frameblocks[3].curr_state <= btbframes.frameblocks[3].curr_state;
	      */
	  end
     end // always_ff @

   //end of 2
   
   
   //end of here we will write the btb code
   

   
   
   assign en_WB = d_ihit | d_dhit;
   
   
   

   always_ff @ (posedge CLK, negedge nRST )
     begin
	if (~nRST)
	  begin
	     memToReg_WB <= 0;
	     lui_WB <= 0;
	     regWrite_WB <= 0;
	     wsel_WB <= 0;
	     porto_WB <= 0;
	     dmemload_WB <= 0;
	     imm_WB <= 0;
	     halt_WB <= 0;
	     jal_WB <= 0;
	     op_WB <= HALT;
	     pc_plus_4_WB <= 0;

	     halt_WB <= 0;
	     
	  end
	else begin
	   if ((en_WB || branch_or_jump) && ~dpif.halt) begin //for the WB stage, for the bubble_lw_f signal i wouldn't matter since we need to popagate it forward. We just need it to caused and resolve a hazard through forward dependency between the WB-EX stages.
	      memToReg_WB <= memToReg_M;
	      lui_WB <= lui_M;
	      regWrite_WB <= regWrite_M;
	      wsel_WB <= wsel_M;
	      porto_WB <= porto_M;
	      dmemload_WB <= dpif.dmemload;
	      imm_WB <= imm_M;
	      halt_WB <= halt_M;
	      jal_WB <= jal_M;
	      op_WB <= op_M;
	      pc_plus_4_WB <= pc_plus_4_M;

	      halt_WB <= halt_M;
	      
	   end
	end // else: !if(~nRST)
     end // always_ff @
   
   //---------END OF MEMORY------------------------------------------------------------------

   //----------WRITE BACK-------------------------------------------------------------------
   
   //memToREg mux
   assign memToReg_out = memToReg_WB ? dmemload_WB : porto_WB;

   //jal mux
   assign jalWB_out = jal_WB ? pc_plus_4_WB : memToReg_out;
   
   //lui mux
   assign wdat_WB = lui_WB ? {imm_WB, 16'b0} : jalWB_out;
     
   //---------END OF WRITE BACK------------------------------------------------------------------

   
   
   
	      

endmodule
