#4 basamaklı ilk rakamı son rakamından büyük olan sayıları yazdıran
#ve kaç tane olduğunu veren program
c=0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,i):
                print(1000*i+100*j+10*k+l)
                c+=1
print("Şu kadar sayı vadar",c)
