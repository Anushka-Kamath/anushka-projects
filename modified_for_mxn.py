
n=input("enter column order:") 
m=input("enter row order:")
cross=n*m
print "no. of locations for traversal = ",cross
c=0

flag=0
r=1
pos=0
roll_die = "y"
cs=0
import random
print "Your initial position is 0,0"
while roll_die=="y" and flag==0:
	rd=(int)(((random.random()*100)%6)+1)
	print ("Value on die.... %d" %rd)
	
	if(pos+rd>cross):
		print ("Cannot add the dice value \n")
	else:
		pos=pos+rd
		c=c+rd
		
		if(c>n):
			c=c%n
			r=r+1
		if(r%2==0):
			cs=n+1-c
		
		else:
			cs=c

	print ("Current position is %d,%d" %(r-1,cs-1))
	roll_die = raw_input("do you want to roll the dice again???- press 'y' or 'n' :")
	if(pos==cross):
		flag=1;
		print ("final")

print ("final position is %d,%d" %(r-1,cs-1))