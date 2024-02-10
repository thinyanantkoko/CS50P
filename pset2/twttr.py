def main():
    #prompting the user for a string of text
    txt = input("Input: ")

    vowels = ["a", "e", "i", "o", "u"]
    out_txt = ""

    #caseless checking of vowels' occurrences and omitting them in output text 
    for ch in txt:
        if ch.casefold() not in vowels:
            out_txt += ch

    #printing out the vowels-omitted text
    print(f"Output: {out_txt}")

main()