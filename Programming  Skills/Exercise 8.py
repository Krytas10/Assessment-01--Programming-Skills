# Ex 8 ( Simple Research )

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "dave"]

search_name = input("Enter the name you want to search for:")

if search_name in names:
    print(f"{search_name} is found in the list.")
else:
    print(f"{search_name} is not found in the list.")