#Soal 2

a= (input('Masukkan Nomor HP: '))
def proses(a):
    b=str(a)
    n=len(b)
    c= (b[:1])
    d= (b[1:2])

    if n >13:
        print('Nomor HP hanya maksimal 13 angka')
    elif c != '0':
        print('Nomor HP harus dimulai dengan \"08\" ')
    elif d !='8':
        print('Nomor HP harus dimulai dengan \"08\" ')
    elif n <= 13:
        print('Nomor HP Saya Adalah', a)

proses(a)

