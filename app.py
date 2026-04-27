import streamlit as st

st.title("ATM Simulator")

balance = 1000

option = st.selectbox("Choose Action", ["Check Balance", "Deposit", "Withdraw"])

if option == "Check Balance":
    st.write("Balance:", balance)

elif option == "Deposit":
    amt = st.number_input("Enter amount")
    if st.button("Deposit"):
        balance += amt
        st.success(f"New Balance: {balance}")

elif option == "Withdraw":
    amt = st.number_input("Enter amount")
    if st.button("Withdraw"):
        if amt <= balance:
            balance -= amt
            st.success(f"New Balance: {balance}")
        else:
            st.error("Insufficient Balance")