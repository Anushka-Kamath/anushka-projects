list1=[1 , 2, 3, 4, 5, 6, 7, 8]
list2=[16,15,14,13,12,11,10,9]
list3=[17,18,19,20,21,22,23,24]
list4=[32,31,30,29,28,27,26,25]
list5=[33,34,35,36,37,38,39,40]
list6=[48,47,46,45,44,43,42,42]
list7=[49,50,51,52,53,54,55,56]
list8=[64,63,62,61,60,59,58,57]



print list1
print list2
print list3
print list4
print list5
print list6
print list7
print list8

n=input("enter order:") 
cross=n*n
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
