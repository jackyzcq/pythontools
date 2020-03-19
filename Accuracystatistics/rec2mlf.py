#-*- coding:utf-8 -*-
import os,sys

def to_mlf(xi):
    dx={
       b"0":"零",
       b"1":"一",
       b"2":"二",
       b"3":"三",
       b"4":"四",
       b"5":"五",
       b"6":"六",
       b"7":"七",
       b"8":"八",
       b"9":"九"
    }
    d=[]
    eng=[]
    tx=[",",".","!","(",")","，","。","！",'；','、','：','？','“','”',"'"];
    for x in xi:
        u=x.encode("utf-8")
        if u in tx:
            continue;
        if len(u)==1:
            if u in dx:
                u=dx[u]
                d.append(u.upper())
            else:
                eng.append(str(u, encoding='utf-8'))
            #print(u)
            #print(str(u, encoding='utf-8'))
            #eng.append(str(u, encoding='utf-8'))
            
        else:
            if len(eng)>0:
                d.append("".join(eng).upper())
                eng=[]
            d.append(str(u, encoding='utf-8'))
    if len(eng)>0:
            d.append("".join(eng).upper())
    return d

def fn_to_lab(s):
    x=s.split()
    for i in x:
        d=to_mlf(i.strip())
        if len(d)>0:
            print("\n".join(d))
    print('.')

fn=sys.argv[1]
print('#!MLF!#')
for l in open(fn):
    l=l.strip()
    if l.startswith("logid:"):
        continue;
    x=l.split()
    k=x[0].strip()
    v=" ".join(x[1:])
    t=".".join(k)
    print('"*No%s.rec" ' % t)
    fn_to_lab(v)