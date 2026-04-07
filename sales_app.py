import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Summary Dashboard")
st.subheader("Interactive app to filter and visualize sales data by category")

# Create hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Watch", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Footwear", "Accessories", "Electronics"],
    "Sales": [50000, 2000, 30000, 4000, 7000, 25000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter dataframe
filtered_df = df[df["Category"] == category]

# Display filtered data
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# Line chart
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])