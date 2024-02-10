def main():
    #a dict. object for nutrition info of 20 most frequently consumed raw fruits by U.S. FDA
    nutri_info = {
    "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
    "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80,
    "peach": 60, "pear": 100, "pineapple": 50, "plums": 70, "strawberries": 50, "sweet cherries": 100,
    "tangerine": 50, "watermelon": 80
    }

    #prompting user to type in the name of fruit(case-insensitively)
    item = input("Item: ").casefold()

    #looking it up in nutrition info and printing out the number of calories in one portion of that fruit
    if item in nutri_info:
        print(f"Calories: {nutri_info[item]}")

main()