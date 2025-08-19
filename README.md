# E-Commerce Data Analytics

## Overview  
An end-to-end e-commerce analytics project: generate synthetic sales data with Python, model and visualize in Power BI, and deliver business insights via dashboards and reports.  

## Repository Contents  
- `main.py` → Python script for data generation & preprocessing  
- `schema.md` → Documentation of database tables (Retail, Manufacturing, Logistics)  
- `dashboard.pdf` → Exported Power BI dashboard report  
- `README.md` → Project overview & usage instructions  

## Data & Schema  
The dataset includes:  
- **Customers** → IDs, names, segments, signup info  
- **Orders** → Dates, payments, delivery status, amounts  
- **Products** → Categories, subcategories, brands, pricing  
- **Logistics** → Warehouses, shipments, returns  
- **Finance** → Revenue, profit, and KPIs  

➡ Full schema is documented in [`schema.md`](./schema.md).  

## Features  
- **Synthetic Data Generation** → Created with Python (Pandas, Faker).  
- **Interactive Dashboards** → KPIs tracked in Power BI with DAX measures.  
- **Key Metrics** → Revenue growth, profit margins, AOV, CLTV, return/cancel rates.  
- **Business Insights** → Sales trends, customer behavior, logistics performance, workforce efficiency.  
- **Deliverables** → Interactive dashboard (`.pbix`) + PDF report.  

## Usage Instructions  
1. Run `main.py` to generate the dataset.  
2. Load the `.pbix` file in Power BI Desktop to view dashboards.  
3. Export to PDF (`dashboard.pdf`) for reporting.  

## Key Business Questions  
- How is revenue growing monthly and yearly?  
- Which products/categories contribute the most profit?  
- Who are the high-value customers (CLTV, AOV)?  
- What are the patterns in returns and cancellations?  
- How efficient are logistics and workforce operations?  
