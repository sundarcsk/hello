inpp="1,9,33,2,17,15,10,15,22,25"
strinp=inpp.split(',')
intinp=[]
for i in strinp:
    intinp.append(int(i))
# print(intinp)
tokens=0-int(intinp[0])
# print("tokens at initial is " +str(tokens))
positivevals=0
for i in range(0,len(intinp)-1):
    # print(intinp[i])
    sum=intinp[i]-intinp[i+1]+positivevals
    # print("sum for " +str(i)+ " value is " +str(sum))
    # print("token value is " +str(tokens))
    if(sum<0):
        tokens=tokens+sum
        positivevals=0
    else:
        positivevals=sum
print("the number of tokens he need to buy is " +str(abs(tokens)))