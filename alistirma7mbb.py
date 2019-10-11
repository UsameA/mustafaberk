#ilk iki rakamının toplamı son rakamına eşit olan sayılar ve kaç tane olduğunu veren program
c=0
for i in range(1,10):
	for j in range (0,10):
		for k in range (0,10):
			if i+j==k:
				print(100*i+10*j+k)
				c=c+1
print("sayı adedi",c)
