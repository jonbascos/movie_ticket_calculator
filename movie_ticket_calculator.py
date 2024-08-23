from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H")
current_hour = int(current_time)

adult_tickets = 5
child_tickets = 2.5
matinee_tickets = 1

number_of_adult_tickets = 0
number_of_child_tickets = 0
number_of_matinee_tickets = 0

purchase_tickets = True

while purchase_tickets:

    # Checks time if before 3pm for Matinee Pricing
    if current_hour < 15:
        number_of_matinee_tickets = int(input(f"How many matinee tickets do you need? "))
    else:
        number_of_adult_tickets = int(input(f'How many adult tickets do you need? '))
        number_of_child_tickets = int(input(f"How many child tickets do you need? "))

    total_adult = float(number_of_adult_tickets * adult_tickets)
    total_child = float(number_of_child_tickets * child_tickets)
    total_matinee = float(number_of_matinee_tickets * matinee_tickets)
    total = float(total_adult + total_child + total_matinee)
    break

print("Your total will be $" + "{:.2f}".format(total))

