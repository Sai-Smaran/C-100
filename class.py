import math
from random import random


class ATM():
  def __init__(self, card_no, pin, withdrawamount):
    self.card_no = card_no
    self.pin = pin
    self.withdrawamount = withdrawamount

  def withdraw(self, card_no, pin->str, withdrawamount):

    # Check from a bunch of predefined card card_nos and pins.
    # If the card doesn't exist, then there is 75% chance that the transaction will be sucessful
    # Else, say that the card number is invalid or the pin is incorrect

    if card_no == "9091 8286 7684 3210" & pin == "8682":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "9876 5432 1012 3456" & pin == "2008":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "4575 4578 6454 8754" & pin == "8433":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "4242 4242 4242 4242" & pin == "0000":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "3651 8276 5028 9201" & pin == "1094":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "5351 6940 7963 4305" & pin == "6208":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    elif card_no == "6147 5631 6741 0366" & pin == "6534":
      print("Withdrawn amount of "+withdrawamount +
            ". Ramaining balance is"+math.floor(random()))
    else:
      if random() < 0.75:
        print("Withdrawn amount of "+withdrawamount +
              ". Ramaining balance is"+math.floor(random()))
      else:
        print("Error:\nAccount doesn't exist or you have entered the wrong pin.")

  def balanceeq(self, card_no, pin):

    # Check from a bunch of predefined card card_nos and pins.
    # If the card doesn't exist, then there is 75% chance that the balance will be returned
    # Else, say that the card number is invalid or the pin is incorrect
    if card_no == "9091 8286 7684 3210" & pin == "8682":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "9876 5432 1012 3456" & pin == "2008":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "4575 4578 6454 8754" & pin == "8433":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "4242 4242 4242 4242" & pin == "0000":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "3651 8276 5028 9201" & pin == "1094":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "5351 6940 7963 4305" & pin == "6208":
      print("Your balance is " + math.floor(random()*1000))
    elif card_no == "6147 5631 6741 0366" & pin == "6534":
      print("Your balance is " + math.floor(random()*1000))
    else:
      if random() < 0.75:
        print("Your balance is " + math.floor(random()*1000))
      else:
        print("Error:\nAccount doesn't exist or you have entered the wrong pin")


def checkInput():
  option = int(input())
  if option == 1:
    card_no = input("Please input your card number: ")
    pin = input("Please input your PIN: ")
    ATM(card_no, pin, 0).balanceeq(card_no, pin)
  elif option == 2:
    card_no = input("Please input your card number: ")
    pin = input("Please input your PIN: ")
    withdrawamount = input("Please input amount of money that you want to withdraw: ")
    ATM(card_no, pin, withdrawamount).withdraw(card_no, pin, withdrawamount)
  else:
    print("That is not a valid option. Please try again")
    checkInput()


def main():
  print("Welcome to CICICI bank ATM!\nWhat do you want to do today?\n1. Check balance\n2. Withdraw cash")
  checkInput()


if __name__ == "__main__":
  main()
