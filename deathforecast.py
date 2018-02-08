#-------------------------------------------------------------------------------
# userName:        module1
# Purpose:
#
# Author:      tolon
#
# Created:     10/02/2017

import random

randNum = random.randint(1, 100)


boredom = 0
talkingTooMuch = 0
badBreath = 0
tooMuchMaths = 0
chanceSurvive = 0
userName = " "
totChance = 100

userName = input("What is your userName?")

while len(userName) < 1 or len(userName) >21 or not (userName.isalpha()):
    print ("Your userName must contain 1 to 21 letters, no numbers or symbols.")
    userName = input("What is your userName?")

print ("Hello", userName +". This is your daily death forecast, brought to you by THE GRIM REAPER... \n")

boredom = random.randint(1, totChance)
print ("Your chance of dying from boredom today is: " +str(boredom) +"%")
totChance = totChance - boredom


talkingTooMuch = random.randint(1, totChance)
print ("Your chance of dying from teachers talking too much today is: " +str(talkingTooMuch) + "%")
totChance = totChance - talkingTooMuch


badBreath = random.randint(1, totChance)
print ("Your chance of dying from your best friend's bad breath today is: " +str(badBreath) + "%")
totChance = totChance - badBreath


tooMuchMaths = random.randint(1, totChance)
print ("Your chance of dying from too much maths today is: " +str(tooMuchMaths) + "%")
totChance = totChance - tooMuchMaths


chanceSurvive = totChance
print ("Your chance of surviving today is: " +str(chanceSurvive) + "% \n")

print ("Have a good day", userName +".")




