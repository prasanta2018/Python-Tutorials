'''
Q3: Jack and his three friends have decided to go for a trip by sharing the expenses of the fuel equally.

Write a Python program to calculate the amount (in Rs) each of them need to put in for the complete (both to and fro) journey.
The program should also display True, if the amount to be paid by each person is divisible by 5, otherwise it should display False. (Hint: Use the relational operators in print statement.)

Assume that mileage of the vehicle, amount per litre of fuel and distance for one way are given.

'''
# Answer:

#PF-Assgn-3
#This verification is based on string match.

# PRE-CAUTION: To verify the code in InfyTq platform, Only use the following inputs as per them, otherwise InfyTq platform shows incorrect Solution

mileage = 12
amount_per_litre = 40
distance_one_way = 190
per_head_cost = 0
divisible_by_five = False

distance_two_way = 2 * distance_one_way
total_amount_of_fuel = distance_two_way / mileage
total_expense = total_amount_of_fuel * amount_per_litre

# as total persons = 4
per_head_cost = total_expense / 4

if(per_head_cost % 5 == 0):
    divisible_by_five = True

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
