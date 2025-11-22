import streamlit as st

# ------- Academics Module ------
class Academics:
    def __init__(self):
        self.marks = {}

    def add_marks(self, name, marks):
        self.marks[name] = marks
        st.success(f"{marks} Marks added for {name}!")

    def view_marks(self):
        if not self.marks:
            st.warning("No academic records found.")
        else:
            st.subheader("📘 Academic Records")
            for name, marks in self.marks.items():
                st.write(f"{name}: {marks}")


# ------- Fees Module ------
class Fees:
    def __init__(self):
        self.fees = {}

    def pay_fee(self, name, amount):
        self.fees[name] = amount
        st.success(f"Fee payment recorded for {name} (₹{amount})")

    def view_fees(self):
        if not self.fees:
            st.warning("No fee records available.")
        else:
            st.subheader("💰 Fee Records")
            for name, amount in self.fees.items():
                st.write(f"{name}: ₹{amount}")


# --------- Hostel Module -------
class Hostel:
    def __init__(self):
        self.hostel_data = {}

    def allot_room(self, name, room):
        self.hostel_data[name] = room
        st.success(f"Room {room} allotted to {name}")

    def view_hostel(self):
        if not self.hostel_data:
            st.warning("No hostel records found.")
        else:
            st.subheader("🏠 Hostel Allotments")
            for name, room in self.hostel_data.items():
                st.write(f"{name}: Room {room}")


# ------ Library Module -------
class Library:
    def __init__(self):
        self.library_data = {}

    def issue_book(self, name, book):
        self.library_data[name] = book
        st.success(f"Book '{book}' issued to {name}")

    def view_books(self):
        if not self.library_data:
            st.warning("No library records found.")
        else:
            st.subheader("📚 Library Records")
            for name, book in self.library_data.items():
                st.write(f"{name}: {book}")


# ----- Main ERP Portal ------
class UniversityERP:
    def __init__(self):
        self.academics = Academics()
        self.fees = Fees()
        self.hostel = Hostel()
        self.library = Library()

    def run(self):
        st.title("🎓 Smart University ERP Portal")

        menu = st.sidebar.radio(
            "Choose Module",
            ["Academics", "Fees", "Hostel", "Library"]
        )

        if menu == "Academics":
            st.header("📘 Academics Module")
            choice = st.radio("Select Action", ["Add Marks", "View Marks"])
            if choice == "Add Marks":
                name = st.text_input("Enter student name")
                marks = st.number_input("Enter marks (out of 100)", 0, 100)
                if st.button("Add"):
                    self.academics.add_marks(name, marks)
            elif choice == "View Marks":
                self.academics.view_marks()

        elif menu == "Fees":
            st.header("💰 Fees Module")
            choice = st.radio("Select Action", ["Pay Fee", "View Fees"])
            if choice == "Pay Fee":
                name = st.text_input("Enter student name")
                amount = st.number_input("Enter amount paid (₹)", 0)
                if st.button("Pay"):
                    self.fees.pay_fee(name, amount)
            elif choice == "View Fees":
                self.fees.view_fees()

        elif menu == "Hostel":
            st.header("🏠 Hostel Module")
            choice = st.radio("Select Action", ["Allot Room", "View Allotments"])
            if choice == "Allot Room":
                name = st.text_input("Enter student name")
                room = st.number_input("Enter room number", 1)
                if st.button("Allot"):
                    self.hostel.allot_room(name, room)
            elif choice == "View Allotments":
                self.hostel.view_hostel()

        elif menu == "Library":
            st.header("📚 Library Module")
            choice = st.radio("Select Action", ["Issue Book", "View Issued Books"])
            if choice == "Issue Book":
                name = st.text_input("Enter student name")
                book = st.text_input("Enter book title")
                if st.button("Issue"):
                    self.library.issue_book(name, book)
            elif choice == "View Issued Books":
                self.library.view_books()


# ------- Run the ERP Portal --------
if __name__ == "__main__":
    system = UniversityERP()
    system.run()
