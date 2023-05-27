a,b,n=map(int,input('a b n > ').split())
s,p,n,z=[f(a,b) for i in range(n)],0,0,0
for i in s:
  if i < 0: N+=1
  elif i==0: Z+=1
  else: P+=1
print(min(s),max(s),N,P,Z)