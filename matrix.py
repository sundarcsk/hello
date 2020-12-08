# Matrix rotation
inp="ABCD#EFGH#IJKL#MNOP"
splinp=inp.split("#")
out=[]
for i in splinp:
    print(list(i))
    out.append(list(i))
# for one rotation
print(out)
for j in out:
    print(j)
# for j in i:
#     print(j)
# print(splinp)
n=1
print("After changing")
# print(len(out))
while(n<3):
    print(len(out))
    for i in range(0,len(out)):
        for j in range(0,len(out)):
            if((i!=len(out)-1)&(j==0)):
                out[i+1][j]=splinp[i][j]
                print("out[i+1][j]" +str(i) +" "+ str(j)+" "+ splinp[i][j])
            if((i==0)&(j!=0)):
                out[i][j-1]=splinp[i][j]
                print("out[i][j-1]" +str(i) +" "+ str(j)+" "+ splinp[i][j])
            if((i==(len(out)-1))&(j!=(len(out)-1))):
                out[i][j+1]=splinp[i][j]
                print("out[i][j+1]" +str(i) +" "+ str(j)+" "+ splinp[i][j])
            if((i!=0)&(j==(len(out)-1))):
                out[i-1][j]=splinp[i][j]
                print("out[i-1][j]" +str(i) +" "+ str(j)+" "+ splinp[i][j])
    n=n+1
    for i in out:
        print(i)
    print("Internal change")
    splinp=out
    for j in splinp:
        print(j)
for i in out:
    print(i)

#inp="ABCDEF#GHIJKL#MNOPQR#STUVWX#YZABCD#EFGHIJ"