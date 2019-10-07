for i in range(1,10):
	for j in range (0,10):
		for k in range (0,10):
			for l in range(0,10):
				if i==l:
					if j==k:
						print(1000*i+100*j+10*k+l)