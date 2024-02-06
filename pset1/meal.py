def main():
    #prompting the user for a time, either in 24-hour or 12-hour format
    t = input("What time is it? ")

    if t.endswith(("a.m.", "p.m.")):
        #splitting the time and its marker, if included
        t, mkr = t.split()
        #converting the time to the corresponding num of hours
        tm = convert(t, mkr)
    else:
        tm = convert(t)

    #checking the time to tell user what to eat when
    match tm:
        case tm if 7.00 <= tm <= 8.00:
            print("breakfast time")
        case tm if 12.00 <= tm <= 13.00:
            print("lunch time")
        case tm if 18.00 <= tm <= 19.00:
            print("dinner time")


def convert(time, marker = None):
    hours, minutes = time.split(":")
    hours = float(hours)

    #checking the time marker whether or not to change it into 24-hour time
    if marker == "p.m." and hours != 12:
        hours += 12
    minutes = float(minutes) / 60

    return hours + minutes


if __name__ == "__main__":
    main()