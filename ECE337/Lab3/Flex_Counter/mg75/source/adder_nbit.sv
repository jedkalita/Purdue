`timescale 1ns / 100ps
module adder_nbit
#(
  parameter BIT_WIDTH = 4
)
(
	input wire [BIT_WIDTH - 1:0] a,
	input wire [BIT_WIDTH - 1:0] b,
	input wire carry_in,
	output wire [BIT_WIDTH - 1:0] sum,
	output wire overflow
);

wire [BIT_WIDTH:0] carrys;
genvar i;

assign carrys[0] = carry_in;
generate
  for(i = 0; i <= BIT_WIDTH - 1; i = i + 1)
  begin
    adder_1bit IX (.a(a[i]), .b(b[i]), .carry_in(carrys[i]), .sum(sum[i]), .carry_out(carrys[i+1]));
    always @ (a[i], b[i], carrys[i])
    begin
      #(2) assert(((a[i] + b[i] + carrys[i]) % 2) == sum[i])
              $info("Correct addition of nbit.");
        else
            $error("Incorrect additon of nbit .");
    end
  end
endgenerate
assign overflow = carrys[BIT_WIDTH];	
endmodule
