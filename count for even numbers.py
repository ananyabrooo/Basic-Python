i=1
count=0
n=int(input("n:"))
while i<=n:
    if(i%2==0):
        count=count+1
    i=i+1
print(f"count of even numbers={count}")
