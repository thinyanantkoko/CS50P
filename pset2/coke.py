def main():
    #amount due for a bottle of Coke(in cents)
    amt_due = 50

    coin = 0
    total_paid = 0

    #a bool flag, to check whether the customer has paid the total amount due or yet
    payment_clear = False


    while amt_due > 0:
        #ensuring the customer paying only the certain denominations of cents,  
        #and re-prompt for it until they comply
        while coin not in [25, 10, 5]:
            #printing out the amount due
            print(f"Amount Due: {amt_due}")
            coin = int(input("Insert Coin: "))

        #calculating the amount due yet to pay
        amt_due -= coin
        total_paid += coin

        if total_paid < 50:
            #resetting the coin value
            coin = 0
        else:
            payment_clear = True


    if payment_clear == True:
        #printing out the change owed to customer(in cents)
        print(f"Change Owed: {abs(amt_due)}") 


main()