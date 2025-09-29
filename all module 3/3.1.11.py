#3.1.11   LAB   Essentials of the if-else statement
"""
Scenario
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid
taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be
paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Your task is to write a tax calculator.
It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding
for you

Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no
tax at all (the tax was equal to zero). Take this into consideration during your calculations.
"""
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 