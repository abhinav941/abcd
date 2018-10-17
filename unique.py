from collections import Counter
n=(int)(input())
li=list(map(int,input().split()))
new_li=[x for x,y in Counter(li).items() if y>1]
if new_li:
    print(" ".join(map(str,(sorted(new_li)))))
else:
    print("Unique")
