num=88888888
i=1
sum=0
while num//10**i > 0 :
    sum+=(num%10**i)//(10**(i-1))

    i+=1
sum+=num//10**(i-1)
print(sum)
