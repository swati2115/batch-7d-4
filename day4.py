for i in range(1042000,702648265):
	sum=0
	temp=i
	while temp>0:
		t=temp%10
		sum=sum+t**3
		temp=temp//10
	if i==sum:
		print("The first armstrong number is:",i)
		break


		

