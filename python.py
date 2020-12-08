# python comprehension
def liv(lis):
  
  a=[ (lis[b][0] + " lives in " + lis[b][2] + " and "+("his"if lis[b][3]=="M" else "her") + " age is " + str(lis[b][1]) ) for b in range(len(lis)) ]
  
  print (a)
liv([('john',25,"USA","M"),("Seetha",30,"UK","F"),("preethi",35,"India","F")])