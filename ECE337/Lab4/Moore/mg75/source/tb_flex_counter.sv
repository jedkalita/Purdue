`timescale 1ns / 10ps
	localparam NUM_CNT_BITS = 4;
module tb_flex_counter();
  reg tb_clk;
	reg tb_n_rst;
	reg tb_count_enable;
	reg tb_clear;
	reg [NUM_CNT_BITS-1:0] tb_rollover_val;
	reg [NUM_CNT_BITS-1:0] tb_count_out;
	reg tb_rollover_flag;

	//DUI portmaps
	flex_counter DEFAULT
	(
	 .clk(tb_clk),
	 .n_rst(tb_n_rst),
	 .count_enable(tb_count_enable),
	 .clear(tb_clear),
	 .rollover_val(tb_rollover_val),
	 .count_out(tb_count_out),
	 .rollover_flag(tb_rollover_flag)
	 );
	 
	 // basic test bench parameters

	localparam	CLK_PERIOD	= 2.5;
	localparam	CHECK_DELAY = 1; 
	 
	 // Clock generation block
	always
	begin
		tb_clk = 1'b0;
		#(CLK_PERIOD/2.0);
		tb_clk = 1'b1;
		#(CLK_PERIOD/2.0);
	end
	
	initial
	begin		
		@(negedge tb_clk); 
		tb_n_rst = 1'b1; //reset with inactive inputs
		tb_count_enable = 1'b0; //count is enabled
		tb_clear = 1'b0; //not cleared
		tb_rollover_val = 1;
		#(0.1);
		tb_n_rst = 1'b0;
		#(CHECK_DELAY);
		if (tb_count_out == 4'b0000)
		  $info("Test case passed for counter");
		else
		  $error("Test case failed for counter.");
		if (tb_rollover_flag == 1'b0)
		  $info("Test case passed for rollover");
		else
		  $error("Test case failed for rollover.");
		  
		@(negedge tb_clk); 
		tb_n_rst = 1'b1; //reset with active inputs
		tb_count_enable = 1'b1; //count is enabled
		tb_clear = 1'b1; //not cleared
		tb_rollover_val = 1;
		#(0.1);
		tb_n_rst = 1'b0;
		#(CHECK_DELAY);
		if (tb_count_out == 4'b0000)
		  $info("Test case passed for counter");
		else
		  $error("Test case failed for counter.");
		if (tb_rollover_flag == 1'b0)
		  $info("Test case passed for rollover");
		else
		  $error("Test case failed for rollover.");
		  
		@(negedge tb_clk); 
		tb_n_rst = 1'b1; //reset with active inputs
		tb_count_enable = 1'b1; //count is enabled
		tb_clear = 1'b0; //not cleared
		tb_rollover_val = 5;
		
		@(posedge tb_clk);
		#(CLK_PERIOD * 4);
		#(CHECK_DELAY);
		if (tb_count_out == 4'b0101)
		  $info("Test case passed for counter");
		else
		  $error("Test case failed for counter.");
		if (tb_rollover_flag == 1'b1)
		  $info("Test case passed for rollover");
		else
		  $error("Test case failed for rollover."); 
		  
		@(negedge tb_clk); 
		tb_n_rst = 1'b1; //reset with active inputs
		tb_count_enable = 1'b1; //count is enabled
		tb_clear = 1'b1; //not cleared
		tb_rollover_val = 5;
		
		@(posedge tb_clk);
		#(CLK_PERIOD * 4);
		#(CHECK_DELAY);
		if (tb_count_out == 4'b0000)
		  $info("Test case passed for counter");
		else
		  $error("Test case failed for counter.");
		if (tb_rollover_flag == 1'b0)
		  $info("Test case passed for rollover");
		else
		  $error("Test case failed for rollover.");
	end
endmodule