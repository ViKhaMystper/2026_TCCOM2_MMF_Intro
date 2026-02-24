# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Check that a user enter the full word or the 'n' letter/s of the word"""
    while True:
        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item

        print("Please enter a valid response.")


def instruction():
    """Prints out the instruction"""
    print('''
For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The programme still record the ticket sale and calculate 
the ticket cost (and the profit).

Once you have either sold all of the tickets or enter the exit code ('xxx'), the
programme will display the ticket sales information and write the data 
to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free)
''')


def not_blank(question):
    """Check that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("This cannot be blank. Please try again.")


def int_check(question):
    """Check users enter an integer"""
    error = "Oops - please enter an integer"

    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


# Main routine
MAX_TICKET = 5
tickets_sold = 0
payment_ans = ('cash', 'credit')

make_statement("Mini Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print()

while tickets_sold < MAX_TICKET:
    print()
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Ask for age INSIDE the loop
    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young for this movie")
        continue
    elif age > 120:
        print(f"{name} is too old for this movie")
        continue

    pay_method = string_check("Payment Method: ", payment_ans, 2)

    print(f"{name} has bought a ticket using {pay_method}")

    tickets_sold += 1

    if tickets_sold == MAX_TICKET:
        print(f"You have sold all the tickets (ie: {MAX_TICKET} tickets)")
    else:
        print(f"You have sold {tickets_sold} / {MAX_TICKET} tickets")