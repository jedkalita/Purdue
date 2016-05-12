/*
  Eric Villasenor
  evillase@gmail.com

  this block is the coherence protocol
  and artibtration for ram
*/

// interface include
`include "cache_control_if.vh"

// memory types
`include "cpu_types_pkg.vh"

module memory_control (
  input CLK, nRST,
  cache_control_if.cc ccif
);
  // type import
  import cpu_types_pkg::*;

  // number of cpus for cc
  parameter CPUS = 2;
   
   //assign ccif.ramaddr = ((ccif.dWEN[0] == 1'b1) || (ccif.dREN[0] == 1'b1)) ? ccif.daddr[0] : ccif.iaddr[0] ;
   /*
   always_comb begin

      ccif.ramstore = ccif.dstore[0];
      ccif.ramWEN = ccif.dWEN[0];
      
      if (ccif.dWEN[0] == 1'b1)
	begin
	   ccif.ramREN = 1'b0;
	end
      else
	begin
	   if ((ccif.dREN[0] == 1'b1) || (ccif.iREN[0] == 1'b1))
	     begin
		ccif.ramREN = 1'b1;
	     end
	   else
	     begin
		ccif.ramREN = 1'b0;
	     end
	end // else: !if(ccif.dWEN[0] == 1'b1)
      
      ccif.iload[0] = ccif.ramload;
      ccif.dload[0] = ccif.ramload;

      

      if (ccif.ramstate == ACCESS)//the RAM is in the ACCESS state
	begin
	   if ((ccif.dREN[0] == 1'b1) || (ccif.dWEN[0] == 1'b1)) //give first priority to data read/write
	     begin
		ccif.dwait[0] = 1'b0;
	     end
	   else //the dwait signal should be high since no reading/writing of data takes place
	     begin
		ccif.dwait[0] = 1'b1;
		if ((ccif.iREN[0] == 1'b1))
		  begin
		     ccif.iwait[0] = 1'b0;
		  end
		else
		  begin
		     ccif.iwait[0] = 1'b1;
		  end
	     end // else: !if((ccif.dREN[0] == 1'b1) || (ccif.dWEN[0] == 1'b1))
	end // if (ccif.ramstate == ACCESS)
      else //the ram is in any other state including free, error, busy
	begin
	   ccif.iwait[0] = 1'b1;
	   ccif.dwait[0] = 1'b1;
	end // else: !if(ccif.ramstate == ACCESS)
      

      
   end // always_comb
    */

   assign ccif.ramstore = ccif.dstore[0];
   assign ccif.ramaddr = (ccif.dWEN[0] || ccif.dREN[0])? ccif.daddr[0] : ccif.iaddr[0];
   assign ccif.ramWEN = ccif.dWEN[0];
   assign ccif.ramREN = (ccif.dWEN[0])? 0 : ccif.dREN[0] || ccif.iREN[0];
   assign ccif.iload[0] = ccif.ramload;
   assign ccif.dload[0] = ccif.ramload;
   assign ccif.dwait[0] = ~((ccif.dREN[0] | ccif.dWEN[0]) & ccif.ramstate == ACCESS) ;
   assign ccif.iwait[0] = ~(~(ccif.dREN[0] | ccif.dWEN[0]) & ccif.iREN[0] & ccif.ramstate == ACCESS);
        
endmodule