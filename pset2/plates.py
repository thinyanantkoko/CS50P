def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #valid min. and max. characters count of a vanity plate
    min = 2
    max = 6

    #to find the first number's index in plate, if numbers included
    first_num_idx = 0

    #checking characters count for validity of the plate
    if min <= len(s) <= max:
        #for the plate with only letters included
        if s.isalpha():
            return True
        #ensuring the whitespace and special characters not included
        elif s.isalnum() == False:
            return False
        #ensuring the plate starts with at least 2 letters
        elif s[:min].isalpha() == False:
            return False
        else:
            s = s[min:]
            for i in range(len(s)):
                if s[i].isdigit():
                    #ensuring the first number used is not 0
                    if s[i] == "0":
                        return False
                    else:
                        #first number's index
                        first_num_idx = i
                        break
            #ensuring only the numbers come, to the end of the plate, once the first number detected
            s = s[first_num_idx+1:]
            return s.isdigit()
    else:
        return False
    

main()