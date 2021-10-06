import math
print("Program Menghitunhg Jarak Antara Titik A dan Titik B")
print("==============================")
Akon=input("Masukan Titik Kordinat Pertama : ")
A1=Akon.split(",")
Bkon=input("Masukan Titik Kordinat Kedua : ")
B2=Bkon.split(",")
Jarak = math.sqrt( ((int(A1[0])-int(B2[0]))**2)+((int(A1[1])-int(B2[1]))**2) )
print("Jarak antara ", Akon,"dan", Bkon,"adalah",Jarak)