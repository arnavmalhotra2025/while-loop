#Activity 1
#input the value of terms 
n = int(input("enter the value of terms:"))

sum = 0 
i = 1
while i <= n:
    sum = sum+i
    i = i+1
    
print ("\n sum =", sum)

#Activity 2
#infinity loop
#i = 0
#while i <= 0:
   # print("I WILL RUN FOREEVER")
   
#activity 3
# amstrong number sum of digit to cubes of number is equals to number
num = int(input("enter a number:"))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
if num == sum:
    print (num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
    