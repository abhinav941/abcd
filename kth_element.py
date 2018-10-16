li=list(map(int,input().split()))
li_a=list(map(int,input().split()))
if li[0]>=li[1]:
  print(sum(li_a[:li[1]]))
else:
  print("invalid')
