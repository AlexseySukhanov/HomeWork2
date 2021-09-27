num=1234562342
i=1
dig=0
while num//10**i > 0 :
    i+=1
for j in range(i+1):
    dig+=((num%10**(j+1))//(10**j))*(10**(i-j-1))

print(int(dig))
