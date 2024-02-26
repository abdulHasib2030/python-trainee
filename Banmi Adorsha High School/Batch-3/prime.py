

a = int(input("Enter a starting number: "))
b = int(input("Enter a Ending number: "))

for i in range(a,b):
    if i <=  1:
        continue
    elif  i <=3:
      print(i,end =' ')
    else:
        flag =True
        for j in range(2,i):
            if i %j ==0:
                flag=False
                break
        if flag ==True:
            print(i,end=" ")          














