import pandas
import random


# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


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
    print(make_statement("Instruction", "ℹ️"))

    print('''
For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The programme will record the ticket sale and calculate 
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

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Main routine

# Initialize ticket numbers
MAX_TICKET = 5
tickets_sold = 0

# Initialize variables / non- default option
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE=7.50
ADULT_PRICE=10.50
SENIOR_PRICE=6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE=0.05

# List to hold ticket details
all_name = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict ={
    'Name': all_name,
    'Ticket price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# program main headings
print(make_statement("Mini Movie Fundraiser Program", "🍿"))

# ask user if they want to see the instruction and display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print()

# Loop to get name, age, payment details
while tickets_sold < MAX_TICKET:
    print()
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Ask for age INSIDE the loop
    age = int_check("Age: ")

    # output error messages / success messages
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket ($7.50)
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif age < 65:
        ticket_price = ADULT_PRICE

    # Senior citizen ticket ($6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    pay_method = string_check("Payment Method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge=0

    # If paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost, surcharge
    all_name.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# End of ticket loop

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total payable for each ticket
mini_movie_frame['Total'] = (mini_movie_frame['Ticket price']
                                 + mini_movie_frame['Surcharge'])
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# choose random winner...
winner = random.choice(all_name)

# find index of winner (ie: position in list)
winner_index = all_name.index(winner)

# retrieve winner ticket price and profit (so we can adjust
# profit numbers so that the winning ticket is excluded)
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# Currency formatting (uses currency function)
add_dollars = ["Ticket price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# output movie frame without index
mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"Total paid: ${total_paid:.2f}"
total_profit_string = f"Total profit: ${total_profit:.2f}"

adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f} which \n"
                        f"means our sales have decreased by ${ticket_won:.2f} and our \n"
                        f"profit decreased by ${profit_won:.2f}.")

# winnet announcement
lucky_winner_string = (f"The lucky winner is {winner}. "
                       f"Their ticket worth ${ticket_won} is free!")
final_total_paid_string = f"Total paid is now ${total_paid - ticket_won:.2f}"
final_total_profit_string = f"Total profit is now ${total_profit - profit_won:.2f}"


if tickets_sold == MAX_TICKET:
    num_sold_string = make_statement(f"You have sold all the tickets" 
                                     f"(ie: {MAX_TICKET} tickets)", "-")
else:
    num_sold_string = make_statement(f"You have sold {tickets_sold} / " 
                                     f"{MAX_TICKET} tickets", "-")

# Additional strings / headings
heading_string = make_statement("Mini Movie Fundraiser", "=")
ticket_details_headings = make_statement("Ticket Details", "-")
raffle_heading = make_statement("---Raffle Winner---", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "-")

adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f} which \n"
                        f"means our sales have decreased by ${ticket_won:.2f} and our \n"
                        f"profit decreased by ${profit_won:.2f}.")

# List of strings to be outputted / written to file
to_write = [heading_string, "\n",
            ticket_details_headings,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string,
            final_total_profit_string, "\n",
            num_sold_string]

# print area
print()
for item in to_write:
    print(item)

# create file to hold data (add. txt extension)
file_name = "MMF_ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")