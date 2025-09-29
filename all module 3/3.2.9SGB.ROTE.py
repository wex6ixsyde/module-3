# 3.2.9   LAB   The break statement – Stuck in a loop
# PROGRAMMED BY SEAN GABRIEL B.ROTE
# BSIT 2-A
# SEPT 24, 2025

"""
Scenario

The break statement is used to exit/terminate a loop.
Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as
the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the
loop should terminate.

Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
"""


# solution 1
"""
word = "" #gumamit po ako ng empty string para ma-initialize yung variable na word
while word != "chupacabra": #gumamit po ako != para sa condition ng while loop para po maging infinite loop
    word = input("Enter a word: ")
    if word == "chupacabra": 
        print("You've successfully left the loop.") 
"""
     

# solution 2
"""
while True: #sa solution 2 po, gumamit po ako ng True kasi infinite loop din po yun (alternative way)
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

"""
