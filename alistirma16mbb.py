#girilen sayının asal olup olmadığını kontrol eden program
c=0
a=input("Bir sayi giriniz: ")
b=int(a)
for i in range(2,b):
      if(b%i==0):
            c+=1
            break
if(c!=0):
      print("Sayı asal değildir")
else:
      print("Sayı asaldır")
