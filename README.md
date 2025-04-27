# 📊 Amazon Products Data Analysis 
![Amazon Sales Dataset EDA.jpg](https://user-images.githubusercontent.com/109474596/204128780-5a28ed57-53f6-4cf7-8d22-c8b8598138a1.png)
Welcome to our Amazon Products Data Analysis project!  
In this project, we dive deep into an Amazon products dataset to explore **pricing strategies**, **discount impacts**, **customer ratings**, and **review patterns**.  
Using **Python**, **Pandas**, **Seaborn**, **Matplotlib**, and **Streamlit**, we transformed raw data into actionable insights and built an **interactive dashboard** to visualize the findings.

---

##  What We Did
- Loaded and cleaned the Amazon product dataset.
- Handled missing or incorrect data types.
- Conducted **price analysis**, **discount analysis**, and **rating review analysis**.
- Detected **outliers** and **anomalies** in product performance.
- Created **interactive dashboards** using Streamlit to display KPIs and visualizations.
--- 
## 📊 Amazon Sales Dashboard

This interactive **Streamlit dashboard** allows you to explore and analyze Amazon products data, focusing on key metrics such as pricing, discounts, ratings, and user reviews. The dashboard offers several interactive filters to explore different product categories, price ranges, and rating criteria.

### Key Features:
- **KPI Metrics:** View total products, average ratings, total discounts, and total revenue.
- **Product Distribution:** Visualize product distribution by discount percentage.
- **User Reviews:** See a distribution of top users by reviews with a pie chart.
- **Price vs Rating:** Explore the relationship between discounted price and product ratings.
- **Top Products by Rating:** View the top 10 products with the highest average ratings.

The dashboard is designed to help businesses and analysts understand product performance, identify trends, and make data-driven decisions.

### How to Use:
- **Select Filters:** Choose product category, price range, and rating range from the sidebar.
- **Explore KPIs and Charts:** View key performance indicators and visual charts based on your selected filters.
- **Data Preview:** Access a table showing the filtered data for detailed insights.

Run the dashboard with the following command:
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


