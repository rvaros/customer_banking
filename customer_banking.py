# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
class SavingsAccount:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    SavingsAccount(balance=0,interest=0)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    savings_interest_earned = balance * interest_rate * months
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_savings_balance = balance + savings_interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    set_balance(updated_savings_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    set_interest(savings_interest_earned)
    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
    updated_savings_balance, savings_interest_earned
class CDAccount:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    CDAccount(balance=0,interest=0)
    # Calculate interest earned
    # ADD YOUR CODE HERE
    cdinterest_earned = balance * interest_rate * months
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_cd_balance = balance + cdinterest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    set_balance(updated_cd_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    set_interest(cdinterest_earned)
    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
    updated_cd_balance, cdinterest_earned
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('Please insert savings balance: '))
    savings_interest = float(input('Please insert savings interest: '))
    savings_maturity = int(input('please insert number of months: '))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(SavingsAccount(updated_savings_balance, interest_earned))
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('Please set CD Balance: '))
    cd_interest = float(input('Please set CD interest: '))
    cd_maturity = int(input('Please set number of months: '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(CDAccount(updated_cd_balance, interest_earned))

if __name__ == "__main__":
    # Call the main function.
    return main