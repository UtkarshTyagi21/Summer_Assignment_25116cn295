#WAP to create voting eligibility system.
def check_voting_eligibility ():
    try:
        age = int(input("Enter your age: ")) #Prompt user for their age
        if age < 0: #Check if age is negative
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= 18: #Check if age is 18 or older
            print("Congratulations! You are eligible to vote.")
        else: #If under 18
            print("You are not eligible to vote yet.")
    except ValueError: #Handle non-integer inputs (like text)
        print("Invalid input. Please enter a numerical value for your age.")

#Run the program
if __name__ == "__main__":
    check_voting_eligibility()

