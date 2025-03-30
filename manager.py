import streamlit as st
import pandas as pd

# Initialize session state for books
if 'books' not in st.session_state:
    st.session_state.books = []

def add_book(title, author, year):
    st.session_state.books.append({"Title": title, "Author": author, "Year": year})

def remove_book(index):
    if 0 <= index < len(st.session_state.books):
        st.session_state.books.pop(index)

st.title("Library Manager By Hunain Shah")

# Book Input Form
with st.form("book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=9999, step=1, value=2024)
    submit = st.form_submit_button("Add Book")
    
    if submit and title and author:
        add_book(title, author, year)
        st.success(f"Added '{title}' by {author} ({year})")

# Display Books
if st.session_state.books:
    st.subheader("Library Collection")
    df = pd.DataFrame(st.session_state.books)
    st.dataframe(df)
    
    # Remove book option
    remove_index = st.number_input("Enter index to remove", min_value=0, max_value=len(st.session_state.books)-1, step=1)
    if st.button("Remove Book"):
        remove_book(remove_index)
        st.success("Book removed successfully!")
else:
    st.write("No books in the library yet.")
