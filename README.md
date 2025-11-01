# E-Commerce Data Analytics

## Project Overview

This is a comprehensive end to end e-commerce analytics project that demonstrates the complete data analytics workflow. The project involves generating synthetic sales data using Python, designing a structured data model, creating interactive visualizations in Power BI, and delivering actionable business insights through dashboards and reports.

## Project Structure

The repository contains the following key files:

**main.py**
This is the Python script responsible for data generation and preprocessing. It creates synthetic e-commerce data that mimics real-world business operations.

**schema.md**
Complete documentation of the database structure. This file provides detailed information about all tables including Retail, Manufacturing, and Logistics schemas.

**dashboard.pdf**
An exported version of the Power BI dashboard report in PDF format. This allows stakeholders to view the insights without requiring Power BI Desktop.

**README.md**
Project overview and usage instructions that guide users through understanding and implementing the project.

## Dataset Description

The project includes a comprehensive dataset that covers multiple aspects of e-commerce operations:

**Customers Table**
Contains customer information including unique customer IDs, customer names, customer segments for targeted analysis, and signup information to track customer acquisition over time.

**Orders Table**
Includes order dates for temporal analysis, payment information and methods, delivery status tracking, and order amounts for revenue calculations.

**Products Table**
Features product categories for high-level grouping, product subcategories for detailed classification, brand information, and pricing data for profitability analysis.

**Logistics Table**
Covers warehouse information and locations, shipment tracking details, and returns management data.

**Finance Table**
Tracks revenue metrics, profit calculations, and key performance indicators for financial health monitoring.

The complete schema with detailed field descriptions and relationships is documented in the schema.md file.

## Key Features

**Synthetic Data Generation**
The entire dataset is generated using Python with libraries including Pandas for data manipulation and Faker for creating realistic synthetic data. This approach ensures privacy while maintaining data realism.

**Interactive Dashboards**
Key performance indicators are tracked and visualized in Power BI. The dashboards utilize DAX measures for advanced calculations and dynamic metrics.

**Key Metrics Analyzed**
The project tracks several critical business metrics including revenue growth over time, profit margins across products and categories, Average Order Value (AOV) to understand customer spending patterns, Customer Lifetime Value (CLTV) for identifying high-value customers, and return and cancellation rates to monitor customer satisfaction and operational efficiency.

**Business Insights**
The analytics provide insights across multiple business dimensions including sales trends and patterns, customer behavior and segmentation, logistics performance and efficiency, and workforce productivity metrics.

**Deliverables**
The project delivers an interactive dashboard in Power BI format (.pbix file) that allows users to explore data dynamically, plus a PDF export (dashboard.pdf) suitable for presentations and reporting to stakeholders.

## How to Use

**Step 1: Generate the Dataset**
Run the main.py Python script to generate the synthetic dataset. This script will create all necessary data files that simulate e-commerce operations.

**Step 2: View the Dashboard**
Load the .pbix file in Power BI Desktop to access and interact with the dashboards. You can filter, drill down, and explore various metrics and dimensions.

**Step 3: Export Reports**
The dashboard can be exported to PDF format (dashboard.pdf) for sharing with stakeholders who do not have Power BI Desktop installed.

## Business Questions Answered

This analytics project addresses several critical business questions:

**Revenue Analysis**
How is revenue growing on a monthly and yearly basis? What are the trends and seasonality patterns in sales?

**Profitability Assessment**
Which products and product categories contribute the most to overall profit? Where should the business focus its resources?

**Customer Value Analysis**
Who are the high-value customers based on Customer Lifetime Value (CLTV) and Average Order Value (AOV)? How can the business retain and grow these customer segments?

**Operational Efficiency**
What are the patterns in product returns and order cancellations? Are there specific products or categories with higher return rates?

**Logistics and Workforce Performance**
How efficient are the logistics operations including warehousing and shipment? What is the workforce productivity across different operational areas?

## Technologies Used

- Python (Pandas, Faker) for synthetic data generation
- Power BI Desktop for data modeling and visualization
- DAX (Data Analysis Expressions) for calculated measures and KPIs
- SQL-style data modeling for relational database design

## Project Value

This project demonstrates proficiency in the complete data analytics pipeline from data generation and cleaning through modeling, visualization, and insight delivery. It showcases practical skills in business intelligence, data storytelling, and translating data into actionable business recommendations.
