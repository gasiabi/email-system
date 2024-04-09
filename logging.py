# name1 = input("your name")
# age1 = input("your age")
#
# data1 = dict(name=name1,age=age1)
#
# print(data1)
import json

with open("5.json", "r") as plik:
    dane_json = json.load(plik)


print("\n1. Log in\n2. Register\n3. Exit")

n = int(input("Choose an option: \n"))
print()

# first option to log in
while True:

    if n == 1:
        your_email = input("Input your email: ")
        print()

        found_user = None
        for uzytkownik in dane_json:
            if uzytkownik.get("email") == your_email:
                found_user = uzytkownik
                break

        if found_user is not None:
            your_password = input("Input your password: ")
            print()
            if uzytkownik.get("password") != your_password:
                print("INVALID PASSWORD")

            else:
                print("LOGGED IN")
                break
        else:
            print("User not found, you need to register first.")
            print()
            answer = input("Do you want to register?\nyes or no?\n")
            print()
            if answer == "yes":
                your_new_email = input("Set your email: ")
                print()
                your_new_password = input("Set your password: ")
                print()
                data1 = dict(email=your_new_email, password=your_new_password)
                dane_json.append(data1)
                with open("5.json", "w") as plik1:
                    json.dump(dane_json, plik1, indent=2)
                break
            else:
                break

# second option to register

    elif n == 2:
        your_new_email = input("Set your email: ")
        your_new_password = input("Set your password: ")
        data1 = dict(email=your_new_email, password=your_new_password)
        dane_json.append(data1)
        with open("5.json", "w") as plik1:
            json.dump(dane_json, plik1, indent=2)
        break

    elif n == 3:
        break
    else:
        print("INVALID OPTION")
        n = int(input("Choose an option: \n"))





