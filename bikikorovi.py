#biki korovi
from turtle import *
from math import *
perv=1;vtor=1;xx=str(input('chislo 1 igroka:'));xy=str(input('chislo 2 igroka:'));y1=xx;y2=xy
while perv!=0 or vtor!=0:
    x1=[u1 for u1 in xx ];x2=[u2 for u2 in xy]
    if x2==['*']*4:perv=0
    f=[t for t in str(input('vvedite dogadku(1 igrok):'))]
    for i in range(4):
        if f[i]==x2[i]:x2[i]='*'
        elif f[i]in x2: x2[x2.index(f[i])]='#'
    if x2==['*']*4:perv=0; break
    print('kolichestvo bikov:',x2.count('*'),'kolichestvo korov:',x2.count('#'))
    g=[w for w in str(input('vvedite dogadku(2 igrok):'))]
    for j in range(4):
        if g[j]==x1[j]:x1[j]='*'
        elif g[j]in x1: x1[x1.index(g[j])]='#'
    if x1==['*']*4:vtor=0; break
    print('kolichestvo bikov:',x1.count('*'),'kolichestvo korov:',x1.count('#'))
if perv==0:
    print('pobeda za pervim igrokom!, chislo pervogo igroka:',y1,'chislo vtorogo igroka:',y2)
if vtor==0:
    print('pobeda za vtorim igrokom!, chislo pervogo igroka:',y1,'chislo vtorogo igroka:',y2)