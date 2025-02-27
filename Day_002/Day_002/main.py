tot_bill  =int(input("Welcome to the tip calculator! \n What was the total bill? $"))
tip=int(input("How much tip would you like to give? $"))
people_count=int(input("How many people to split the bill?"))
print(f"Each person should pay: ${(tot_bill+tip)/people_count}")
