"""
@Author: Logan Herrera
@Date: 3/19/2020
The functionality of this class is to generate a montecarlo run of a flipped
coin on a case by case bases. It returns the results to the user.
"""
import random
from fractions import *

class FlipCoin:

    def __init__(self, cases, number):
        self.cases = cases
        self.number = number

#Print results of each case to the user
    @classmethod
    def giveResults(self, cases, number):
        for i in range(cases):
            answer = self.cointoss(number)
            print "Case: ", i+1
            print "Coin flipped ", number, " times."
            print "Heads:Tails " , answer
            print "\n"

#Simulate the coin Flip and record results in a list
    @classmethod
    def cointoss(self, number):
        recordList = []
        for i in range(number):
            flip_coin = random.choice(['H', 'T'])
            if flip_coin == 'H':
                recordList.append('H')
            else:
                recordList.append('T')
        return (recordList.count('H'), recordList.count('T'))

#Main function to take input from user to start monte-carlo run
def main():
    cases = int(input("How many cases? "))
    number = int(input("How many times do we flip the coin?"))
    fC = FlipCoin(cases, number,)
    fC.giveResults(cases, number)

#Creating modularity independence
if __name__== "__main__":
    main()
