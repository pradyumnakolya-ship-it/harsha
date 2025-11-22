# Smart university ERP Portal
#Combines Academics, fees, hostel, and library systems

# create a class for each module of the ERP system

#-------- Academics module-----

class Academics:
    def _init_(self):
        self.marks = {}

    def add_marks(self):
        name = input("Enter student name: ")
        marks = int(input("Enter total marks (out of 100): "))
        self.marks[name] = marks
        print(f"{marks} Marks added for {name}!")

    def view_marks(self):
        if not self.marks:
            print(" No records found.")
        else:
            print("Academic Records")

            for name,marks in self.marks.items():
                print(f"{name}: {marks}")


# ------- Fees modules------
class Fees:
    def _init_(self):
        self.fees = {}

    def pay_fee(self):
        name = input("Enter student name: ")
        amount = int(input("Enter amount paid Rs:- "))
        self.fees[name] = amount
        print(f"fee payment recorded for {name} (₹{amount})")

    def view_fees(self):
        if not self.fees:
            print("No fee records available")
        else:
            print("\n --- Fee Records ----")
            for name,amount in self.fees.items():
                print(f"{name}: ₹{amount}")

# --------- Hostel Module -------

class Hostel:
    def _init_(self):
        self.hostel_data = {}

    def allot_room(self):
        name = input("Enter student name: ")
        room = int(input("Enter room number: "))
        self.hostel_data[name] = room
        print(f"Room {room} alloted to {name}")

    def view_hostel(self):
        if not self.hostel_data:
            print(f"No hostel records found.")
        else:
            print("\n ---- Hostel Allotments----")
            for name,room in self.hostel_data.items():
                print(f"{name}: Room {room}")

#------ Library module-------

class Library:
    def _init_(self):
        self.library_data = {}

    def issue_book(self):
        name = input("Enter student name: ")
        book = input("Enter book title: ")
        self.library_data[name] = book
        print(f"Book '{book}' issued to {name}")

    def view_books(self):
        if not self.library_data:
            print("No library records found.")
        else:
            print("\n---Library records---")
            for name,book in self.library_data.items():
                print(f"{name}: {book}")

#----- Main ERP Portal ------
class UniversityERP:
    def _init_(self):
        # Create objects for all modules
        self.academics = Academics()
        self.fees = Fees()
        self.hostel = Hostel()
        self.library = Library()

    def main_menu(self):
        while True:
            print("\n ======= SMART UNIVERSITY ERP PORTAL =======")
            print("1. Academics")
            print("2. Fees")
            print("3. Hostel")
            print("4. Library")
            print("5. Exit")
            choice = input("Enter your choice (1 to 5): ")

            if choice == '1':
                self.academics_menu()
            elif choice== '2':
                self.fees_menu()
            elif choice == '3':
                self.hostel_menu()
            elif choice == '4':
                self.library_menu()
            elif choice == '5':
                print(" Thank you for using Smart university ERP!")
                break
            else:
                print(" Invalid choice. Try again.")

# --- Sub-menus for each module ---
    def academics_menu(self):
        print("\n--- Academics Menu ---")
        print("1. Add Marks")
        print("2. view marks")
        choice = input("Enter choice: ")
        if choice == '1':
            self.academics.add_marks()
        elif choice == '2':
            self.academics.view_marks()

    def fees_menu(self):
        print("\n---- Fees Menu ----")
        print("1. Pay Fee")
        print("2. View Fees")
        choice = input("Enter choice: ")
        if choice == '1':
            self.fees.pay_fee()
        elif choice == '2':
            self.fees.view_fees()

    def hostel_menu(self):
        print("\n --- Hostel Menu ---")
        print("1. Allot Room")
        print("2. View Allotments")
        choice = input("Enter choice: ")
        if choice == '1':
            self.hostel.allot_room()
        elif choice == '2':
            self.hostel.view_hostel()


    def library_menu(self):
        print("\n--- Library menu---")
        print("1. Issue Book ")
        print("2. View Issued books")
        choice = input("Enter choice: ")
        if choice == '1':
            self.library.issue_book()
        elif choice == '2':
            self.library.view_books()

# ------- Run the ERP Portal --------
if _name_ == "_main_":
    system = UniversityERP()
    system.main_menu()