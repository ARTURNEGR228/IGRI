#krestiki noliki
from turtle import *
from math import *
k=50
km=0
o=1
n=[[9,9,9],
   [9,9,9],
   [9,9,9]]
tracer(0)
shape('turtle')
getscreen().bgcolor('black')
pencolor('white')
for i in range(4):
    fd(3*2**0.5*k)
    rt(90)
fd(2**0.5*k);rt(90);fd(3*2**0.5*k); lt(90);fd(2**0.5*k);lt(90);fd(3*2**0.5*k);rt(90);fd(2**0.5*k)
rt(90);fd(2**0.5*k);rt(90);fd(3*2**0.5*k);lt(90);fd(2**0.5*k);lt(90);fd(3*2**0.5*k)
up();setpos(0,0); lt(90); fd(k);rt(90);fd(35); write('A');fd(2**0.5*k); write('B');fd(2**0.5*k); write('C')
up();setpos(0,0); rt(180); fd(k);lt(90);fd(35); write('1');fd(2**0.5*k); write('2');fd(2**0.5*k); write('3')
up();setpos(0,0); rt(135); fd(k*2**0.5);stamp();rt(45)
while o!=0:
    if o==1 and km==9:
        title('Nichya!');o=0;color('purple');write('Nichya!',font=('Verdana',30));ht()
        break
    p=str(textinput('KRESTIKI NOLIKI','hod 1 igroka:'))
    if p[0]=='A':zx=0
    if p[0]=='B':zx=1
    if p[0]=='C':zx=2
    if p[0]=='A':zx=0
    if p[0]=='B':zx=1
    if p[0]=='C':zx=2
    if n[zx][int(p[1])-1]!=0:
        n[zx][int(p[1])-1]=1
        if p[1]=='1':y=0
        elif p[1]=='2':y=2**0.5*k*-1
        elif p[1]=='3':y=2**0.5*k*2*-1
        if p[0]=='A':x=0
        elif p[0]=='B':x=2**0.5*k
        elif p[0]=='C':x=2**0.5*k*2
        setpos(x,y)
        down()
        rt(135);fd(2*k); lt(135);up();fd(2**0.5*k);lt(135);down();fd(2*k);rt(135);up()
        update()
        if n[0][0]+n[1][1]+n[2][2]==3 or n[0][2]+n[1][1]+n[2][0]==3 or [1,1,1] in n or n[0][0]+n[1][0]+n[2][0]==3 or n[0][1]+n[1][1]+n[2][1]==3 or n[0][2]+n[1][2]+n[2][2]==3:
            bk(k)
            title('Pobeda za Krestikom!');o=0;color('purple');write('Pobeda za Krestikom, Pozdravlyayu!',font=('Verdana',30));ht()
            break
    elif n[zx][int(p[1])-1]==0 : setpos(2**0.5*k*2,2*k); write('ОШИБКА!',font=('Verdana',16,'normal'));bk(15);write('Вы теряете ход :(',font=('Verdana',10)); up(); pass
    km=0
    for j in range(len(n)):
        for l in range(len(n)):
            if str(n[j][l])=='9':
                km+=1
    if o==1 and km==0:
        bk(k)
        title('  Nichya!');o=0;color('purple');write('Nichya!',font=('Verdana',30));ht()
        break
    q=str(textinput('KRESTIKI NOLIKI','hod 2 igroka:'))
    if q[0]=='A':zx=0
    if q[0]=='B':zx=1
    if q[0]=='C':zx=2
    if n[zx][int(q[1])-1]!=1:
        n[zx][int(q[1])-1]=0
        if q[1]=='1':y=(2**0.5*k/2)*-1
        elif q[1]=='2':y=(2**0.5*k/2)*-3
        elif q[1]=='3':y=(2**0.5*k/2)*-5
        if q[0]=='A':x=2**0.5*k
        elif q[0]=='B':x=2**0.5*k*2
        elif q[0]=='C':x=2**0.5*k*3
        setpos(x,y);down();circle(2**0.5*k/2,360);up()
        update()
        if n[0][0]+n[1][1]+n[2][2]==0 or n[0][2]+n[1][1]+n[2][0]==0 or [0,0,0] in n or n[0][0]+n[1][0]+n[2][0]==0 or n[0][1]+n[1][1]+n[2][1]==0 or n[0][2]+n[1][2]+n[2][2]==0:
            bk(k)
            title('Pobeda za Nolikom!');o=0;color('purple');write('Pobeda za Nolikom, Pozdravlyayu!',font=('Verdana',30));ht()
            break
    elif n[zx][int(p[1])-1]==1: setpos(2**0.5*k*2,2*k); write('ОШИБКА!',font=('Verdana',16,'normal'));bk(15);write('Вы теряете ход :(',font=('Verdana',10)); up(); pass
    km=0
    for j in range(len(n)):
        for l in range(len(n)):
            if str(n[j][l])=='9':
                km+=1
    if o==1 and km==0:
        bk(k)
        title('  Nichya!');o=0;color('purple');write('Nichya!',font=('Verdana',30));ht()
        break
update()
exitonclick()