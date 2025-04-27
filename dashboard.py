import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Basmala\OneDrive\Desktop\Amason\Data\cleaned_data.csv")
    return df

df = load_data()

# --- Preprocessing ---
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
categories = df['category'].dropna().unique()
selected_category = st.sidebar.selectbox('Select Product Category', categories)

# Filtering by price range
price_range = st.sidebar.slider("Select Price Range", min_value=int(df['discounted_price'].min()), 
                                max_value=int(df['discounted_price'].max()), 
                                value=(int(df['discounted_price'].min()), int(df['discounted_price'].max())))

# Filtering by rating
rating_range = st.sidebar.slider("Select Rating Range", min_value=0, max_value=5, value=(0, 5))

# Filtering data
filtered_df = df[(df['category'] == selected_category) & 
                 (df['discounted_price'] >= price_range[0]) & 
                 (df['discounted_price'] <= price_range[1]) & 
                 (df['rating'] >= rating_range[0]) & 
                 (df['rating'] <= rating_range[1])]

# --- Main Title ---
st.title("🛒 Amazon Sales Dashboard")

# --- KPIs Section ---
st.markdown("## 📊 Overview Metrics")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_products = len(filtered_df)
average_rating = round(filtered_df['rating'].mean(), 2)
total_discount = filtered_df['discount_percentage'].sum()  
revenue = (filtered_df['discounted_price'] * total_products).sum()  

kpi1.metric("Total Products", total_products, delta_color="normal")
kpi2.metric("Average Rating", average_rating, delta_color="normal")
kpi3.metric("Total Discounts", total_discount, delta_color="normal")
kpi4.metric("Total Revenue", f"${revenue:,.2f}", delta_color="normal")

# --- Charts Section ---
st.markdown("---")
chart1, chart2 = st.columns((2, 1))

# 1. Product Distribution by Discount Percentage
with chart1:
    st.subheader("Product Distribution by Discount Percentage")
    discount_distribution = filtered_df['discount_percentage'].value_counts().sort_index()
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=discount_distribution.index, y=discount_distribution.values, palette='viridis', ax=ax1)
    ax1.set_xlabel("Discount Percentage")
    ax1.set_ylabel("Number of Products")
    st.pyplot(fig1)

# 2. User Reviews Distribution (Pie Chart)
with chart2:
    st.subheader("User Reviews Distribution")
    user_reviews = filtered_df['user_name'].value_counts().head(10)  # Top 10 users by number of reviews
    fig2, ax2 = plt.subplots()
    ax2.pie(user_reviews, labels=user_reviews.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    ax2.axis('equal')
    st.pyplot(fig2)

# --- More Detailed Charts ---
st.markdown("---")
chart3, chart4 = st.columns(2)

with chart3:
    st.subheader("Price vs Rating")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=filtered_df, x='discounted_price', y='rating', hue='rating', palette='coolwarm', edgecolor='black', ax=ax3)
    ax3.set_xlabel("Discounted Price")
    ax3.set_ylabel("Rating")
    st.pyplot(fig3)

with chart4:
    st.subheader("Average Rating per Product (Top 10)")
    top_avg = filtered_df.groupby('product_name')['rating'].mean().sort_values(ascending=False).head(10)
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=top_avg.values, y=top_avg.index, palette='Blues_r', ax=ax4)
    ax4.set_xlabel("Average Rating")
    ax4.set_ylabel("Product")
    st.pyplot(fig4)

# --- Full Data Table ---
st.markdown("---")
st.subheader("🗂 Full Data Preview")
st.dataframe(filtered_df, use_container_width=True)

# --- Aesthetic Improvements ---
st.markdown("""
    <style>
    .stMetric {
        font-size: 20px !important;
        background-color: #f0f0f5;
        border-radius: 8px;
        padding: 10px;
    }
    .css-1d391kg {
        font-size: 18px;
        background-color: #f9f9f9;
    }
    .css-1v0mbdj p {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)