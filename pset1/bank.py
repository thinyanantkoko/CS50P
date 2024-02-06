def main():
    greeting = input("Greeting: ")
    greeting = greeting.lstrip().casefold()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()