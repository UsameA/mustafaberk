#çarpımları 121212 olan ve aralarındaki en küçük farka sahip olan iki pozitif tamsayıyı veren program
y=1
for x in range(1,60606):
	for y in range(1,x):
		if x*y==121212:
			if x>y:
				print(x,y)
				break
	if x*y==121212:
			if x>y:
				break
