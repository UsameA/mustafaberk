#5 basamaklı asal sayıları ekrana yazdıran uygulama
for i in range(10000,100000):
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)
