n = int(input())

while n>0:
    l=int(input())
    dic={}
    for i in range(l):
        k=int(input())
        if k in dic:
            dic[k]+=1
        else:
            dic[k]=1
        print(dic.values)
    n-=1