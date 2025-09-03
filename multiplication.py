while True:
    rows = int(input("\nEnter number of rows: "))
    cols = int(input("Enter number of columns: "))
    search = int(input("Enter number to search: "))

    if rows <= 0 or cols <= 0:
        print("\nStop the loop. Goodbye!")
        break

    print("\nMultiplication Table:\n")
    found = False

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            value = i * j
            if value == search:
                print(f"[{value}]", end="\t")
                found = True
            else:
                print(value, end="\t")
        print()

    if found:
        print(f"\n{search} was found in the table.")
    else:
        print(f"\n{search} was NOT found in the table.")
