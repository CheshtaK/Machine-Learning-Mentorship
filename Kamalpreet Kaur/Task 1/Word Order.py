#Enter your code here. Read input from STDIN. Print output to STDOUT
li={}
for i in range(int(input())):
    n=input();
    if n not in li:
        li[n]=1
    else:
        li[n]=li[n]+1
#print(li)
print(len(li))
for i in li:
    print(li[i],end=" ") 
