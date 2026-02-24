# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")

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


def instruction ():
    """Prints out the instruction"""
make_statement("Mini Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check ("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

make_statement("Instruction", "ℹ️")

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


print()
print("Program continues... ")