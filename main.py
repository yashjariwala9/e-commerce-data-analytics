import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker('en_IN')

PRODUCT_BRAND_MAPPING = {
    'Electronics': {'brands': ['Samsung', 'Apple', 'OnePlus', 'Xiaomi', 'Realme', 'Oppo', 'Vivo', 'Sony', 'LG', 'Panasonic', 'Boat', 'JBL', 'Dell', 'HP', 'Lenovo', 'Asus'], 'subcategories': ['Smartphones', 'Laptops', 'Tablets', 'Headphones', 'Cameras', 'TVs', 'Audio Systems', 'Smart Watches', 'Gaming Consoles', 'Accessories']},
    'Clothing & Fashion': {'brands': ['Zara', 'H&M', 'Uniqlo', 'Fabindia', 'W for Woman', 'Biba', 'Aurelia', 'Peter England', 'Van Heusen', 'Allen Solly', "Levi's", 'Pepe Jeans', 'Manyavar', 'Sabyasachi'], 'subcategories': ['Kurtas', 'Sarees', 'Jeans', 'T-Shirts', 'Formal Shirts', 'Dresses', 'Footwear', 'Accessories', 'Ethnic Wear', 'Western Wear']},
    'Home & Furniture': {'brands': ['IKEA', 'Godrej', 'Nilkamal', 'Durian', 'Urban Ladder', 'Pepperfry', 'HomeTown', 'Sleepwell', 'Kurlon', 'Wipro Furniture', 'Spacewood'], 'subcategories': ['Sofas', 'Beds', 'Dining Tables', 'Wardrobes', 'Kitchen Appliances', 'Home Decor', 'Mattresses', 'Lighting', 'Storage Solutions', 'Garden Furniture']},
    'Beauty & Personal Care': {'brands': ['Lakme', 'Maybelline', "L'Oreal", 'Nykaa', 'Mamaearth', 'Himalaya', 'Dabur', 'Patanjali', 'Nivea', 'Dove', 'Forest Essentials', 'Biotique'], 'subcategories': ['Skincare', 'Makeup', 'Hair Care', 'Fragrances', "Men's Grooming", 'Ayurvedic Products', 'Body Care', 'Nail Care', 'Tools & Accessories']},
    'Food & Beverages': {'brands': ['Amul', 'Britannia', 'Parle', 'ITC', 'Nestle', 'Coca-Cola', 'PepsiCo', "Haldiram's", 'MTR', 'Maggi', 'Tata Tea', 'Mother Dairy', 'Everest'], 'subcategories': ['Snacks', 'Beverages', 'Dairy Products', 'Ready-to-Eat', 'Spices & Condiments', 'Tea & Coffee', 'Sweets & Desserts', 'Health Foods', 'Organic Products']},
    'Books & Stationery': {'brands': ['Penguin', 'Oxford', 'Cambridge', 'Classmate', 'Reynolds', 'Camlin', 'Faber-Castell', 'Navneet', 'Apsara', 'Cello'], 'subcategories': ['Fiction', 'Non-Fiction', 'Educational', "Children's Books", 'Stationery', 'Art Supplies', 'Notebooks', 'Writing Instruments', 'Academic Books']},
    'Sports & Fitness': {'brands': ['Adidas', 'Nike', 'Puma', 'Reebok', 'Decathlon', 'Nivia', 'Cosco', 'Yonex', 'Li-Ning', 'Victor', 'Spalding'], 'subcategories': ['Cricket Equipment', 'Fitness Equipment', 'Athletic Wear', 'Outdoor Sports', 'Yoga & Wellness', 'Badminton', 'Football', 'Basketball', 'Swimming']},
    'Automotive': {'brands': ['Maruti Suzuki', 'Hyundai', 'Tata Motors', 'Mahindra', 'Hero', 'Bajaj', 'TVS', 'Bosch', 'MRF', 'Apollo Tyres', 'Castrol'], 'subcategories': ['Car Accessories', 'Bike Parts', 'Tyres', 'Engine Oil', 'Car Care Products', 'Interior Accessories', 'Safety Equipment', 'Performance Parts']},
    'Health & Wellness': {'brands': ['Dabur', 'Himalaya', 'Patanjali', 'Zandu', 'Revital', 'Centrum', 'Protinex', 'Complan', 'Horlicks', 'Baidyanath'], 'subcategories': ['Ayurvedic Medicine', 'Vitamins', 'Supplements', 'First Aid', 'Personal Hygiene', 'Health Drinks', 'Herbal Products', 'Medical Devices']},
    'Toys & Games': {'brands': ['Funskool', 'Mattel', 'Hasbro', 'Lego', 'Fisher-Price', 'Hot Wheels', 'Barbie', 'Nerf', 'Play-Doh'], 'subcategories': ['Educational Toys', 'Action Figures', 'Board Games', 'Dolls', 'Electronic Toys', 'Building Blocks', 'Puzzles', 'Outdoor Toys', 'Soft Toys']}
}

