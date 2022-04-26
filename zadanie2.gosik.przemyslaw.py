
def funkcja(x):
        return (x*x)+(3*x)-5
def sortowanie(f,n):
    i=1
    while i<n:
        j=i-1
        pom=f[i]
        while j>=0 and f[j]<pom:
            f[j+1]=f[j]
            j-=1
        f[j+1]=pom
        i+=1
    return f
a=0
b=-1
while a>b:
    a=int(input("Podaj dolny wymiar"))
    b=int(input("Podaj gorny wymiar"))
n=((b-a)*1000)+1
X=[0]*n
i=0
while i<n:
    X[i]=a+(i/1000)
    i+=1
print(X)
i=0
f=[0]*n
while i<n:
    f[i]=funkcja(X[i])
    i+=1
print(f)
f=sortowanie(f,n)
print(f)



