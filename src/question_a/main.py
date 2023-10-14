import question_a
again = "yes" 

while again == "yes" or again == "y" or again == "Y" :

    num = input("ENTER A NUMBER ")
    num = int (num)
    y = question_a.is_prime(num)

    print (y)

    again = str(input("if you want to try again , Enter yes .If not enter any other character: "))

    if again != "yes" and again != "y" and again != "Y":

        print ("exiting program")