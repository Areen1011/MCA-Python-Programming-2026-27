while True:

    num = int(input("Enter a number: "))

    choice = input("""1 - Check Prime
    2 - Check Palindrome
    3 - Check Armstrong
    4 - Check Factorial
    5 - Check Fibonacci Series
    6 - Exit
    Enter your choice: """)

    match choice:
        case '1':
            i = 2
            prime = True

            if num < 2:
                prime = False
            else:
                while i < num:
                    if num % i == 0:
                        prime = False
                        break
                    i = i + 1

            if prime:
                print("Prime number")
            else:
                print("Not a prime number")

        case '2':
            temp = num
            reversed_num = 0

            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp = temp // 10

            if num == reversed_num:
                print("Palindrome")
            else:
                print("Not Palindrome")

        case '3':
            sum_of_cubes = 0
            temp = num

            while temp > 0:
                digit = temp % 10
                sum_of_cubes += digit ** 3
                temp = temp // 10

            if num == sum_of_cubes:
                print("Armstrong number")
            else:
                print("Not an Armstrong number")

        case '4':
            factorial = 1

            for i in range(1, num + 1):
                factorial *= i

            print("Factorial of", num, "is:", factorial)

        case '5':
            a = 0
            b = 1

            print("Fibonacci series:")

            for i in range(num):
                print(a, end=" ")

            a, b = b, a + b
            print()

        case '6':
            print("Exiting the program.")
            break

        case _:
            print("Invalid choice. Please select a valid option.")