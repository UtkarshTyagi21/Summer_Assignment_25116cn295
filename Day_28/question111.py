#WAP to create ticket booking system.
events = {"Movie A": 10, "Movie B": 5, "Movie C": 0} #Available movies/eventsand their remaining seats

ticket_price = 12 #Price per ticket in dollars

print("--- Welcome to the Ticket Booking System ---")

while True:
    print("\nAvailable shows and seats: ") #1. Display available options
    for event, seats in events.items():
        print(f"- {event}: {seats} seats left")

    choice = input("\nEnter event name to book (or try 'exit' to quit): ").strip()

    if choice.lower() == 'exit':
        print("Thank you for using our system!")
        break

    if choice in events:
        if events[choice] > 0: #3. Process booking
            try:
                num_tickets = int(input(f"How many tickets for {choice}? "))
                if num_tickets <= events[choice] and num_tickets > 0:
                    events[choice] -= num_tickets
                    total_cost = num_tickets * ticket_price
                    print(f" Success ! Booked {num_tickets} ticket(s) for {choice}.")
                    print(f"Total Amount Due: ${total_cost}")
                else:
                    print(f"Error: Not enough seats. Only {events[choice]} left.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        else:
            print("Sorry, this show is completely sold out !")
    else:
        print("Event not found. Please match the exact name and spelling.")