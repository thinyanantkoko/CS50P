def main():
    #prompting the user to type in the text in camelCase
    camelCase = input("camelCase: ")

    print("snake_case: ", end = "")

    #swapping the case accordingly and printing out the corresponding text in snake_case
    for ch in camelCase:
        if ch.islower():
            print(ch, end = "")
        else:
            print("_" + ch.swapcase(), end = "")
    print()

main()