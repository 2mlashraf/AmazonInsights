import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Basmala\OneDrive\Desktop\Amason\Data\cleaned_data_no_outliers.csv")
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

# Limit to first 20 products in the selected category
filtered_df = filtered_df.head(20)

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
    ax1.grid(True, linestyle='--', alpha=0.5)  # Add gridlines for better visualization
    st.pyplot(fig1)

# 2. Product Distribution by Rating (Pie Chart)
with chart2:
    st.subheader("Product Distribution by Rating")
    rating_distribution = filtered_df['rating'].value_counts().sort_index()  # Distribution based on product ratings
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax2.pie(rating_distribution, 
                                        labels=rating_distribution.index, 
                                        autopct='%1.1f%%', 
                                        startangle=90, 
                                        colors=sns.color_palette("Blues", len(rating_distribution)), 
                                        wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': 'solid'},
                                        textprops={'color': 'black', 'fontsize': 12, 'fontweight': 'bold'})
    
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)

# --- Additional Charts for Aesthetics & Insights ---
st.markdown("---")
chart3, chart4 = st.columns(2)

# 1. Heatmap showing the relationship between price and rating
with chart3:
    st.subheader("Heatmap: Price vs Rating")
    correlation_matrix = filtered_df[['discounted_price', 'rating']].corr()
    fig5, ax5 = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, ax=ax5)
    ax5.set_title("Correlation Heatmap between Price and Rating")
    st.pyplot(fig5)

# 2. Boxplot to examine price distribution and ratings
with chart4:
    st.subheader("Boxplot: Price and Rating Distribution")
    fig6, ax6 = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=filtered_df[['discounted_price', 'rating']], ax=ax6, palette="Set2")
    ax6.set_title('Price vs Rating Distribution')
    ax6.set_xlabel('Price / Rating')
    ax6.set_ylabel('Value')
    ax6.grid(True, linestyle='--', alpha=0.5)  # Add gridlines for better visualization
    st.pyplot(fig6)

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
