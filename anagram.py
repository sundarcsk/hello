inp='anagram','nagaram'
diction1={}
diction={}
choice=0
len1=len(inp[0])
len2=len(inp[1])
if(len1==len2):
    for i in inp:
        choice+=1
        for j in i:
            count=0
            if(j in diction1):
                count=diction1[j]
                count+=1
                diction1[j]=count
            else:
                count+=1
                diction1[j]=count
        if(choice%2!=0):
            diction=diction1.copy()
    shared_items = {k: diction[k] for k in diction if k in diction1 and (diction[k]*2) == diction1[k]}
    if(len(shared_items)==len(diction)):
        print('Anagram')
    else:
        print("not an anagram")
else:
    print("not an anagram")
# for x,y in diction.items():

#for x,y in dict.items():
#print(x,y)
