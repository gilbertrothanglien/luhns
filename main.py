import sys


def checkValid(cnumber):  # Function for checking if the given card number is valid
    nCard = cnumber
    counted = 0  # Variable to add second to last digit
    nonCounted = 0  # Variable for the digits which are not counted

    for i in range(len(str(cnumber))):  # iterate through the number
        nonCounted = (nCard % 10) + nonCounted  # Taking the modulus of the uncounted and adding them
        nCard = int(nCard / 10)  # Dividing the number by 10 and taking the integer value of the digit
        checkNum = (nCard % 10) * 2
        checkNum = str(checkNum)

        if len(str(checkNum)) > 1:  # Condition checking if the length of the counted which is multipled by 2 is greater than 1
            for i in range(len(checkNum)):  # If the condition is true it will iterate through the number and add them seperately
                counted = int(checkNum[i]) + counted
        elif len(checkNum) <= 1:  # If the condition is false it will directly add the multiplied counted number to the counted number
            counted = int(checkNum) + counted

        nCard = int(nCard / 10)

    ans = counted + nonCounted

    if ans % 2 == 0:  # This checks if the sum of counted and uncounted last digit is 0
        return True
    else:
        return False


def checkType(cardNumber):  # Function to check the type of card if the card number passes the validation
    amex = ['4', '7']
    mas = ['1', '2', '3', '4', '5']
    # This condition checks what type of card it is according to the length of the card number and the starting digit of the card
    if len(cardNumber) == 15 and (cardNumber[0] == '3' and cardNumber[1] in amex):
        ctype = "AMEX"
        return ctype
    elif len(cardNumber) == 16 and (cardNumber[0] == '5' and cardNumber[1] in mas):
        ctype = "MASTERCARD"
        return ctype
    elif (len(cardNumber) == 13 or len(cardNumber) == 16) and cardNumber[0] == '4':
        ctype = "VISA"
        return ctype
    else:
        sys.exit("INVALID")


def main():
    card_number = input("Number: ")

    for i in range(len(card_number)):  # Iterate through the string of input and check if the given input is a number
        if card_number[i] >= '0' and card_number[i] <= '9':
            continue
            break
        elif card_number[i] < '0' or card_number[i] > '9':
            main()
            exit()

    if len(card_number) < 13 or len(card_number) > 16:  # Check the length of the card
        sys.exit("INVALID")

    cnumber = int(card_number)
    ans = checkValid(cnumber)

    if ans == True:  # If validation is True it will call the cardType function else it will exit
        cardType = checkType(card_number)
        print(cardType)
    else:
        sys.exit("INVALID")


main()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
