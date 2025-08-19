# E-Commerce Data Analytics & Reporting

## Overview

This project simulates and analyzes e-commerce sales data end-to-end. You generate realistic data with Python, transform it, visualize key metrics in Power BI, and share insights via interactive dashboards and a final PDF report.

## About the Data

You create a synthetic e-commerce dataset with columns like:

* **Customer Info** (e.g., customer ID, name, segment)
* **Order Details** (order ID, date, order value)
* **Product Data** (product ID, category, price)
* **Logistics & Returns** (warehouse, shipping mode, return flag)
* **Financial Metrics** (revenue, profit margin)

## Features

* **Data Generation & Preprocessing**
  Simulate and clean an e-commerce dataset using Python tools like Pandas and Faker.

* **KPI Tracking via Power BI**
  Build an interactive dashboard with calculated fields and DAX measures to monitor:

  * Revenue growth
  * Profit margins
  * Average Order Value (AOV)
  * Customer Lifetime Value (CLTV)
  * Return and cancellation rates

* **Business Insights & Reports**
  Uncover trends in customer behavior, product performance, logistics, and workforce efficiency. Export everything into clean, presentation-ready PDF reports.

## Prerequisites

* **Python** (with Pandas, Faker installed)
* **Power BI Desktop** (for building dashboards)
* **PDF export capability** (built into Power BI)

## Usage Instructions

1. **Generate & Clean Dataset**
   Run `main.py` to create and preprocess your e-commerce dataset.

2. **Open Power BI Dashboard**
   Load the `.pbix` file in Power BI Desktop to explore interactive visuals.

3. **Export Report**
   Once you're happy with the dashboard, export it as a PDF and share it with stakeholders.

## Key Business Questions Answered

* What’s the trend in monthly and yearly revenue?
* Which products and categories drive the most profit?
* Who are high-value customers based on CLTV and AOV?
* What are the peak return or cancellation patterns?
* How efficient are logistics and workforce operations?
