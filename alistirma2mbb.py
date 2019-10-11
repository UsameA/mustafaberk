#euler formülü ile pi sayısının yaklaşık değerini hesaplayan program
import math
sum=0
for i in range(1,10000000):
    sum=1/(i**2)+sum

pi= math.sqrt(6*sum)
print(pi)
    
