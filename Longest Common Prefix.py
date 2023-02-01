def longestCommonPrefix(strs):
    strs=sorted(strs)
    l1=len(strs[0])
    l2=len(strs)
    s=""
    for i in range(l1):
        l=strs[0][i]
        c=0
        for j in range(l2):
            if strs[j][i]!=l:
                break
            c+=1
        if c!=l2:
            break
        else:
            s+=l
    return s

strs=["dog","racecar","cars"]
res=longestCommonPrefix(strs)
print(res)