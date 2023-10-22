import random
d=['1','2','3','4','5','6','7','8','9']
random.shuffle(d)
n= [[d[0],d[1],d[2]],
    [d[3],d[4],d[5]],
    [d[6],d[7],d[8]]]
o=[['#','#','#'],['#','#','#'],['#','#','#']]
strok=9;stolb=9;hod=0
sum1=0;sum2=0;cont=1
ifunc1=19;jfunc1=19
for i in n:
    print(i,end='\n')
def aces1(i,j,n):
    if j==2 and (n[i][j-1]and n[i][j-2])=='#':
        return 0
    elif j==1 and (n[i][j+1]=='#' and n[i][j-1]=='#'):
        return 0
    elif j==0 and (n[i][j+1]=='#'and n[i][j+2]=='#'):
        return 0
    else:
        return 1
def aces2(i,j,n):
    if i==2 and n[i-1][j]=='#'and n[i-2][j]=='#':
        return 0
    elif i==1 and (n[i+1][j]=='#' and n[i-1][j]=='#'):
        return 0
    elif i==0 and (n[i+1][j]=='#' and n[i+2][j]=='#'):
        return 0
    else:
        return 1
while cont!=0:
    p=0
    if hod==0:
        if aces1(ifunc1,jfunc1,n)==1:
            chi1=str(input('1 igrok vvedi vibrannoe chislo: ')) 
            if strok==9:
                for i1 in range(len(n)):
                    for j1 in range(len(n[i1])):
                        if n[i1][j1]==chi1:
                            sum1+=int(chi1)
                            n[i1][j1]='#'
                            stolb=j1
                            ifunc2=i1
                            jfunc2=j1
                            for iii in n:
                                print(iii,end='\n')
                            print('summa 1 igroka=',sum1,'столбец для хода 2 игрока-',stolb+1)
                            hod=1                         
            elif strok !=9:               
                for j11 in range(len(n[strok])):
                    if n[strok][j11]==chi1:
                        p=1
                        sum1+=int(chi1)
                        n[strok][j11]='#'
                        stolb=j11
                        ifunc2=strok
                        jfunc2=j11
                        for j111 in n:
                            print(j111,end='\n')
                        print('summa 1 igroka=',sum1,'столбец для хода 2 игрока-',stolb+1)
                        hod=1
                if p==0:print("Ошибка, вы теряете ход :(");hod=1
        else: print('Ходов нет, ты лох :(');hod=1
    if n==o:cont=0                           
    if hod==1:
        if aces2(ifunc2,jfunc2,n)==1:
            chi2=str(input('2 igrok vvedi vibrannoe chislo: ')) 
            for i2 in range(len(n)):
                if n[i2][stolb]==chi2:
                    p=1
                    sum2+=int(chi2)
                    n[i2][stolb]='#'
                    strok=i2
                    ifunc1=i2
                    jfunc1=stolb
                    for i2 in n:
                        print(i2,end='\n')
                    print('summa 2 igroka=',sum2,'строка для хода 1 игрока-',strok+1)
                    hod=0                     
            if p==0:print("Ошибка, вы теряете ход :(");hod=0
        else: print('Ходов нет, ты лох :(');hod=0;pass
    if n==o:cont=0 
if sum1>sum2:print('первый игрок победил, второй игрок лох!')
elif sum1==sum2:print('ничья')
else:print('второй игрок победил, первый игрок лох!')