#girilen 3 veya 4 basamaklı sayının palindromik olup olmadığını sorgulayan
#programdır
a=input("3 veya 4 basamaklı bir sayı giriniz: ")
b=str(a)
if (len(b)==3):
        if (b[0]==b[2]):
                print("Girdiğiniz sayi palindromiktir.")
        else:
                print("Girdiğiniz sayi palindromik değildir.")
elif (len(b)==4):
        if (b[0]==b[3]) and (b[1]==b[2]):
                print("Girdiğiniz sayi palindromiktir.")
        else:
                print("Girdiğiniz sayi palindromik değildir.")  
else:
        print("3 veya 4 basamaklı bir sayı giriniz!")
