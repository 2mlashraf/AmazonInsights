# 📊 Amazon Products Data Analysis 
![Amazon Sales Dataset EDA.jpg](https://user-images.githubusercontent.com/109474596/204128780-5a28ed57-53f6-4cf7-8d22-c8b8598138a1.png)


## **Project Overview**
This project involves a comprehensive analysis of an Amazon products dataset, aimed at uncovering actionable insights related to **pricing strategies**, **discount effects**, **customer ratings**, and **review trends**. The analysis leverages the power of **Python**, **Pandas**, **Seaborn**, **Matplotlib**, and **Streamlit** to transform raw data into meaningful information. Additionally, an interactive dashboard has been developed to facilitate dynamic data exploration and visualization.

---

## **Project Objectives**
The primary objectives of this project are as follows:
- **Data Exploration**: Investigate pricing structures, discount patterns, customer reviews, and ratings across various product categories.
- **Data Cleaning**: Address missing data, data type inconsistencies, and ensure uniformity across the dataset.
- **Insight Extraction**: Derive actionable insights based on product performance, customer behavior, and trends in the dataset.
- **Data Visualization**: Utilize visualization techniques to present key findings clearly and concisely.
- **Interactive Dashboard**: Develop an interactive dashboard that allows users to explore the data and visualize key metrics.

---

## **Project Methodology**
1. **Data Loading & Cleaning**:
   - The dataset was loaded and cleaned by addressing missing values, ensuring correct data types, and standardizing column formats.
   
2. **Data Analysis**:
   - Conducted a detailed analysis of pricing, discount percentages, and ratings, identifying patterns and correlations.
   
3. **Outlier Detection**:
   - Identified outliers and anomalies in product performance, focusing on discrepancies between price, discount, and customer ratings.
   
4. **Interactive Dashboard**:
   - Developed an interactive dashboard using **Streamlit**, enabling dynamic filtering of product data and visual exploration of key performance indicators.

---

## 📊 **Amazon Sales Dashboard**

The **Streamlit-based dashboard** provides an interactive platform for analyzing and visualizing key product metrics. Users can explore a variety of filters, including product category, price range, and rating criteria. The dashboard allows for the investigation of key metrics such as pricing, discount percentages, product ratings, and review distribution.

### **Key Features**:
- **KPI Metrics**: View overall product count, average ratings, total discounts, and total revenue.
- **Product Distribution**: Visualize product distribution based on discount percentages.
- **User Reviews**: Display the distribution of top users by reviews through pie charts and other visualizations.
- **Price vs Rating**: Examine the relationship between price, discount percentage, and product ratings.
- **Top Rated Products**: Identify the top 10 products with the highest average ratings.

### **Usage Instructions**:
1. **Select Filters**: Choose product categories, price ranges, and rating ranges from the sidebar.
2. **Explore KPIs & Visualizations**: View key performance indicators and visualizations that update based on the selected filters.
3. **Access Data Preview**: View a detailed table of the filtered data for further insights.

To run the dashboard, use the following command:
```bash
streamlit run dashboard.py
```
##  Summary of Findings

### 1.  Price Analysis
- Products show a wide price range from **₹389** to **₹19,125**.
- Significant discounts available on several products, up to **65% off**.

### 2.  Discounts
- Discounts range between **46%** and **70%**.
- Heavily discounted products may drive higher sales volume.

### 3.  Ratings and Reviews
- Ratings vary between **3.4** and **4.5** stars.
- Products with more reviews often had better average ratings.

### 4. Categories
- Most common categories: **Accessories & Peripherals**, **Televisions**.
- Dataset includes diverse product types from **Electronics** to **Home Theater**.

### 5. Outliers & Anomalies
- Identified high-priced, low-rated products that might need business review.
- Highlighted great-value products with low prices and high ratings.

### 6.  Product Descriptions & Reviews
- Positive reviews emphasize **value for money**.
- Negative comments reveal **areas for improvement** like **charging speeds**.

### 7.  Images and Links
- Each product had associated images and purchase links, crucial for marketing impact.
---
##  Key Insights
- **Higher ratings** and **more reviews** indicate better market reception.
- **Discounts alone** don't guarantee higher customer satisfaction — perceived **value matters more**.
- Businesses should **analyze outliers** (like expensive but poorly rated products) to adjust strategies.
- **Product Categories:** Products from categories with a higher number of positive reviews (e.g., **Accessories & Peripherals**) tend to perform better compared to categories with mixed feedback, such as **Home & Kitchen**. 
- **Customer Behavior:** A product with a significant discount doesn’t always guarantee a higher rating, suggesting that customers may still be dissatisfied with product quality, even if it is affordable.
- **Review Sentiment:** Both positive and negative reviews provide valuable insights. Positive feedback often mentions the product's reliability and value, while negative reviews indicate opportunities for improvement (e.g., performance issues, charging speeds, etc.).
---

## Challenges Faced
- **Data Cleaning:** One of the main challenges was dealing with missing or inconsistent data. We had to handle null values and ensure data types were consistent across columns (e.g., ensuring ratings were numerical).
  
- **Outliers Detection:** Identifying outliers required a balance between detecting genuinely poor-performing products and distinguishing them from those with genuine sales success but low ratings.
---
##  Technologies & Libraries Used
- **Python**
- **Pandas** (for data cleaning and manipulation)
- **Seaborn** (for data visualization)
- **Matplotlib** (for plotting graphs)
- **Streamlit** (for building an interactive dashboard)
----
## 👥 Contributors

- [Basmala Saeed](https://github.com/basmalaeltabakh) 
- [Aml Ashraf](https://github.com/2mlashraf) 
- [Fayrouz Abdelhalim](https://github.com/fayrouzabdelhalim) 


