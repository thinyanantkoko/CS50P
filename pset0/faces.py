def main():
    txt = input("Enter some text: ")
    print(convert(txt))

def convert(txt):
    return txt.replace(":)", "🙂").replace(":(", "🙁")

main()