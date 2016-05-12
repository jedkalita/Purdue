#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-28 11:24:05 -0500 (Wed, 28 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab02/sorting.bash $:
 if [[ $# < 1 ]]
 then
     echo "Usage: ./sorting.bash <input file>"
     exit 1
 fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file"
    exit 2
fi
file=$1
i=0
fn=()
ln=()
cn=()
ad=()
city=()
cnty=()
st=()
zp=()
ph=()
fx=()
em=()
wb=()
ind=0
#fn[$ind]=$(echo $file | cut -d',' -f1)
#ln[$ind]=$(echo $file | cut -d',' -f2)
#	cn[$ind]=$(echo $file | cut -d',' -f3)
#	ad[$ind]=$(echo $file | cut -d',' -f4)
#	city[$ind]=$(echo $file | cut -d',' -f5)
#	cnty[$ind]=$(echo $file | cut -d',' -f6)
#	st[$ind]=$(echo $file | cut -d',' -f7)
#	zp[$ind]=$(echo $file | cut -d',' -f8)
#	ph[$ind]=$(echo $file | cut -d',' -f9)
#	fx[$ind]=$(echo $file | cut -d',' -f10)
#	em[$ind]=$(echo $file | cut -d',' -f11)
#	wb[$ind]=$(echo $file | cut -d',' -f12)
while (( 1 == 1 ))
do
echo "Your choices are: 
1) First 10 people
2) Last 5 names by highest zipcode 
3) Address of 6th-10th by reverse e-mail
4) First 12 companies
5) Pick a number of people
6) Exit"
read -p "Your choice: " response
echo $response

if (( $response == 1 ))
then 
    #while read file
    #do
    #echo $i
	
	    sort -k7,7 -k5,5 -k3,3 -k1,1 -t"," $1 | head -n 10
	    #let i=$i+1
	
	    
    #done < $1 
fi
if (( $response == 2 ))
then 
    #while read file
    #do
    #echo $i
	
	    sort -k8,8 -r -t"," $1 | head -n 5 | cut -d"," -f1,2
	
#done < $1
fi
if (( $response == 3 ))
then 
   # while read file
    #do
    #echo $i
	
	    sort -k11,11 -r -t"," $1 | head -n 6 | cut -d"," -f4
	
#done < $1
fi
if (( $response == 4 ))
then 
    #while read file
    #do
    #echo $i
	
	
	    sort -k3,3 -r -t"," $1 | head -n 11 | tail -n 5 | cut -d"," -f3
	
#done < $1
fi
if (( $response == 5 ))
then 
    #while read file
    #do
    #echo $i
	
	    read -p "Enter number of people: " num
	    sort -k2,2 -k1,1 -t"," $1 | head -n $num
	
#done < $1
fi
if (( $response == 6 ))
then 
    exit 0
fi
done
exit 0
