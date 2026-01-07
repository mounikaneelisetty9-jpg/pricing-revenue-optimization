# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pricing & Revenue Optimization", layout="centered")
st.title("💰 Pricing & Revenue Optimization")
st.write("Explore how price affects demand and revenue for a simple product.")

# --- Inputs ---
st.sidebar.header("Model Parameters")
a = st.sidebar.number_input("Maximum demand (a)", value=100)
b = st.sidebar.number_input("Demand slope (b)", value=2)
price_slider = st.sidebar.slider("Select a price", min_value=0.0, max_value=100.0, step=0.5)

# --- Linear Demand Model ---
quantity = max(a - b * price_slider, 0)  # avoid negative demand
revenue = price_slider * quantity

st.subheader("Results at selected price")
st.write(f"📦 Quantity demanded: {quantity:.2f}")
st.write(f"💵 Revenue: ${revenue:.2f}")

# --- Revenue Curve ---
prices = np.linspace(0, a/b*1.2, 100)  # slightly past max demand
revenues = prices * (a - b*prices)

plt.figure(figsize=(6,4))
plt.plot(prices, revenues, label="Revenue Curve")
plt.scatter(price_slider, revenue, color='red', label="Selected Price")
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Revenue vs Price")
plt.legend()
plt.grid(True)
st.pyplot(plt)

# --- Optimal Price ---
optimal_price = a / (2*b)
optimal_revenue = optimal_price * (a - b*optimal_price)

st.subheader("Optimal Price")
st.write(f"💡 Price that maximizes revenue: ${optimal_price:.2f}")
st.write(f"Revenue at optimal price: ${optimal_revenue:.2f}")

st.info("This is a **basic linear demand model**. You can adjust 'a' and 'b' to see how demand and revenue change.")
