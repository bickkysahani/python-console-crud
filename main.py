# Python Console CRUD App for Insight Workshop Academy
from crud import CRUD, Registration
import sendemail

def programs():
    print("Please select a program:")
    print("1. Python Workshop")
    print("2. Java Workshop")
    print("3. C++ Workshop")
    print("4. C# Workshop")
    print("5. Go Workshop")
    # print("6. Exit")
    program = input("Please select a program: ")
    if program == "1":
        program = "Python Workshop"
    elif program == "2":
        program = "Java Workshop"
    elif program == "3":
        program = "C++ Workshop"
    elif program == "4":
        program = "C# Workshop"
    elif program == "5":
        program = "Go Workshop"
    return program

def first():
    print("Welcome to Insight Workshop Academy CRUD App")
    print("Please select an option:")
    print("1. Create/Read/Update/Delete an account")
    print("2. Register for a program at Insight Workshop Academy [Must have an account already created!]")
    print("3. Exit")

def registratiom_choices():
    print("Please select an option:")
    print("1. Register for a program")
    print("2. Read all registered users")
    print("3. Update a registered user")
    print("4. Delete a registered user")
    print("5. Go back to main menu")

def display_choices():
    print("Please select an option:")
    print("1. Create a new account")
    print("2. Read all accounts")
    print("3. Update an account")
    print("4. Delete an account")
    print("5. Go back to main menu")

while True:
    first()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print('-'*60)
        display_choices()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user = CRUD()
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            user.create(name, email)
            user.close()
        elif choice == 2:
            user = CRUD()
            users = user.read()
            print(users)
            user.close()
        elif choice == 3:
            user = CRUD()
            users = user.read()
            print(users)
            id = int(input("Enter the id of the user you want to update: "))
            name = input("Enter the new name: ")
            email = input("Enter the new email: ")
            user.update(id, name, email)
            user.close()
        elif choice == 4:
            user = CRUD()
            users = user.read()
            print(users)
            id = int(input("Enter the id of the user you want to delete: "))
            user.delete(id)
            user.close()
        elif choice == 5:
            continue
        else:
            print('-'*40)
            print("Invalid choice. Please try again.")
            print('-'*40)


    elif choice == 2:
        print('-'*60)
        registratiom_choices()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            program = programs()
            # print(program)
            user = CRUD()
            reg = Registration()
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            #check if this name and email is in users table or not
            emails = user.read_emails()
            # print(emails,type(emails))
            for mail in emails:
                if email == list(mail)[0]:
                    reg.create(name, email, program)
                    #send email to user
                    sendemail.email_alert('Insight Workshop Registration', name + " You have successfully registered for the " + program + " program.", email)
                    reg.close()
                    user.close()
                    break
                else:
                    continue
            else:
                print('-'*60)
                print("You donot have a account in our database. Please create a account first then try to register for a program.")
                print('-'*60)
                
        elif choice == 2:
            user = Registration()
            users = user.read()
            print(users)
            user.close()
        elif choice == 3:
            user = Registration()
            users = user.read()
            print(users)
            id = int(input("Enter the id of the user you want to update and then select a program: "))
            #select a new program
            program = programs()
            user.update(id, program)
            user.close()
        elif choice == 4:
            user = Registration()
            users = user.read()
            print(users)
            id = int(input("Enter the id of the user you want to delete: "))
            user.delete(id)
            user.close()
        elif choice == 5:
            continue
        else:
            print('-'*40)
            print("Invalid choice. Please try again.")
            print('-'*40)

    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print('-'*60)
        print("Invalid choice. Please try again.")
        print('-'*60)
    
