#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print('Hello, my name is Jacob Sievert.')
username = input("What is you name?\n")
print('Hello, {0}!'.format(username))
favgame = input("What is your favorite game?\n")
print('My favorite game is Kingdom Hearts 2. I think they aced the balance of variety of gameplay mechanics without overloading the player.')
input("This project was made as an introductory project to a class. One of the questions we are asked to answer is if we have concerns for this class. Do you have any concerns going on in your life right now?\n")
print('I do not really have any concerns about this class at the moment.')
excitement = input("What are you excited about within the next week?\n")
print('I am very excited to run my next D&D campaign. I have homebrewed an entire new class that I call the Reality Shifter.')
stacker = input("Do you use stackoverflow?\n").lower().strip()
if (stacker == 'y' or stacker == 'yes'):
    print('My stackoverflow.com user number is 11991138. You can use that to look me up.')
else:
    print('Well, it is a great resource and you should start using it. My stackoverflow.com user number is 11991138. You can use that to look me up.')
gitter = input("Do you use Github?\n").lower().strip()
if (gitter == 'y' or gitter == 'yes'):
    print('Here is the url for my Github profile. https://github.com/jsievert73 You can use it to look at any new projects I will be working on.')
else:
    print('Well, it is a great resource and you should start using it. Here is the url for my Github profile. https://github.com/jsievert73 You can use it to look at any new projects I will be working on.')