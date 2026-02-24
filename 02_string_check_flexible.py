# Function go here
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

        print(f"Please choose an option from {valid_answers}")


# main routine goes here
# payment_ans = ('cash' or 'credit')
payment_list =["cash", "credit"]

while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()

# play_method = string_check("Payment methods: ", payment_ans, 2)
# print(f"You chose {play_method}")