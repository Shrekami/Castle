# a=[1,2,5,2,4,7,2,4,6,9,2,3,4,1,5,2,6,7,3]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)

# a = [3,5,7,9,11]
# b = []
# for i in range(len(a)):
#     if i %2==0:
#         b.append(a[i])
# print(b)

# a=["tail","body","head"]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)

# a=[9,1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,5,15]
# b=[]
# for i in range(len(a)-1,-1,-1,):
#     b.append(a[i])
# print(b)

# print(a[::-1])
# for i in range(10000,-1,-1):
#     print(i)

# a=int(input('Type range you want '))
# b=[]
# for i in range(1,a+1):
#     b.append(i)
# print(b)

# a=[1,2,-15,4,5]
# b=[]
# for i in a:
#     b.append(i*-1)
# print(b)

# a=[1,2,3,3,2,2,2,3,3,3,2,3,4,5,6,6,5,4,45]
# print(a[3:16:2])


a=['bicycle','jarmony','flick','sheep','flick']
b=[]
c=True
for i in a:
    if i!='flick':
        b.append(c)
    else:
        c=not c
        b.append(c)
print(b)