'''
Created by Shouvik Dutta
gcd of array
'''
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
li=[1,2,3,4,5,6,7,8,9,10]
gc=li[0]
for i in range(1,len(li)):
   gc=gcd(li[i],gc)
print(gc)
