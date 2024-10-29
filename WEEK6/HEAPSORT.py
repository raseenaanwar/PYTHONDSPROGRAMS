def heapify(a,n,i):
    large=i
    lchildIndex=2*i+1
    rchildIndex=2*i+2
    if lchildIndex<n and a[large]<a[lchildIndex]:
        large=lchildIndex
    if rchildIndex<n and a[large]<a[rchildIndex]:
        large=rchildIndex
    if large!=i:
        a[i],a[large]=a[large],a[i]
        heapify(a,n,large)

def heapSort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)

a=[12,11,13,5,6,7]
heapSort(a)
print("Soretd array is")
for i in range(len(a)):
    print(a[i])
