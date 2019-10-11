#1 ile 999 arasında rakamları toplamı 9 dan küçük sayıları yan yana yazdıran program
for i in range(1,9):
    print(i,end=" ")
for j in range(10,100):
    b=str(j)
    if (int(b[0])+int(b[1]))<9:
        print(int(b),end=" ")
for k in range(100,1000):
    c=str(k)
    if (int(c[0])+int(c[1])+int(c[2]))<9:
        print(int(c),end=" ") 
