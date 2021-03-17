#Soal 6:
while True:
    case=list(map(int,input().split()))
    if case[0]==case[1]==case[2]==0:
        break
    else:
        if case[1]-case[0]==case[2]-case[1]:
            N=2*case[2]-case[1]
            print('AP '+str(N))
        else:
            N=2*case[2]**2/case[1]/ 2
            print('GP '+str(N))

a,b,c,d,e = int(input())
x = list(a,b,c,d,e)


