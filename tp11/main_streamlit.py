import streamlit as st
from CustomerDAO import CustomerDAO

def main():
    st.write("# Hello")
    
    name = st.text_input("Name ?", "")

    if st.button("Say hello"):
        st.write(f"bonjour {name}")
    
    dao =CustomerDAO("../customers_db.db")
    customers = dao.findAll()

    st.table(customers)

# streamlit run main_streamlit.py

if __name__=='__main__':
    main()
