import question_c
print("We will sum all even numbers from 0 to your input")
try_again = 'y'
while try_again == 'y' or try_again == 'Y' or try_again == 'yes' or try_again == 'YES':
    while True:
        try:
            num = int(input("Enter a number greater than 0: "))
            break
        except ValueError:
            print("Not a WHOLE Number")
    z = question_c.get_sum_of_evens(num)
    print (z)
    try_again = str(input("Enter 'Yes' or 'Y' if you would like to Try Again? "))
    if try_again == 'y' or try_again == 'Y' or try_again == 'YES' or try_again == 'yes':
        print("\nYou selected to try again!")
    else:
        print("Exiting Program")
        