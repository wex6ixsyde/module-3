#3.1.10   LAB   Comparison operators and conditional execution
"""
Scenario
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that
filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it
involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

Write a program that utilizes the concept of conditional execution, takes a string as input, and:
prints the sentence "Yes - Spathiphyllum is the best 
plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
"""

flower = input("Enter the name of the flower: ")
if flower == "Spathiphyllum":
    print("Spathiphyllum is the best plant ever!")
elif flower == "spathiphyllum":     
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ",  flower, "!")
    
#alternative solution
"""
flower = input("Enter the name of the flower: ")
if flower == "Spathiphyllum":
    print("Spathiphyllum is the best plant ever!")
elif flower == "spathiphyllum":     
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {flower}!")
"""