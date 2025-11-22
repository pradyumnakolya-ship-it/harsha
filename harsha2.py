import streamlit as st
import pandas as pd
import os

# Utility functions for persistence
def load_data(filename, columns):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=columns)

def save_data(filename, df):
    df.to_csv(filename, index=False)

# ------- Academics Module ------
class Academics:
    def __init__(self):
        self.filename = "academics.csv"
        self.data = load_data(self.filename, ["Name", "Marks"])

    def add_marks(self, name, marks):
        new_row = pd.DataFrame([[name, marks]], columns=["Name", "Marks"])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        save_data(self.filename, self.data)
        st.success(f"{marks} Marks added for {name}!")

    def view_marks(self):
        if self.data.empty:
            st.warning("No academic records found.")
        else:
            st.subheader("📘 Academic Records")
            st.dataframe(self.data)


# ------- Fees Module ------
class Fees:
    def __init__(self):
        self.filename = "fees.csv"
        self.data = load_data(self.filename, ["Name", "Amount"])

    def pay_fee(self, name, amount):
        new_row = pd.DataFrame([[name, amount]], columns=["Name", "Amount"])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        save_data(self.filename, self.data)
        st.success(f"Fee payment recorded for {name} (₹{amount})")

    def view_fees(self):
        if self.data.empty:
            st.warning("No fee records available.")
        else:
            st.subheader("💰 Fee Records")
            st.dataframe(self.data)


# --------- Hostel Module -------
class Hostel:
    def __init__(self):
        self.filename = "hostel.csv"
        self.data = load_data(self.filename, ["Name", "Room"])

    def allot_room(self, name, room):
        new_row = pd.DataFrame([[name, room]], columns=["Name", "Room"])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        save_data(self.filename, self.data)
        st.success(f"Room {room} allotted to {name}")

    def view_hostel(self):
        if self.data.empty:
            st.warning("No hostel records found.")
        else:
            st.subheader("🏠 Hostel Allotments")
            st.dataframe(self.data)


# ------ Library Module -------
class Library:
    def __init__(self):
        self.filename = "library.csv"
        self.data = load_data(self.filename, ["Name", "Book"])

    def issue_book(self, name, book):
        new_row = pd.DataFrame([[name, book]], columns=["Name", "Book"])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        save_data(self.filename, self.data)
        st.success(f"Book '{book}' issued to {name}")

    def view_books(self):
        if self.data.empty:
            st.warning("No library records found.")
        else:
            st.subheader("📚 Library Records")
            st.dataframe(self.data)


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
