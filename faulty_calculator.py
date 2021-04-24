print("\t\t\t\t\t\t\tFAULTY CALCULATOR")

#Using if-elif-else only

n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
op = input("Enter the operation : ")

#Wrong answers will be dispayed for the below operations

if n1 == 56 and n2 == 9 and op == "+" :
    print("The result is : 77")
elif n1 == 45 and n2 == 3 and op == "*" :
    print("The result is : 555")
elif n1 == 56 and n2 == 6 and op == "/" :
    print("The result is : 4 ")
elif n1 != 56 and n2 != 9 and op == "+" :
    print("The result is : ",n1*n2)
elif n1 != 45 and n2 != 3 and op == "*" :
    print("The result is : ",n1/n2)
elif n1 != 56 and n2 != 6 and op == "/" :
    print("The result is :  ",n1+n2)

# Correct answer will be displayed for the below operations

elif op == "-" :
    print("The result is ", n1 - n2)
elif op == "**" :
    print("The result is : ", n1**n2)
elif op == "%" :
    print("The result is : ", n1 % n2)
else:
    print("Invalid choice")