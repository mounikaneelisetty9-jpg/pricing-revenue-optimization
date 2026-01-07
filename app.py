# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pricing & Revenue Optimization", layout="centered")
st.title("💰 Pricing & Revenue Optimization - Multi Product")
st.write("Simulate pricing strategies and see revenue effects for multiple products.")

# --- Inputs ---
st.sidebar.header("Products")
num_products = st.sidebar.number_input("Number of products", min_value=1, max_value=5, value=2, step=1)

products = []
for i in range(num_products):
    st.sidebar.subheader(f"Product {i+1}")
    name = st.sidebar.text_input(f"Name", value=f"Product {i+1}", key=f"name{i}")
    a = st.sidebar.number_input(f"Max demand (a)", value=100, key=f"a{i}")
    b = st.sidebar.number_input(f"Demand slope (b)", value=2, key=f"b{i}")
    price = st.sidebar.slider(f"Price", min_value=0.0, max_value=100.0, step=0.5, key=f"price{i}")
    products.append({"name": name, "a": a, "b": b, "price": price})

# --- Calculate revenues ---
st.subheader("Product Revenue")
total_revenue = 0
revenue_data = []

for p in products:
    quantity = max(p['a'] - p['b']*p['price'], 0)
    revenue = p['price'] * quantity
    total_revenue += revenue
    optimal_price = p['a'] / (2*p['b'])
    optimal_revenue = optimal_price * (p['a'] - p['b']*optimal_price)
    
    st.write(f"**{p['name']}**")
    st.write(f"Quantity demanded: {quantity:.2f}")
    st.write(f"Revenue: ${revenue:.2f}")
    st.write(f"Optimal price: ${optimal_price:.2f}, Max revenue: ${optimal_revenue:.2f}")
    
    # Store data for table
    revenue_data.append({
        "Product": p['name'],
        "Selected Price": p['price'],
        "Quantity": quantity,
        "Revenue": revenue,
        "Optimal Price": optimal_price,
        "Max Revenue": optimal_revenue
    })

# --- Show table ---
df = pd.DataFrame(revenue_data)
st.subheader("Summary Table")
st.dataframe(df)

st.subheader("Total Revenue")
st.write(f"💰 Total Revenue for all products: ${total_revenue:.2f}")

# --- Plot revenue curves ---
st.subheader("Revenue Curves")
plt.figure(figsize=(8,5))
for p in products:
    prices = np.linspace(0, p['a']/p['b']*1.2, 100)
    revenues = prices * (p['a'] - p['b']*prices)
    plt.plot(prices, revenues, label=p['name'])
    # highlight selected price
    selected_quantity = max(p['a'] - p['b']*p['price'],0)
    selected_revenue = p['price']*selected_quantity
    plt.scatter(p['price'], selected_revenue, color='red')
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Revenue vs Price for Multiple Products")
plt.legend()
plt.grid(True)
st.pyplot(plt)
