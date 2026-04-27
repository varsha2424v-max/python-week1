import streamlit as st

# balance ko memory me store karo
if "balance" not in st.session_state:
    st.session_state.balance = 1000

st.title("ATM Simulator")

option = st.selectbox("Choose Action", ["Check Balance", "Deposit", "Withdraw"])

# CHECK BALANCE
if option == "Check Balance":
    st.write("Balance:", st.session_state.balance)

# DEPOSIT
elif option == "Deposit":
    amt = st.number_input("Enter amount", min_value=0)
    if st.button("Deposit"):
        st.session_state.balance += amt
        st.success(f"Deposited! New Balance: {st.session_state.balance}")

# WITHDRAW
elif option == "Withdraw":
    amt = st.number_input("Enter amount", min_value=0)
    if st.button("Withdraw"):
        if amt <= st.session_state.balance:
            st.session_state.balance -= amt
            st.success(f"Withdrawn! New Balance: {st.session_state.balance}")
        else:
            st.error("Insufficient Balance")