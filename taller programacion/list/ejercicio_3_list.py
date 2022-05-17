
A=[8,9,10]

A[1]=17

for i in range(4,7):
    A.append(i)
A.pop(0)

A.sort()

B=2*A

B.insert(3,25)
print(B)