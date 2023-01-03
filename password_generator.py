#Password Generator
new_password="yes"
while new_password == "yes":
    print("\n") 
    user_name=input("Please enter your name: ")
    print("\n")
    print("\n")
    print("                                                     ","Hi" , user_name, "Welcome to Virgil Password Generator")
    print("_________________________________________________________________________________________________________________________________________________________________")

    #Creating lists of letters,numbers and characters.
    upper_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    characters=['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','{','}']

    #Inputs
    try:        
        print("\n")
        nr_upper_letters = int(input("How many uppercase letters would you like in your password? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")
        print("\n")
        nr_lower_letters = int(input("How many lowercase letters would you like in your password? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")
        print("\n")
        nr_symbols = int(input(f"How many symbols would you like? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")
        print("\n")
        nr_numbers = int(input(f"How many numbers would you like? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")

    except:
        print("\n")
        print("Please enter a valid number")  
        print("\n")
        print("Try again ;) ")  
        print("_______________________________________________________________________________________________________________________________________________________________")
        nr_upper_letters = int(input("How many uppercase letters would you like in your password? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")
        nr_lower_letters = int(input("How many lowercase letters would you like in your password? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")
        nr_symbols = int(input(f"How many symbols would you like? "))
        print("\n") 
        print("_______________________________________________________________________________________________________________________________________________________________")
        nr_numbers = int(input(f"How many numbers would you like? "))
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________")


    #Importing random function to generate random numbers,characters and letters for the password.
    import random

    #Creating a list to store the password
    pin=[]

    for char in range(1, nr_upper_letters + 1):
            pin.append(random.choice(upper_letters))

    for char in range(1, nr_lower_letters + 1):
            pin.append(random.choice(lower_letters))

    for char in range(1, nr_numbers + 1):
            pin.append(random.choice(numbers))

    for char in range(1, nr_symbols + 1):
            pin.append(random.choice(characters))
        
    random.shuffle(pin)

        

    password=""
    for char in pin:
        password += char

    #Convert list to string 
    pwd = ''.join(pin)
    print("\n")
    print(f"Your password is : {pwd}") 
    print("\n")
    print("_______________________________________________________________________________________________________________________________________________________________")
    

    new_password ="no"
    print("\n")
    new_password = str(input("Do you want to generate another password (yes/no)? "))
    print("\n")
    print("________________________________________________________________________________________________________________________________________________________________")
    continue
print("\n")
print("Thankyou and have a great day.")
