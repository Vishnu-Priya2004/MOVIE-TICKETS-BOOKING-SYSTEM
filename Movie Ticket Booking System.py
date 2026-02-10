class MovieTicketBooking:
    def __init__(self):
        self.movies = {
            1: {"name": "JOE", "price": 250},
            2: {"name": "SIRAI", "price": 300},
            3: {"name": "HI NANNA", "price": 280}
        }
        self.seats = [["A1", "A2", "A3", "A4"],1
                      ["B1", "B2", "B3", "B4"],
                      ["C1", "C2", "C3", "C4"],
                      ["D1", "D2", "D3", "D4"]]
        self.booked_seats = []
    def display_movies(self):
        print("\n Available Movies:")
        for key, value in self.movies.items():
            print(f"{key}. {value['name']} - ₹{value['price']} per ticket")
    def display_seats(self):
        print("\n Available Seats:")
        for row in self.seats:
            for seat in row:
                if seat in self.booked_seats:
                    print(f"[X]", end=" ")  # X = booked
                else:
                    print(f"[{seat}]", end=" ")
            print()
    def book_ticket(self):
        self.display_movies()
        choice = int(input("\nEnter the movie number you want to watch: "))
        if choice not in self.movies:
            print("Invalid choice. Please restart.")
            return
        selected_movie = self.movies[choice]["name"]
        ticket_price = self.movies[choice]["price"]
        tickets = int(input(f"How many tickets for {selected_movie}? "))
        self.display_seats()
        chosen_seats = []
        for i in range(tickets):
            seat = input(f"Select seat {i+1}: ").upper()
            if seat in self.booked_seats:
                print(" Seat already booked. Choose another.")
                return
            chosen_seats.append(seat)
            self.booked_seats.append(seat)
        total_cost = tickets * ticket_price
        print("\n Booking Confirmed ")
        print(f"Movie: {selected_movie}")
        print(f"Tickets: {tickets}")
        print(f"Seats: {', '.join(chosen_seats)}")
        print(f"Price per ticket: ₹{ticket_price}")
        print(f"Total Amount: ₹{total_cost}")
        print("Enjoy your movie! ")

booking_system = MovieTicketBooking()
booking_system.book_ticket()