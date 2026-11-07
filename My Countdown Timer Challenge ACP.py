def countdown(digit):
    if digit == 0:
        print("\nYour time is UP!!")
        return 
    print(digit)
    countdown(digit - 1)

first = int(input("\nEnter a number for countdown : "))
print()
countdown(first)

def buildunwind(step):
    if step == 0:
        print("\nThe base case has been reached. Now the undwinding begins!\n")
        return
    print(f"Building Level : {step}")
    buildunwind(step - 1)
    print(f"Unwinding Level : {step}")

second = int(input("\nEnter a number : "))
print()
buildunwind(second)

def countup(digit):
    if digit > 10:
        return

    print(digit)
    countup(digit + 1)

third = int(input("\nEnter a number (1 to 9) : "))
print(f"Counting from {third} to 10 :\n")
countup(third)

def factorial(digit):
    if digit == 0 or digit == 1:
        return 1

    return digit * factorial(digit - 1)

fifth = int(input("\nEnter a number : "))
print(f"{fifth}! : {factorial(fifth)}\n")

def unsafecountdown(digit):
    print(f"Number : {digit}\n⚠️  ALERT : This is Stack Overflow!!⚠️\nNote : Stack Overflow has not been completed because it will result in a 'RecursionError'.")

sixth = int(input("\nEnter a number : "))
unsafecountdown(sixth)