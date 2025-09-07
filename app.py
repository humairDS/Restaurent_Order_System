import streamlit as st

# Menu stored in dictionary
Menu = {
    'Broast': 150,
    'Burger': 120,
    'Sandwich': 100,
    'Pizza': 200,
    'Pasta': 130,
    'Roll': 70,
    'Zinger': 180,
}

# Title and description
st.title("🍔 Umair's Fast Foods")
st.write("Welcome to Umair's Fast Foods! Please select your order from the menu below:")

# Store order details
order_items = []
order_total = 0

# Show menu with checkboxes
for food, price in Menu.items():
    if st.checkbox(f"{food} - Rs{price}"):
        order_items.append(food)
        order_total += price

# Show order summary
if order_items:
    st.subheader("🧾 Your Order:")
    st.write(", ".join(order_items))
    st.subheader(f"💰 Total Bill: Rs {order_total}")
else:
    st.info("Please select at least one food item to order.")
