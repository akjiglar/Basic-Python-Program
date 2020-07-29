a=[2,4,3]
print("no of elements:-",len(a))
c=len(a);
for i in range (0,3):
    for j in range (0,3):
        print(a[j:c])
        c--;
