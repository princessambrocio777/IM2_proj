"""print("Enter matrix: ")
num=int(input())

for x in range(1,11):
    for y in range (1,num+1):
        if x%2==0:
            print(f"*", end=" ")
        else:
            print(f"o", end=" ")
    print() """

print("Enter string: ")
str=input()

for z in str:
    print(z)

for a in range(len(str)):
    match str[a]:
        case "a":
          print(f"{str[a]} Vowel")
        case "e":
          print(f"{str[a]} Vowel")
        case "i":
          print(f"{str[a]} Vowel")
        case "o":
          print(f"{str[a]} Vowel")
        case "u":
          print(f"{str[a]} Vowel")
        case _:
          print(f"{str[a]} Vowel")