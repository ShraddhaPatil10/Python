class Train:
    def __init__(self, total_seats):
        self.no_of_seats = total_seats
        self.name = ""
        self.salary = 0

    def book_ticket(self):
        if self.no_of_seats > 0:
            print("Enter your name:")
            self.name = input()

            print("Enter payment amount:")
            self.salary = int(input())

            print("Ticket booked successfully for", self.name)
            self.no_of_seats -= 1
        else:
            print("Ooops, train is full now!!!")

    def get_status_info(self):
        print("No of seats available:", self.no_of_seats)

    def fare_info(self):
        print("Price of Pune to Chennai: $5000")
        print("Price of Mumbai to Chennai: $4000")

def main():
    print("WELCOME TO CHENNAI EXPRESS BOOKING")

    total_seats = 10
    train_obj = Train(total_seats)

    while True:
        print("\nEnter your choice:")
        print("1. Book ticket\n2. Get Status info\n3. Fare Information\n4. Exit")
        choice = int(input())

        if choice == 1:
            train_obj.book_ticket()
        elif choice == 2:
            train_obj.get_status_info()
        elif choice == 3:
            train_obj.fare_info()
        elif choice == 4 or train_obj.no_of_seats < 1:
            print("Thank you for using Chennai Express Booking!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
