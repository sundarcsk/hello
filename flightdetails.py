inpp="Sundar:1234567890:Delhi,Raman:234567890:Mumbai"
result=""
if(',' in inpp):
    strinpp=inpp.split(',')
    dummy=0
    # print(str(strinpp))
    for i in strinpp:
        sum=0
        dummy+=1
        coloninpp=i.split(':')
        # print(coloninpp)
        for num in coloninpp[1]:
            sum+=int(num)
        result+=coloninpp[0][:2]+str(sum)+coloninpp[2][-2:]
        if(len(strinpp)!=dummy):
            result+=','
else:
    coloninpp=inpp.split(':')
    for num in coloninpp[1]:
        sum+=int(num)
    result+=coloninpp[0][:2]+str(sum)+coloninpp[2][-2:]
print(result)
