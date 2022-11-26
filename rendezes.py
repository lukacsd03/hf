A=[2,5,6,8,13,32,42,50,53,62,66,70,80,89,91]
N=len(A)

also= 0
felso = N
i = 0
while also <= felso:
    i+=1
    k=(felso+also)//2
    if 70 < A[k]:
        felso=k-1
    elif 70 > A[k]:
        also = k+1
    else:
        kimenet=True,k
        break
else:
    kimenet = False

print("Felső:"+felso)
print("Alsó:"+also)
print("Közép"+k)
print("Lépésszám"+i)

