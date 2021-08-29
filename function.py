def most_frequent(s):
  d={}
  sset=sorted(list(set(s)))
  for i in sset:
    v=s.count(i)
    d[i]=v
  dd=sorted(d.items(),key=lambda kv:kv[1],reverse=True) 
  for i in dd:
    print(i[0],"=",i[1],end=" ")

s=input("Please enter a string:").lower()
most_frequent(s) 
