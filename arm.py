def isArmstrong(x):
      
    number = 153
    temp = number
    add_sum = 0
    while temp!=0:
        k = temp%10
        add_sum +=k*k*k
        temp = temp//10
    if add_sum==number:
        print('Armstrong Number')
    else:
        print('Not a Armstrong Number')

x = 153
print(isArmstrong(x))
  
x = 1253
print(isArmstrong(x))


