#iki rakamlı iki sayı var. bu sayıları yan yana getirdiğimizde elde edilen 
#4 rakamlı sayı bu iki sayının 11 katıdır. bu iki sayıyı bulan program
for i in range(10,100):
    for j in range(10,100):
        a=str(i)
        b=str(j)
        if int(a+b)==11*(i+j):
            print(i,j)
