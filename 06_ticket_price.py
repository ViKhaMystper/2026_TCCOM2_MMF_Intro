# Function goes here
def int_check(question):
    """Check users enter an integer"""
    error = "Oops - please enter an integer"

    while True:

        try:
            response = int(input(question))  # Return the response if it's an integer

            return response

        except ValueError:
            print(error)

def not_blank(question):
    """Check that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Check that a user enter the full word or the 'n' letter/s of the word from
    a list of valid responses"""
    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            elif response == item [:num_letters]:
                return item


# Main routine goes here
# Initialize variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE=7.50
ADULT_PRICE=10.50
SENIOR_PRICE=6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE=0.05

# Looping for testing purpose...
while True:
    print()

    # Ask users for their name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask for their age and check that it's between 12 and 120
    age = int_check("Age: ")

    # output error messages / success messages
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket ($7.50)
    elif 12 <= age < 16:
        ticket_price=CHILD_PRICE

    # Adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price=ADULT_PRICE

    # Senior citizen ticket ($6.50)
    elif 65 <= age < 121:
        ticket_price=SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # Ask users for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment Method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge=0

    # If paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # Calculate total payable...
    total_to_pay= ticket_price + surcharge

    print(f"{name}'s ticket cost is ${ticket_price:.2f}, they pay by {pay_method}"
          f" so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")
