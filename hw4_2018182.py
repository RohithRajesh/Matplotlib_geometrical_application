#Name=Rohith Rajesh
#Roll Number=2018182
#Section=A
#Group=6



import matplotlib.pyplot as plt 
import math
class Matrix():
	def __init__(self):
		pass
	def multiply(self,m,n):
		l=[]
		for i in range(len(m)):
			sums=0
			x=0
			for j in m[i]:
				sums+=j*(n[x][0])
				x+=1
			l.append([sums])

		return l
# making a class of operations with 3 methods i.e scaling rotation and translation and calling them whenever required.
class Operations():
	def __int__(self):
		pass
	def scaling(self,m,x,y):
		m.append([1])
		scalar=[[x,0,0],[0,y,0],[0,0,1]]
		f=Matrix()
		g=f.multiply(scalar,m)
		return g[:2]
	def rotation(self,m,theta):
		theta=math.radians(theta)
		m.append([1])
		rotator=[[math.cos(theta),-math.sin(theta),0],[math.sin(theta),math.cos(theta),0],[0,0,1]]
		f=Matrix()
		g=f.multiply(rotator,m)
		return g[:2]
	def translation(self,m,dx,dy):
		m.append([1])
		translator=[[1,0,dx],[0,1,dy],[0,0,1]]
		f=Matrix()
		g=f.multiply(translator,m)
		return g[:2]
plt.ion()
'''
for a polygon:
	Output=== revised x and y coordinates respectively of the vertices in different lines
for an ellipse:
	Output: revised center and length of both semi axes with the axes along x mentioned first.
'''
s=input()
if s=="polygon":

	list_x=list(map(str,input().split()))
	list_y=list(map(str,input().split()))
	list_x=list(map(int,list_x))
	list_y=list(map(int,list_y))
	list_x.append(list_x[0])
	list_y.append(list_y[0])
	plt.axis('equal')
	plt.plot(list_x,list_y,'ro-',markersize=1)
	plt.show()
	while True:
		r=input()
		if r!='quit':
			if r[0]=='S':
				x,y=map(float,r[2:].split())
				g=Operations()
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.scaling(temp,x,y)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				for i in a[:-2]:
					print(round(i,3),end=' ')
				print()
				for i in b[:-2]:
					print(round(i,3),end=' ')
				print()
				
			if r[0]=='R':
				theta=float(r[2:])
				g=Operations()
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.rotation(temp,theta)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				for i in a[:-2]:
					print(round(i,3),end=' ')
				print()
				for i in b[:-2]:
					print(round(i,3),end=' ')
				print()
			if r[0]=='T':
				x,y=map(float,r[2:].split())
				g=Operations()
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.translation(temp,x,y)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				for i in a[:-2]:
					print(round(i,3),end=' ')
				print()
				for i in b[:-2]:
					print(round(i,3),end=' ')
				print()


		else:
			break

elif s=='disc':
	p=input()
	center_x,center_y,m,s=map(int,p.split())
	list_x=[]
	list_y=[]
	t=0
	while t<=2*(math.pi):
		list_x.append(center_x+m*math.cos(t))
		list_y.append(center_y+m*math.sin(t))
		t+=0.01
	plt.axis('equal')
	plt.plot(list_x,list_y,'ro-',markersize=1)
	plt.show()

	while True:
		r=input()
		if r!='quit':
			if r[0]=='S':
				x,y=map(float,r[2:].split())
				m=m*x				
				s=s*y
				g=Operations()
				clist=[]
				clist.append([center_x])
				clist.append([center_y])
				center_x=g.scaling(clist,x,y)[0][0]
				center_y=g.scaling(clist,x,y)[1][0]
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.scaling(temp,x,y)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.axis('equal')
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				print(round(center_x,3),round(center_y,3),m,s)
			if r[0]=='R':
				m=m
				s=s
				theta=float(r[2:])
				g=Operations()
				clist=[]
				clist.append([center_x])
				clist.append([center_y])
				center_x=g.rotation(clist,theta)[0][0]
				center_y=g.rotation(clist,theta)[1][0]
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.rotation(temp,theta)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				print(round(center_x,3),round(center_y,3),m,s)
			if r[0]=='T':
				x,y=map(float,r[2:].split())
				g=Operations()
				m=m
				s=s
				center_x+=x
				center_y+=y
				a=[]
				b=[]
				for j in range(len(list_x)):
					temp=[]
					temp.append([list_x[j]])
					temp.append([list_y[j]])
					l=g.translation(temp,x,y)
					
					a.append(l[0][0])
					b.append(l[1][0])
				a.append(a[0])
				b.append(b[0])
				list_x=a
				list_y=b
				plt.axis('equal')
				plt.plot(a,b,'ro-',markersize=1)
				plt.show()
				print(round(center_x,3),round(center_y,3),m,s)


		else:
			break



	

