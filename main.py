#This is the COS 101 assignment to calculate the compound interest and simple interest
#for the Yusuf and Sons business
#define formula for compound interest
def calculate_compound_interest(principal, rate, time, number_of_years):
    return principal * (1 + rate/number_of_years) ** number_of_years * time
#dsefine formula for simple interest
def calculate_simple_interest(principal, rate, time):
    return principal * (1 + rate * time)
#Collect User input
principal = float(input("Enter initial amount: "))
rate = float(input("Enter rate of interest per period: "))
time = float(input("Enter the number of times interest applied: "))
number_of_years = float(input("Enter the number of times interest compounded annually: "))
#Initialize variables
simple_interest = float(calculate_simple_interest(principal, time, rate))
compound_interest = float(calculate_compound_interest(principal, rate, time, number_of_years))
#Display values for effective information
print("Welcome to Yusuf and Sons Limited")
print(f"The simple interest amassed is: {simple_interest} naira")

print(f"The compound interest amassed is: {compound_interest} naira")











