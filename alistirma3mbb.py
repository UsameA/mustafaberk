#euler formülü sayesinde e sayısını hesaplayan program
import math
sum=0
for i in range(1,1000):
    sum=sum+(1/(math.factorial(i)))
print(sum)
