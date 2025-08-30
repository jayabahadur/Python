# l1=[1, 2,3,4,5]
# l2=list(map(lambda number:number**2, l1))

# print (l1)
# print (l2)

l1= [1,2,3]
l2=[3,5,6]
l3= [7,8,9]
l4=list(map(lambda a,b,c: a+b+c, l1,l2,l3))

print (l4)
