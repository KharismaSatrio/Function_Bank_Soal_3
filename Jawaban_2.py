#Soal 3

x= ([1,3,2,2,1,5,1,24,12,124,12,21,32,15])
def proses(x):
    ganjil =[]
    genap=[]
    gabungan=[]
    for i in x:
        if i % 2 == 0:
            genap.append(i)
            genap.sort(reverse=True)
        elif i % 2 !=0:
            ganjil.append(i)
            ganjil.sort()
            
    str(ganjil)
    str(genap)
    gabungan.append(ganjil)
    gabungan.append(genap)
    print(gabungan)

proses(x)