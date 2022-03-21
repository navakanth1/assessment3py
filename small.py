sum=1
found=0
for i in range(1000, 10000):
  a=i%10
  b=i//10%10
  c=i//100%10
  d=i//1000%10
  if (a!=b)&(a!=c)&(a!=d)&(b!=c)&(b!=d)&(c!=d)&(a+b+c+d==sum):
    found=True
    break
if found:
  print(i)
else:
  print('num not found')