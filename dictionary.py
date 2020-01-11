s=input("enter string")
if(s[0]==' ' or s[0]=='_'):
    print ("error rerun")
p=s[0]+".txt"
f=open(p)
cnt=len(s)-(s.count(' ')+s.count('_'))
dic={}
c=0
for i in range(0,len(s)):
    if(s[i]!=' ' and s[i]!="_"):
        dic[i]=s[i]
print(dic)
for line in f:
    word=line.split()
    for wrd in word:
        for i in range(0,len(wrd)):
           if(i in dic.keys() and wrd[i]==dic[i]):
               c+=1
        if(cnt==c):
            print(wrd)
            c=0
        c=0
                    
            
    
