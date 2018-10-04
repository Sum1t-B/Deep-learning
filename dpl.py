x1=[1,0,0,0,0]
x2=[1,0,0,1,1]
x3=[1,0,1,0,1]
x4=[1,0,1,1,1]
x5=[1,1,0,0,1]
x6=[1,1,0,1,1]
x7=[1,1,1,0,1]
x8=[1,1,1,1,1]
X=[x1,x2,x3,x4,x5,x6,x7,x8]
w=[0,0,-1,2]
u=None
tim=0
err = 0
while u!=w :
	tim = tim+ 1
	u=list(w)
	#print("again",tim)
	for i in range(8):
		#print("i:", i)
		#print("u:",u)
		#print("w:",w)
		y=X[i]
		#print("y:",y)
		s=0
		for r in range(4):
			#print("r:" ,r)
			#print("s:",s)
			s=s+(w[r]*y[r])
			#print("s:",s)
		if y[4] == 1 and s<0:
			err+=1
			#print("got<0", err)
			#print("u:", u)
			for rin in range(4):
			#	print("rin:" ,rin)
			#	print("w[rin]",w[rin])
			#	print("u[rin2]",u[rin])
				w[rin]=w[rin]+y[rin]
			#	print("w[rin]",w[rin])
			#	print("u[rin2]",u[rin])
			#print("w t:",w)
			#print("u t:", u)
			if u==w and i==7 and tim>=1:
			#	print("w is:", w)
				break
		elif y[4]==0 and s>=0:
			err+=1
			#print("got>=0",err)
			#print("u:", u)
			for rin in range(4):
			#	print("rin2:" ,rin)
			#	print("w[rin2]",w[rin])
			#	print("u[rin2]",u[rin])
				w[rin]=w[rin]-y[rin]
			#	print("w[rin2]",w[rin])
			#	print("u[rin2]",u[rin])
			#print("w q:",w)
			#print("u q:", u)
			if u==w and i==7 and tim>=1:
			#	print("w is d:", w)
				break
				

print ('The Answer is \n')
print (w)