METRO_CITIES = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
TIER2_CITIES = ['Surat', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Patna', 'Bhopal', 'Ludhiana', 'Agra', 'Vadodara', 'Coimbatore', 'Kochi', 'Visakhapatnam', 'Madurai']
ALL_INDIAN_CITIES = METRO_CITIES + TIER2_CITIES
METRO_SET = set(METRO_CITIES)

REGIONS = ['North India', 'South India', 'West India', 'East India', 'Central India', 'Northeast India']
PAYMENT_METHODS = ['Cash', 'Credit Card', 'Debit Card', 'UPI']
PAYMENT_WEIGHTS = [0.2, 0.4, 0.3, 0.5]
ORDER_STATUSES = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Exchanged', 'Refunded']
ORDER_STATUS_WEIGHTS = [0.3, 0.3, 0.25, 0.1, 0.02, 0.02, 0.03]
CHANNELS = ['Online', 'In-Store', 'Mobile App']
RETURN_REASONS = ['Defective', 'Wrong Size', 'Not as Described', 'Changed Mind', 'Damaged in Shipping', 'Better Price Found', 'Quality Issues']
PRODUCT_STATUSES = ['Active', 'Discontinued', 'Out of Stock', 'Limited Stock']
STORE_TYPES = ['Flagship Store', 'Outlet', 'Online Only']
CUSTOMER_SEGMENTS = ['Regular', 'VIP', 'One-time']
STORAGE_TYPES = ['Cold Storage', 'Dry Storage', 'General']
STORAGE_WEIGHTS = [0.1, 0.3, 0.6]
MACHINE_TYPES = ['Textile Loom', 'CNC Machine', 'Injection Molding', 'Packaging Machine', 'Food Processing Unit', 'Assembly Line', 'Quality Control Station', 'Printing Press', 'Welding Station']
SHIFTS = ['Morning', 'Evening', 'Night', 'General']
ROLES = ['Operator', 'Technician', 'Supervisor', 'Quality Inspector', 'Maintenance', 'Floor Manager', 'Safety Officer', 'Driver', 'Warehouse Manager', 'Inventory Clerk', 'Sales Associate', 'HR Specialist', 'IT Support', 'Logistics Coordinator', 'Store Manager']
DEPARTMENTS = ['Manufacturing', 'Logistics', 'Sales', 'Human Resources', 'Information Technology', 'Inventory Management', 'Store Management']
SHIPMENT_STATUSES = ['Delivered', 'In Transit', 'Failed', 'Pending', 'Out for Delivery', 'Returned']
VEHICLE_TYPES = ['Truck', 'Mini Truck', 'Container Truck']
TRAFFIC_LEVELS = ['Low', 'Medium', 'High', 'Very High']
WEATHER_CONDITIONS = ['Clear', 'Rain', 'Heavy Rain', 'Fog', 'Cloudy', 'Stormy', 'Hot', 'Humid']
DOWNTIME_REASONS = ['Scheduled Maintenance', 'Material Shortage', 'Technical Issue', 'Operator Break', 'Quality Check', 'Power Outage', 'Equipment Failure']
WAREHOUSE_LOCATIONS = ['Gurgaon', 'Pune', 'Chennai', 'Bangalore', 'Mumbai', 'Ahmedabad', 'Hyderabad', 'Kolkata', 'Surat', 'Indore', 'Coimbatore', 'Noida', 'Faridabad', 'Manesar']
INDIAN_FIRST_NAMES = ['Amit', 'Raj', 'Priya', 'Sunita', 'Rahul', 'Neha', 'Vikram', 'Kavya', 'Arjun', 'Pooja', 'Ravi', 'Meera', 'Sanjay', 'Deepika', 'Anil', 'Shweta', 'Rohan', 'Anita', 'Suresh', 'Nisha', 'Karan', 'Sneha', 'Ajay', 'Ritu', 'Varun', 'Preeti', 'Manoj', 'Divya', 'Ashok', 'Geeta', 'Nitin', 'Sakshi', 'Ramesh', 'Shreya', 'Gaurav', 'Anjali', 'Pavan', 'Aarti', 'Naveen', 'Ruchi', 'Sachin', 'Jyoti']
INDIAN_LAST_NAMES = ['Sharma', 'Patel', 'Singh', 'Kumar', 'Agarwal', 'Gupta', 'Jain', 'Bansal', 'Mittal', 'Shah', 'Mehta', 'Malhotra', 'Kapoor', 'Chopra', 'Joshi', 'Verma', 'Yadav', 'Reddy', 'Nair', 'Iyer', 'Menon', 'Krishnan', 'Rao', 'Bose', 'Ghosh', 'Mukherjee', 'Chatterjee', 'Das']

COST_PRICE_RANGES = {
    'Electronics': (5000, 100000), 'Clothing & Fashion': (300, 10000), 'Home & Furniture': (2000, 50000),
    'Beauty & Personal Care': (100, 2000), 'Food & Beverages': (50, 1000), 'Books & Stationery': (100, 2000),
    'Sports & Fitness': (500, 15000), 'Automotive': (500, 20000), 'Health & Wellness': (200, 5000), 'Toys & Games': (200, 5000)
}
MARKUP_RANGES = {
    'Electronics': (1.1, 1.5), 'Clothing & Fashion': (2.0, 3.5), 'Home & Furniture': (1.5, 2.5),
    'Beauty & Personal Care': (1.8, 3.0), 'Food & Beverages': (1.2, 2.0), 'Books & Stationery': (1.3, 1.8),
    'Sports & Fitness': (1.5, 2.5), 'Automotive': (1.3, 2.0), 'Health & Wellness': (1.5, 2.5), 'Toys & Games': (1.8, 3.0)
}
QTY_RANGES = {
    'Food & Beverages': (1, 10), 'Beauty & Personal Care': (1, 10), 'Clothing & Fashion': (1, 5),
    'Books & Stationery': (1, 5), 'Toys & Games': (1, 5), 'Electronics': (1, 2),
    'Home & Furniture': (1, 2), 'Sports & Fitness': (1, 2), 'Automotive': (1, 2), 'Health & Wellness': (1, 2)
}
DISCOUNT_RANGES = {
    'Electronics': (0, 0.2), 'Clothing & Fashion': (0.1, 0.5), 'Food & Beverages': (0, 0.15),
    'Beauty & Personal Care': (0.05, 0.3), 'Home & Furniture': (0.05, 0.25), 'Books & Stationery': (0, 0.2),
    'Sports & Fitness': (0, 0.2), 'Automotive': (0, 0.2), 'Health & Wellness': (0, 0.2), 'Toys & Games': (0, 0.2)
}
GST_RATES = {
    'Food & Beverages': 0.05, 'Books & Stationery': 0.05, 'Clothing & Fashion': 0.12,
    'Beauty & Personal Care': 0.12, 'Electronics': 0.18, 'Home & Furniture': 0.18,
    'Sports & Fitness': 0.18, 'Automotive': 0.18, 'Health & Wellness': 0.18, 'Toys & Games': 0.18
}
PRODUCTION_RANGES = {
    'Food & Beverages': (200, 2000), 'Beauty & Personal Care': (200, 2000), 'Clothing & Fashion': (100, 1000),
    'Books & Stationery': (50, 500), 'Sports & Fitness': (50, 500), 'Automotive': (50, 500),
    'Health & Wellness': (50, 500), 'Toys & Games': (50, 500), 'Home & Furniture': (50, 500), 'Electronics': (50, 500)
}
SALARY_RANGES = {
    'Operator': (20000, 30000), 'Technician': (25000, 35000), 'Supervisor': (40000, 60000),
    'Quality Inspector': (30000, 40000), 'Maintenance': (25000, 35000), 'Floor Manager': (45000, 60000),
    'Safety Officer': (30000, 40000), 'Driver': (25000, 35000), 'Warehouse Manager': (40000, 55000),
    'Inventory Clerk': (20000, 30000), 'Sales Associate': (25000, 35000), 'HR Specialist': (35000, 50000),
    'IT Support': (30000, 45000), 'Logistics Coordinator': (30000, 40000), 'Store Manager': (40000, 60000)
}
DEPARTMENT_MAPPING = {
    'Operator': 'Manufacturing', 'Technician': 'Manufacturing', 'Supervisor': 'Manufacturing',
    'Quality Inspector': 'Manufacturing', 'Maintenance': 'Manufacturing', 'Floor Manager': 'Manufacturing',
    'Safety Officer': 'Manufacturing', 'Driver': 'Logistics', 'Warehouse Manager': 'Inventory Management',
    'Inventory Clerk': 'Inventory Management', 'Sales Associate': 'Sales', 'HR Specialist': 'Human Resources',
    'IT Support': 'Information Technology', 'Logistics Coordinator': 'Logistics', 'Store Manager': 'Store Management'
}
MACHINE_BRANDS = {
    'Textile Loom': ['Lakshmi Machine Works', 'Rieter', 'Trutzschler', 'Picanol'],
    'CNC Machine': ['HMT', 'Haas', 'DMG Mori', 'Mazak', 'Okuma'],
    'Injection Molding': ['Arburg', 'Engel', 'Sumitomo', 'Husky'],
    'Packaging Machine': ['Bosch Packaging', 'Tetra Pak', 'I.M.A. Industria Macchine Automatiche', 'Mitsubishi'],
    'Food Processing Unit': ['GEA Group', 'SPX Flow', 'JBT Corporation', 'Alfa Laval'],
    'Assembly Line': ['Siemens', 'Rockwell Automation', 'ABB', 'Fanuc'],
    'Quality Control Station': ['Mitutoyo', 'Hexagon', 'Zeiss', 'Keyence'],
    'Printing Press': ['Heidelberg', 'Man Roland', 'Komori', 'KBA'],
    'Welding Station': ['Lincoln Electric', 'Miller Electric', 'ESAB', 'Fronius']
}
AVAILABILITY_OPTIONS = {
    'Driver': ['Available', 'On Trip', 'Off Duty'],
    'default': ['Available', 'On Duty', 'Off Duty']
}
LICENSE_PREFIXES = ['KA', 'MH', 'DL', 'TN', 'GJ', 'UP', 'RJ']
LICENSE_SUFFIXES = ['A', 'B', 'C']
TRAFFIC_FACTORS = {'Low': (1.0, 1.3), 'Medium': (1.3, 1.7), 'High': (1.7, 2.0), 'Very High': (2.0, 2.5)}
MANUFACTURING_ROLES = {'Operator', 'Technician', 'Maintenance', 'Quality Inspector'}
ELIGIBLE_ORDER_ROLES = {'Sales Associate', 'Store Manager', 'Logistics Coordinator'}
ELIGIBLE_SHIP_ROLES = {'Driver', 'Warehouse Manager', 'Logistics Coordinator'}
STORE_NAME_PREFIXES = ['Big Bazaar', 'Reliance Digital', 'Shoppers Stop', 'Lifestyle', 'Future Store', 'Brand Factory', 'Central Mall', 'Express Avenue']
DELAY_REASONS = ['Traffic', 'Weather', 'Vehicle Issue', 'Address Issue', 'Festival Holiday', 'Strike', 'Road Condition']
FINANCE_CATEGORIES = ['Expense', 'Income', 'Marketing', 'Rent']
FINANCE_SUBCATEGORIES = {'Expense': ['Salary', 'Hosting', 'Shipping'], 'Income': ['Sales', 'Service'], 'Marketing': ['Ads', 'Promotions'], 'Rent': ['Office', 'Warehouse']}
MARKETING_CHANNELS = ['Facebook', 'Google Ads', 'Email', 'Instagram', 'LinkedIn']
FINANCIAL_COLUMNS = ['TotalAmount', 'TaxAmount', 'ShippingFee', 'UnitPrice', 'UnitCost', 'ShippingCost', 'RouteCost', 'Salary']
PERISHABLE_CATEGORIES = {'Food & Beverages', 'Beauty & Personal Care', 'Health & Wellness'}
INVENTORY_RANGES = {
    'Electronics': (50, 1000), 'Clothing & Fashion': (200, 5000), 'Food & Beverages': (500, 10000),
    'Beauty & Personal Care': (100, 2000), 'Books & Stationery': (50, 1500), 'Sports & Fitness': (50, 1500),
    'Automotive': (50, 1500), 'Health & Wellness': (50, 1500), 'Toys & Games': (50, 1500), 'Home & Furniture': (50, 1500)
}


class UnifiedDataGenerator:
    def __init__(self, num_records=10000):
        self.num_records = num_records
        self.data = {}

    def _indian_name(self):
        return f"{random.choice(INDIAN_FIRST_NAMES)} {random.choice(INDIAN_LAST_NAMES)}"

    def _indian_phone(self):
        return f"+91 {random.randint(70000, 99999)}{random.randint(10000, 99999)}"

    def _license_number(self):
        return f"{random.choice(LICENSE_PREFIXES)}{random.randint(10, 99)}{random.choice(LICENSE_SUFFIXES)}{random.randint(1000, 9999)}"

    def _clamp_gauss(self, mu, sigma, lo, hi):
        return max(lo, min(hi, random.gauss(mu, sigma)))

    def generate_marketing_spend(self, num_spends=100):
        today = datetime.now().date()
        start = today - timedelta(days=365)
        records = [{
            'SpendID': f'SPEND_{i+1:04d}',
            'Date': fake.date_between(start_date=start, end_date=today),
            'Channel': random.choice(MARKETING_CHANNELS),
            'CampaignName': f'Campaign_{fake.word().title()}_{i+1}',
            'Amount': round(random.uniform(1000, 50000), 2)
        } for i in range(num_spends)]
        self.data['marketing_spend'] = pd.DataFrame(records)
        print(f"Generated {num_spends} marketing spend records.")
        return self.data['marketing_spend']

    def generate_finance_transactions(self, num_transactions=200):
        today = datetime.now().date()
        start = today - timedelta(days=730)
        records = []
        for i in range(num_transactions):
            category = random.choice(FINANCE_CATEGORIES)
            records.append({
                'TransactionID': f'TRANS_{i+1:06d}',
                'Date': fake.date_between(start_date=start, end_date=today),
                'Amount': round(random.uniform(500, 100000), 2),
                'Category': category,
                'SubCategory': random.choice(FINANCE_SUBCATEGORIES[category]),
                'Type': 'Debit' if category == 'Expense' else 'Credit',
                'PaymentMethod': random.choice(['UPI', 'Bank Transfer', 'Cash'])
            })
        self.data['finance_transactions'] = pd.DataFrame(records)
        print(f"Generated {num_transactions} finance transaction records.")
        return self.data['finance_transactions']

    def generate_stores(self, num_stores=50):
        records = [{
            'StoreID': f'STORE_{i+1:04d}',
            'Name': f"{random.choice(STORE_NAME_PREFIXES)} {random.choice(ALL_INDIAN_CITIES)}",
            'Region': random.choice(REGIONS),
            'StoreType': random.choice(STORE_TYPES),
            'ManagerID': None,
            'IsActive': random.choice([True, False]),
            'InventoryCapacity': random.randint(1000, 20000)
        } for i in range(num_stores)]
        self.data['stores'] = pd.DataFrame(records)
        return self.data['stores']

    def generate_customers(self, num_customers=10000):
        records = [{
            'CustomerID': f'CUST_{i+1:06d}',
            'Name': self._indian_name(),
            'Email': fake.email(),
            'Phone': self._indian_phone() if random.random() > 0.05 else None,
            'Location': random.choice(ALL_INDIAN_CITIES),
            'SignupDate': fake.date_between(start_date='-3y', end_date='today'),
            'CustomerSegment': random.choice(CUSTOMER_SEGMENTS)
        } for i in range(num_customers)]
        self.data['customers'] = pd.DataFrame(records)
        return self.data['customers']

    def generate_products(self, num_products=500):
        records = []
        categories = list(PRODUCT_BRAND_MAPPING.keys())
        for i in range(num_products):
            category = random.choice(categories)
            cat_data = PRODUCT_BRAND_MAPPING[category]
            cost_min, cost_max = COST_PRICE_RANGES[category]
            mu = (cost_min + cost_max) / 2
            sigma = (cost_max - cost_min) / 6
            cost_price = round(max(cost_min, min(cost_max, random.gauss(mu, sigma))), 2)
            markup_min, markup_max = MARKUP_RANGES[category]
            sell_price = round(cost_price * random.uniform(markup_min, markup_max) / 10) * 10
            records.append({
                'SKU': f'SKU_{i+1:06d}',
                'Name': f"{random.choice(cat_data['brands'])} {random.choice(cat_data['subcategories'])} {fake.word().title()}",
                'Category': category,
                'Subcategory': random.choice(cat_data['subcategories']),
                'Brand': random.choice(cat_data['brands']),
                'CostPrice': cost_price,
                'SellPrice': sell_price,
                'Status': random.choice(PRODUCT_STATUSES),
                'LaunchDate': fake.date_between(start_date='-5y', end_date='today'),
                'AverageRating': round(random.uniform(3.0, 5.0), 1)
            })
        self.data['products'] = pd.DataFrame(records)
        return self.data['products']

    def generate_warehouses(self, num_warehouses=30):
        suffixes = ['Distribution Center', 'Logistics Hub', 'Warehouse', 'Fulfillment Center']
        records = [{
            'WarehouseID': f'WH_{i+1:03d}',
            'Name': f'{(loc := random.choice(WAREHOUSE_LOCATIONS))} {random.choice(suffixes)}',
            'Location': loc,
            'Capacity': random.randint(20000, 100000),
            'StorageType': random.choices(STORAGE_TYPES, weights=STORAGE_WEIGHTS, k=1)[0]
        } for i in range(num_warehouses)]
        self.data['warehouses'] = pd.DataFrame(records)
        return self.data['warehouses']

    def generate_machines(self, num_machines=300):
        emp_df = self.data.get('employees', pd.DataFrame())
        eligible_ids = emp_df[emp_df['Role'].isin(MANUFACTURING_ROLES)]['EmployeeID'].tolist() if not emp_df.empty else []
        pool = eligible_ids + [None]
        records = []
        for i in range(num_machines):
            mtype = random.choice(MACHINE_TYPES)
            records.append({
                'MachineID': f'MACH_{i+1:03d}',
                'MachineType': mtype,
                'MachineBrand': random.choice(MACHINE_BRANDS.get(mtype, ['Generic'])),
                'PurchaseDate': fake.date_between(start_date='-10y', end_date='-1y'),
                'Location': random.choice(WAREHOUSE_LOCATIONS),
                'Status': random.choices(['Active', 'Maintenance', 'Out of Service', 'Repair'], weights=[0.7, 0.15, 0.08, 0.07], k=1)[0],
                'EmployeeID': random.choice(pool)
            })
        self.data['machines'] = pd.DataFrame(records)
        return self.data['machines']

    def generate_orders_details(self, num_orders=None):
        if num_orders is None:
            num_orders = self.num_records

        today = datetime.now().date()
        start_date = today - timedelta(days=2 * 365)

        festive_periods = [
            ('diwali_2023', 0.2, (datetime(2023, 10, 1).date(), datetime(2023, 11, 30).date())),
            ('christmas_2023', 0.1, (datetime(2023, 12, 1).date(), datetime(2023, 12, 31).date())),
            ('diwali_2024', 0.2, (datetime(2024, 10, 1).date(), datetime(2024, 11, 30).date())),
            ('christmas_2024', 0.1, (datetime(2024, 12, 1).date(), datetime(2024, 12, 31).date())),
            ('diwali_2025', 0.2, (datetime(2025, 10, 1).date(), datetime(2025, 11, 30).date())),
            ('christmas_2025', 0.1, (datetime(2025, 12, 1).date(), datetime(2025, 12, 31).date())),
            ('non_festive', 0.3, (start_date, today))
        ]
        valid_periods = [(name, weight, (s, min(e, today))) for name, weight, (s, e) in festive_periods if s <= today]
        period_names = [p[0] for p in valid_periods]
        period_weights = [p[1] for p in valid_periods]
        period_ranges = {p[0]: p[2] for p in valid_periods}

        emp_df = self.data.get('employees', pd.DataFrame())
        eligible_emp_ids = emp_df[emp_df['Role'].isin(ELIGIBLE_ORDER_ROLES)]['EmployeeID'].tolist() if not emp_df.empty else []

        store_ids = self.data['stores']['StoreID'].tolist()
        customer_ids = self.data['customers']['CustomerID'].tolist()
        skus = self.data['products']['SKU'].tolist()
        sku_to_info = self.data['products'].set_index('SKU')[['Category', 'CostPrice']].to_dict('index')

        orders_details = []
        detail_id = 1

        for i in range(num_orders):
            period = random.choices(period_names, weights=period_weights, k=1)[0]
            s, e = period_ranges[period]
            if s >= e:
                s = e - timedelta(days=1)
            order_date = fake.date_between(start_date=s, end_date=e)

            store_id = random.choice(store_ids)
            customer_id = random.choice(customer_ids)
            employee_id = random.choice(eligible_emp_ids) if eligible_emp_ids else None
            payment_method = random.choices(PAYMENT_METHODS, weights=PAYMENT_WEIGHTS, k=1)[0]
            status = random.choices(ORDER_STATUSES, weights=ORDER_STATUS_WEIGHTS, k=1)[0]
            delivery_type = random.choices(['Standard', 'Express', 'Same-Day'], weights=[0.6, 0.3, 0.1], k=1)[0]
            order_id = f'ORD_{i+1:08d}'
            num_items = random.randint(1, 4)

            for _ in range(num_items):
                sku = random.choice(skus)
                info = sku_to_info[sku]
                category = info['Category']
                cost_price = float(info['CostPrice'])
                unit_cost = round(cost_price * random.uniform(0.95, 1.05), 2)
                unit_price = round(unit_cost * random.uniform(1.2, 1.8), 2)
                d_min, d_max = DISCOUNT_RANGES.get(category, (0, 0.2))
                discount = round(random.uniform(d_min, d_max) * unit_price, 2)
                qty = random.randint(*QTY_RANGES.get(category, (1, 5)))
                tax_rate = GST_RATES.get(category, 0.18)
                base_amount = max(0, qty * (unit_price - discount))
                tax_amount = round(base_amount * tax_rate, 2)
                shipping_fee = round(random.uniform(40, 300) if base_amount < 1000 else random.uniform(150, 500), 2)
                total_amount = round(base_amount + tax_amount + shipping_fee, 2)

                base_row = {
                    'OrderID': order_id, 'OrderDate': order_date, 'StoreID': store_id,
                    'CustomerID': customer_id, 'EmployeeID': employee_id, 'TotalAmount': total_amount,
                    'PaymentMethod': payment_method, 'Currency': 'INR', 'DeliveryType': delivery_type,
                    'TaxAmount': tax_amount, 'ShippingFee': shipping_fee, 'SKU': sku,
                    'Qty': qty, 'UnitPrice': unit_price, 'Discount': discount, 'UnitCost': unit_cost
                }

                if status in ('Refunded', 'Exchanged'):
                    orders_details.append({**base_row, 'DetailID': f'DET_{detail_id:08d}', 'Status': 'Delivered', 'Returned': False, 'ReturnReason': None})
                    detail_id += 1
                    orders_details.append({
                        **base_row,
                        'DetailID': f'DET_{detail_id:08d}',
                        'OrderDate': order_date + timedelta(days=random.randint(1, 30)),
                        'TotalAmount': -total_amount, 'TaxAmount': -tax_amount, 'ShippingFee': -shipping_fee,
                        'Status': status, 'Returned': True, 'ReturnReason': status
                    })
                    detail_id += 1
                else:
                    orders_details.append({**base_row, 'DetailID': f'DET_{detail_id:08d}', 'Status': status, 'Returned': False, 'ReturnReason': None})
                    detail_id += 1

        self.data['orders_details'] = pd.DataFrame(orders_details)
        print(f"Generated {len(orders_details)} order details records.")
        return self.data['orders_details']

    def generate_orders_summary(self):
        od = self.data.get('orders_details')
        if od is None or od.empty:
            print("Warning: No orders_details data available to generate summary!")
            return pd.DataFrame()

        agg_dict = {col: agg for col, agg in {
            'OrderDate': 'first', 'StoreID': 'first', 'CustomerID': 'first', 'EmployeeID': 'first',
            'TotalAmount': 'sum', 'PaymentMethod': 'first',
            'Status': lambda x: x.iloc[-1] if len(x) > 1 else x.iloc[0],
            'Currency': 'first', 'DeliveryType': 'first', 'TaxAmount': 'sum', 'ShippingFee': 'sum'
        }.items() if col in od.columns}

        summary = od.groupby('OrderID').agg(agg_dict).reset_index()
        self.data['orders_summary'] = summary
        print(f"Generated {len(summary)} unique orders in orders_summary.")
        return self.data['orders_summary']

    def generate_inventory_levels(self):
        inventory = []
        wh_df = self.data['warehouses']
        wh_info = wh_df.set_index('WarehouseID')[['Capacity', 'StorageType', 'Location']].to_dict('index')
        wh_ids = wh_df['WarehouseID'].tolist()
        warehouse_totals = {wh: 0 for wh in wh_ids}
        now = datetime.now()

        for _, product in self.data['products'].iterrows():
            sku = product['SKU']
            category = product['Category']
            inv_min, inv_max = INVENTORY_RANGES.get(category, (50, 1500))
            mu = (inv_min + inv_max) / 2
            sigma = (inv_max - inv_min) / 6
            selected_whs = random.sample(wh_ids, random.randint(1, min(3, len(wh_ids))))
            is_perishable = category in PERISHABLE_CATEGORIES

            for wh_id in selected_whs:
                wh = wh_info[wh_id]
                if category == 'Food & Beverages' and wh['StorageType'] != 'Cold Storage':
                    continue
                capacity = wh['Capacity']
                wh_city = wh['Location']

                for weeks_back in range(104):
                    date = (now - timedelta(weeks=weeks_back)).date()
                    base_inv = int(self._clamp_gauss(mu, sigma, inv_min, inv_max))
                    remaining = int(capacity * 0.7) - warehouse_totals[wh_id]
                    on_hand = min(base_inv, max(0, remaining))
                    warehouse_totals[wh_id] += on_hand

                    reserved = random.randint(0, min(int(on_hand * 0.05), 500))
                    safety_stock = int(random.uniform(0.1, 0.2) * inv_max)
                    reorder_point = int(max(safety_stock, on_hand * 0.3 + reserved))

                    prod_city = random.choice(ALL_INDIAN_CITIES)
                    if wh_city == prod_city:
                        days_to_restock = random.randint(1, 7)
                    elif wh_city in METRO_SET and prod_city in METRO_SET:
                        days_to_restock = random.randint(7, 15)
                    else:
                        days_to_restock = random.randint(15, 30)

                    inventory.append({
                        'SKU': sku, 'WarehouseID': wh_id, 'Date': date,
                        'OnHandQty': on_hand, 'ReservedQty': reserved,
                        'ReorderPoint': reorder_point, 'SafetyStock': safety_stock,
                        'DaysToRestock': min(30, days_to_restock),
                        'ShelfLifeDays': random.randint(30, 365) if is_perishable else None
                    })

        self.data['inventory_levels'] = pd.DataFrame(inventory)
        return self.data['inventory_levels']

    def generate_production_runs(self, num_runs=5000):
        machine_ids = self.data['machines']['MachineID'].tolist()
        emp_df = self.data.get('employees', pd.DataFrame())
        mfg_emps = emp_df[emp_df['Department'] == 'Manufacturing']['EmployeeID'].tolist() if not emp_df.empty else []
        skus = self.data['products']['SKU'].tolist()
        sku_to_cat = self.data['products'].set_index('SKU')['Category'].to_dict()

        records = []
        for i in range(num_runs):
            sku = random.choice(skus)
            category = sku_to_cat[sku]
            p_min, p_max = PRODUCTION_RANGES.get(category, (50, 500))
            planned = int(self._clamp_gauss((p_min + p_max) / 2, (p_max - p_min) / 6, p_min, p_max))
            actual = max(0, int(planned * random.uniform(0.85, 0.95)))
            records.append({
                'ProdRunID': f'PROD_{i+1:06d}',
                'Date': fake.date_between(start_date='-2y', end_date='today'),
                'MachineID': random.choice(machine_ids),
                'SKU': sku,
                'PlannedUnits': planned,
                'ActualUnits': actual,
                'ScrapUnits': random.randint(0, int(actual * 0.05)),
                'DowntimeMins': random.randint(0, 480),
                'DowntimeReason': random.choice(DOWNTIME_REASONS) if random.random() > 0.6 else None,
                'EmployeeID': random.choice(mfg_emps) if mfg_emps else None,
                'Shift': random.choice(SHIFTS)
            })
        self.data['production_runs'] = pd.DataFrame(records)
        return self.data['production_runs']

    def generate_shipments(self, num_shipments=8000):
        od = self.data.get('orders_details')
        if od is None or od.empty:
            print("Warning: No orders_details data available!")
            return pd.DataFrame()

        today = datetime.now().date()
        emp_df = self.data.get('employees', pd.DataFrame())
        eligible_emp_ids = emp_df[emp_df['Role'].isin(ELIGIBLE_SHIP_ROLES)]['EmployeeID'].tolist() if not emp_df.empty else []

        unique_orders = od.groupby('OrderID')['OrderDate'].first().reset_index()
        unique_orders['OrderDate'] = pd.to_datetime(unique_orders['OrderDate'])

        cust_loc = self.data['customers'].set_index('CustomerID')['Location'].to_dict()
        od_cust = od.drop_duplicates('OrderID').set_index('OrderID')['CustomerID'].to_dict()
        wh_ids = self.data['warehouses']['WarehouseID'].tolist()
        wh_loc = self.data['warehouses'].set_index('WarehouseID')['Location'].to_dict()

        order_rows = unique_orders.to_dict('records')
        shipments = []

        for i in range(num_shipments):
            row = random.choice(order_rows)
            order_id = row['OrderID']
            order_date = row['OrderDate'].date()
            wh_id = random.choice(wh_ids)
            wh_city = wh_loc[wh_id]
            customer_id = od_cust.get(order_id)
            cust_city = cust_loc.get(customer_id, random.choice(ALL_INDIAN_CITIES))

            if wh_city == cust_city:
                delivery_days = random.randint(2, 3)
            elif wh_city in METRO_SET and cust_city in METRO_SET:
                delivery_days = random.randint(3, 4)
            elif wh_city not in METRO_SET and cust_city not in METRO_SET:
                delivery_days = random.randint(3, 5)
            else:
                delivery_days = random.randint(4, 7)

            delivery_date = order_date + timedelta(days=delivery_days)
            if delivery_date > today:
                days_avail = (today - order_date).days
                if days_avail >= 2:
                    delivery_date = today
                else:
                    continue

            if (delivery_date - order_date).days < 2:
                delivery_date = order_date + timedelta(days=2)
                if delivery_date > today:
                    continue

            distance = round(random.uniform(5, 1500), 2)
            shipments.append({
                'ShipmentID': f'SHIP_{i+1:08d}',
                'OrderID': order_id,
                'WarehouseID': wh_id,
                'ShipDate': order_date + timedelta(days=1),
                'DeliveryDate': delivery_date,
                'DistanceKM': distance,
                'Status': random.choice(SHIPMENT_STATUSES),
                'DelayReason': random.choice(DELAY_REASONS) if random.random() > 0.8 else None,
                'ShippingCost': max(0, round(random.uniform(50, 2000) * (distance / 500), 2)),
                'EmployeeID': random.choice(eligible_emp_ids) if eligible_emp_ids else None
            })

        self.data['shipments'] = pd.DataFrame(shipments)

        val = pd.merge(self.data['shipments'], unique_orders, on='OrderID', how='left')
        val['DeliveryDate'] = pd.to_datetime(val['DeliveryDate'])
        val['OrderDate'] = pd.to_datetime(val['OrderDate'])
        val['FulfillmentDays'] = (val['DeliveryDate'] - val['OrderDate']).dt.days
        neg = val[val['FulfillmentDays'] < 0]
        if len(neg) > 0:
            print(f"ERROR: {len(neg)} shipments have negative fulfillment days!")
        else:
            print(f"SUCCESS: All {len(shipments)} shipments have positive fulfillment days (2-7 days)")
            print(f"Fulfillment days range: {val['FulfillmentDays'].min()} to {val['FulfillmentDays'].max()}")

        return self.data['shipments']

    def generate_routes(self):
        emp_df = self.data.get('employees', pd.DataFrame())
        driver_ids = set(emp_df[emp_df['Role'] == 'Driver']['EmployeeID'].tolist()) if not emp_df.empty else set()
        emp_vehicle = emp_df.set_index('EmployeeID')['VehicleType'].to_dict() if not emp_df.empty else {}

        od_cust = self.data['orders_details'].drop_duplicates('OrderID').set_index('OrderID')['CustomerID'].to_dict()
        cust_loc = self.data['customers'].set_index('CustomerID')['Location'].to_dict()
        wh_loc = self.data['warehouses'].set_index('WarehouseID')['Location'].to_dict()

        routes = []
        for i, (_, s) in enumerate(self.data['shipments'].iterrows()):
            distance = s['DistanceKM']
            emp_id = s['EmployeeID']
            vehicle_type = emp_vehicle.get(emp_id, random.choice(VEHICLE_TYPES)) if emp_id in driver_ids else random.choice(VEHICLE_TYPES)

            if distance <= 50:
                est_time = random.randint(30, 120)
            elif distance <= 500:
                est_time = random.randint(120, 360)
            else:
                est_time = random.randint(360, 720)

            traffic_level = random.choice(TRAFFIC_LEVELS)
            lo, hi = TRAFFIC_FACTORS[traffic_level]
            actual_time = max(est_time, int(est_time * random.uniform(lo, hi)))

            is_heavy = vehicle_type in ('Truck', 'Container Truck')
            route_cost = round(random.uniform(100, 5000) * (distance / 500) * (1.5 if is_heavy else 1.0), 2)

            order_id = s['OrderID']
            customer_id = od_cust.get(order_id)
            end_loc = cust_loc.get(customer_id, random.choice(WAREHOUSE_LOCATIONS))
            start_loc = wh_loc.get(s['WarehouseID'], random.choice(WAREHOUSE_LOCATIONS))

            ship_date = pd.to_datetime(s['ShipDate'])
            start_time = ship_date + pd.Timedelta(hours=random.randint(8, 18), minutes=random.randint(0, 59))
            end_time = start_time + pd.Timedelta(minutes=actual_time)

            routes.append({
                'RouteID': f'ROUTE_{i+1:08d}',
                'ShipmentID': s['ShipmentID'],
                'StartLocation': start_loc,
                'EndLocation': end_loc,
                'EstimatedTimeMin': est_time,
                'ActualTimeMin': actual_time,
                'TrafficLevel': traffic_level,
                'WeatherCondition': random.choice(WEATHER_CONDITIONS),
                'EmployeeID': emp_id,
                'RouteCost': route_cost,
                'StartTime': start_time,
                'EndTime': end_time
            })

        self.data['routes'] = pd.DataFrame(routes)
        return self.data['routes']

    def _build_employee_record(self, emp_id, role, machine_ids, machine_idx, eligible_ship_ids):
        department = DEPARTMENT_MAPPING[role]
        sal_min, sal_max = SALARY_RANGES[role]
        availability = random.choice(AVAILABILITY_OPTIONS.get(role, AVAILABILITY_OPTIONS['default']))
        is_driver = role == 'Driver'
        is_mfg = role in MANUFACTURING_ROLES
        return {
            'EmployeeID': emp_id,
            'Name': self._indian_name(),
            'Role': role,
            'Department': department,
            'HireDate': fake.date_between(start_date='-5y', end_date='today'),
            'Salary': round(random.uniform(sal_min, sal_max), 2),
            'Status': random.choices(['Active', 'On Leave', 'Terminated'], weights=[70, 20, 10], k=1)[0],
            'Location': random.choice(WAREHOUSE_LOCATIONS),
            'Shift': random.choice(SHIFTS),
            'PerformanceScore': round(self._clamp_gauss(3.5, 0.75, 0.0, 5.0), 1),
            'VehicleType': random.choice(VEHICLE_TYPES) if is_driver else None,
            'LicenseNumber': self._license_number() if is_driver else None,
            'Availability': availability,
            'MachineID': machine_ids[machine_idx % len(machine_ids)] if is_mfg and machine_ids else None,
            'ShipmentID': random.choice(eligible_ship_ids) if role in ELIGIBLE_SHIP_ROLES and eligible_ship_ids else None,
            'Phone': self._indian_phone() if random.random() > 0.05 else None,
            'Email': fake.email(),
            'DateOfBirth': fake.date_between(start_date='-60y', end_date='-20y'),
            'Gender': random.choice(['Male', 'Female', 'Other']),
            'AttendanceRate': round(self._clamp_gauss(0.9, 0.05, 0.0, 1.0), 2)
        }

    def generate_initial_employees(self, num_drivers=50):
        existing_count = len(self.data.get('employees', pd.DataFrame()).index)
        records = []
        for i in range(num_drivers):
            emp_id = f'EMP_{existing_count + i + 1:04d}'
            records.append({
                'EmployeeID': emp_id, 'Name': self._indian_name(), 'Role': 'Driver', 'Department': 'Logistics',
                'HireDate': fake.date_between(start_date='-5y', end_date='today'),
                'Salary': round(random.uniform(25000, 35000), 2),
                'Status': random.choices(['Active', 'On Leave', 'Terminated'], weights=[70, 20, 10], k=1)[0],
                'Location': random.choice(WAREHOUSE_LOCATIONS), 'Shift': random.choice(SHIFTS),
                'PerformanceScore': round(self._clamp_gauss(3.5, 0.75, 0.0, 5.0), 1),
                'VehicleType': random.choice(VEHICLE_TYPES), 'LicenseNumber': self._license_number(),
                'Availability': random.choice(AVAILABILITY_OPTIONS['Driver']),
                'MachineID': None, 'ShipmentID': None,
                'Phone': self._indian_phone() if random.random() > 0.05 else None,
                'Email': fake.email(), 'DateOfBirth': fake.date_between(start_date='-60y', end_date='-20y'),
                'Gender': random.choice(['Male', 'Female', 'Other']),
                'AttendanceRate': round(self._clamp_gauss(0.9, 0.05, 0.0, 1.0), 2)
            })
        df_new = pd.DataFrame(records)
        if 'employees' not in self.data or self.data['employees'].empty:
            self.data['employees'] = df_new
        else:
            self.data['employees'] = pd.concat([self.data['employees'], df_new], ignore_index=True)
        print(f"Generated {num_drivers} initial drivers")
        return self.data['employees']

    def generate_employees(self, num_employees=250):
        machine_ids = self.data['machines']['MachineID'].tolist()
        random.shuffle(machine_ids)
        eligible_ship_ids = self.data['shipments']['ShipmentID'].tolist() if 'shipments' in self.data else []
        existing_count = len(self.data.get('employees', pd.DataFrame()).index)

        num_mfg = max(50, int(num_employees * 0.3))
        num_rest = num_employees - num_mfg
        mfg_role_list = list(MANUFACTURING_ROLES)

        records = []
        for i in range(num_mfg):
            emp_id = f'EMP_{existing_count + i + 1:04d}'
            role = random.choice(mfg_role_list)
            records.append(self._build_employee_record(emp_id, role, machine_ids, existing_count + i, eligible_ship_ids))

        offset = existing_count + num_mfg
        for i in range(num_rest):
            emp_id = f'EMP_{offset + i + 1:04d}'
            role = random.choice(ROLES)
            records.append(self._build_employee_record(emp_id, role, machine_ids, offset + i, eligible_ship_ids))

        df_new = pd.DataFrame(records)
        if 'employees' not in self.data or self.data['employees'].empty:
            self.data['employees'] = df_new
        else:
            self.data['employees'] = pd.concat([self.data['employees'], df_new], ignore_index=True)

        if 'shipments' in self.data:
            ship_emp_map = self.data['shipments'].dropna(subset=['EmployeeID']).groupby('EmployeeID')['ShipmentID'].first().to_dict()
            eligible_role_set = ELIGIBLE_SHIP_ROLES
            mask = self.data['employees']['EmployeeID'].isin(ship_emp_map) & self.data['employees']['Role'].isin(eligible_role_set)
            self.data['employees'].loc[mask, 'ShipmentID'] = self.data['employees'].loc[mask, 'EmployeeID'].map(ship_emp_map)

        if 'stores' in self.data and not self.data['stores'].empty:
            mgr_ids = self.data['employees'][self.data['employees']['Role'] == 'Store Manager']['EmployeeID'].tolist()
            if mgr_ids:
                self.data['stores']['ManagerID'] = [random.choice(mgr_ids) for _ in range(len(self.data['stores']))]

        return self.data['employees']

    def generate_all_data(self):
        print("Generating synthetic data...")
        print("1. Generating stores...")
        self.generate_stores(num_stores=50)
        print("2. Generating customers...")
        self.generate_customers(num_customers=10000)
        print("3. Generating products...")
        self.generate_products(num_products=500)
        print("4. Generating warehouses...")
        self.generate_warehouses(num_warehouses=30)
        print("5. Generating initial employees (drivers only)...")
        self.generate_initial_employees(num_drivers=50)
        print("6. Generating orders details...")
        self.generate_orders_details(num_orders=10000)
        print("7. Generating orders summary...")
        self.generate_orders_summary()
        print("8. Generating machines...")
        self.generate_machines(num_machines=250)
        print("9. Generating shipments...")
        self.generate_shipments(num_shipments=8000)
        print("10. Generating full employees...")
        self.generate_employees(num_employees=250)
        print("11. Generating inventory levels...")
        self.generate_inventory_levels()
        print("12. Generating production runs...")
        self.generate_production_runs(num_runs=5000)
        print("13. Generating routes...")
        self.generate_routes()
        print("14. Generating marketing spend...")
        self.generate_marketing_spend(num_spends=100)
        print("15. Generating finance transactions...")
        self.generate_finance_transactions(num_transactions=200)
        print("Data generation complete!")
        return self.data

    def save_to_csv(self, output_dir='data'):
        if not os.access(output_dir, os.W_OK):
            output_dir = os.path.join('C:\\Users\\admin\\Documents', 'ECommerceData')
        os.makedirs(output_dir, exist_ok=True)

        for table_name, df in self.data.items():
            existing_fin_cols = [c for c in FINANCIAL_COLUMNS if c in df.columns]
            if existing_fin_cols:
                neg_mask = (df[existing_fin_cols] < 0).any(axis=1)
                if neg_mask.any():
                    print(f"Critical: {neg_mask.sum()} negative values found in {table_name}, correcting...")
                    for col in existing_fin_cols:
                        df[col] = df[col].clip(lower=0)

            file_path = os.path.join(output_dir, f'{table_name}.csv')
            try:
                df.to_csv(file_path, index=False)
                print(f"Saved {table_name} to {file_path} ({len(df)} records)")
            except Exception as e:
                print(f"Error saving {table_name}: {e}")

    def get_summary(self):
        return {
            name: {'records': len(df), 'columns': len(df.columns), 'memory_usage': df.memory_usage(deep=True).sum()}
            for name, df in self.data.items()
        }


if __name__ == "__main__":
    generator = UnifiedDataGenerator(num_records=10000)
    data = generator.generate_all_data()
    generator.save_to_csv()
    summary = generator.get_summary()
