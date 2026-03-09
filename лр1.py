s="HELLO WORLD"
print(s[0])
print(s[10])
print(s[7:])
#------1--------
a=input("Введите строку:")
if len(a)%2==0:
    print(a.upper())
else:
   print(a.lower())
#------2---------
t=input("Введите строку:")
sm={'a','e','i','o','u'}
SM={'A','E','I','O','U'}
st=0
g=0
for i in range(len(s)):
    if s[i] in sm:
         st+=1
    if s[i] in SM:
         g+=1
print(st)
print(g)
#-----3-----

S = str(input())
result = ""
for i in range(len(S)):
    if i==0 or S[i]!=S[i-1]:
       result +=S[i]
print(result)
#----4----
first = str(input())
second = str(input())
sl1= set(first)
sl2 = set(second)
count = False
if sl1 == sl2:
    count= True
else:
    count = False
print(count)
#-----5-----