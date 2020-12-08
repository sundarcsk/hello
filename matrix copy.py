inp="ABCDEFG#HIJKLMN#OPQRSTU#VWXYZAB#CDEFGHI#JKLMNOP#QRSTUVW"
# inp="ABCD#EFGH#IJKL#MNOP"
listinp=inp.split("#")
listOut=[]
rowLength=0
for i in listinp:
    # print(i)
    rowLength=len(i)
    listOut.append(list(i))
# print("Row Length = "+str(rowLength))
# print("Column Length = "+ str(len(listOut)))
factor=0
while(factor<3):
    print("Factor = " +str(factor))
    n=1
    while(n<3):
        prevEle=listOut[0+factor][0+factor]
        print("1st prev element "+prevEle)
        for i in range(0+factor,(len(listOut)-1)-factor):
            # print(listOut[i][0])
            temp=listOut[i+1][0+factor]
            listOut[i+1][0+factor]=prevEle
            prevEle=temp
        
        print("2nd prev element "+prevEle)

        for j in range(0+factor,rowLength-1-factor):
            # print(listOut[colLength-1][j])
            temp=listOut[len(listOut)-1-factor][j+1]
            listOut[len(listOut)-1-factor][j+1]=prevEle
            prevEle=temp

        print("3rd prev element "+prevEle)

        for k in range(len(listOut)-1-factor,0+factor,-1):
            # print(listOut[k][len(listOut)-1])
            temp=listOut[k-1][len(listOut)-1-factor]
            listOut[k-1][len(listOut)-1-factor]=prevEle
            prevEle=temp
        print("4th prev element "+prevEle)

        for m in range(rowLength-1-factor,0+factor,-1):
            temp=listOut[0+factor][m-1]
            listOut[0+factor][m-1]=prevEle
            prevEle=temp
        print("5th prev element "+prevEle)

        print("After "+str(n) +" completion of rotation")

        for i in listOut:
            print(i)
        n=n+1
    factor=factor+2
# print(len(listOut))
