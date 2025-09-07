import streamlit as st
import pandas as pd

# Menu (Dictionary)
Menu = {
    'Broast': 150,
    'Burger': 120,
    'Sandwich': 100,
    'Pizza': 200,
    'Pasta': 130,
    'Roll': 70,
    'Zinger': 180,
}

# App Title & Intro
st.title("🍔 Umair's Restaurant Ordering System")
st.write("Welcome! Please place your order from the sidebar menu.")

# Customer Info
customer_name = st.text_input("Enter your name:")

# Sidebar - Order Selection
st.sidebar.header("📋 Menu")

order = {}
for food, price in Menu.items():
    quantity = st.sidebar.number_input(
        f"{food} (Rs {price})", 
        min_value=0, 
        max_value=10, 
        step=1
    )
    if quantity > 0:
        order[food] = quantity

# Confirm Order Button
if st.button("✅ Confirm Order"):
    if not order:
        st.warning("Please select at least one item before confirming.")
    elif not customer_name:
        st.warning("Please enter your name before confirming.")
    else:
        # Build receipt DataFrame
        order_summary = []
        total = 0
        for item, qty in order.items():
            price = Menu[item]
            subtotal = qty * price
            total += subtotal
            order_summary.append([item, qty, price, subtotal])
        
        df = pd.DataFrame(order_summary, columns=["Item", "Quantity", "Price", "Subtotal"])

        st.success(f"Thank you {customer_name}! 🎉 Here’s your receipt:")
        st.table(df)
        st.subheader(f"💰 Total Bill: Rs {total}")
