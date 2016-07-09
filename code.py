
import sys
r=1
c=0
pos=0
cu=0
f=0
d=0
n=input("enter order:") 
cross=n**n
print "no. of locations for traversal = ",cross
roll_die = "y"

flag=[[0 for j in range(n)] for i in range(n)]


def check( flag ):
	count=0

	for i in range(n):
		count=0
		for j in range(n):
			if(flag[i][j]==1):
				count=count+1
		if(count==n):
			print ("The row %d was completely visited\n" %i)
			return 1

	for i in range(n):
		count=0
		for j in range(n):
			if(flag[j][i]==1):
				count=count+1
		if(count==n):
			print ("The column %d was completely visited\n" %i)
			return 1

	return 0

import random
print ("Your initial position is... 0,0")


while roll_die=="y":
	
	rnd=(int)(((random.random()*100)%6)+1)
	print (" value on die is %d" %rnd)
	if((pos+rnd)>(n*n)):
		r=1
		c=0
		rnd=((pos+rnd)-(n*n))
		pos=0
	
	pos=pos+rnd
	c=c+rnd
		
	if(c>n):
		c=c%n
		r=r+1
	if(r%2==0):
		cu=n+1-c
	else:
		cu=c

	print ("Your current position is %d,%d" %(r-1,cu-1))

	flag[r-1][cu-1]=1

	f=check(flag)
	if(f==1):
		var=input("END")
		quit()
	d=0
	roll_die = raw_input("do you want to roll the dice again???- press 'y' or 'n' :")

print ("Your final position is %d,%d"  %(r-1,cu-1))