

lis4 = []
num0 = 0
num1 = 0
num2 = -1
#maunit = 0
for i in IN[0]:

	num2 = num2+1
	if num2==4:
		num2 = 0
		num1 = num1+1
		if num1 == 6:
			num1 = 0
			num0 = num0+1	


		
	Anno = str(num0+1)+"."+str(num1+1)+"."+str(num2+1)
	lis4.append(Anno)	

		

OUT = lis4