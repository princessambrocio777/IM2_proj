mydict = {
    0: "underwear",
    1: "tank top",
    2: "jacket"
}

print("You have 3 items in the cart")

while True:
    action = input("\nWhat would you like to do [A]dd [C]hange items [R]emove [D]isplay  S[earch] ? ").strip().lower()

    if action == "*":
        print("Bye")
        break

    elif action == "d":
        print("\nDisplaying Values")
        print(f"{'Key':<8} {'Value'}")
        for key, value in mydict.items():
            print(f"{key:<8} {value}")

    elif action == "s":
        search = input("\nEnter item to search: ").strip()
        found = False
        for key, value in mydict.items():
            if value.lower() == search.lower():
                print(f"Found {value} item")
                found = True
                break
        if not found:
            try:
                key = int(search)
                if mydict.get(key) is None:
                    print("I'm sorry, not in the cart")
                else:
                    print(f"Found item: {mydict[key]}")
            except ValueError:
                print("Invalid input. Please enter a valid item name or key.")

    elif action == "r":
        key_input = input("\nEnter key to search: ").strip()
        try:
            key = int(key_input)
            value = mydict.get(key)
            if value is not None:
                del mydict[key]
                print(f"The key {key} with value {value} has been deleted")
            else:
                print("I'm sorry, not in the cart")
        except ValueError:
            print("Key not found")

    elif action == "c":
        key_input = input("\nEnter key to search: ").strip()
        try:
            key = int(key_input)
            value = mydict.get(key)
            if value is not None:
                print(f"Found {value} item")
                new_value = input("Enter value: ").strip()
                mydict[key] = new_value
            else:
                print("I'm sorry, not in the cart")
        except ValueError:
            print("Invalid key")

    elif action == "a":
        try:
            new_key = int(input("\nEnter new key (integer): ").strip())
            if new_key in mydict:
                print(f"Key {new_key} already exists with value '{mydict[new_key]}'")
            else:
                new_value = input("Enter item name: ").strip()
                mydict[new_key] = new_value
                print(f"Item '{new_value}' added with key {new_key}")
        except ValueError:
            print("Invalid key. Please enter an integer.")

    else:
        print("Invalid option. Please choose A, C, R, D, S or * to exit.")
