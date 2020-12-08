inp=[16, 17, 4, 3, 5, 2]
out=[]
# for i in range(1,len(inp)):
#     sortt=[]
#     sortt=sorted(inp[i:])
#     out.append(sortt[len(sortt)-1])
# out.append(-1)
# print(out)
    # for j in range(0,len(inp)-1):

for i in range(1,len(inp)):
    greatval=inp[i]
    for j in range(i+1,len(inp)):
        if(i==len(inp)-1):
            greatval=inp[i+1]
        if(greatval>inp[j]):
            pass
        else:
            greatval=inp[j]
    out.append(greatval)
out.append(-1)
print(out)