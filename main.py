import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os
from dateutil.relativedelta import relativedelta

fake = Faker('en_IN')

PRODUCT_BRAND_MAPPING = {
    'Electronics': {'brands': ['Samsung', 'Apple', 'OnePlus', 'Xiaomi', 'Realme', 'Oppo', 'Vivo', 'Sony', 'LG', 'Panasonic', 'Boat', 'JBL', 'Dell', 'HP', 'Lenovo', 'Asus'], 'subcategories': ['Smartphones', 'Laptops', 'Tablets', 'Headphones', 'Cameras', 'TVs', 'Audio Systems', 'Smart Watches', 'Gaming Consoles', 'Accessories']},
    'Clothing & Fashion': {'brands': ['Zara', 'H&M', 'Uniqlo', 'Fabindia', 'W for Woman', 'Biba', 'Aurelia', 'Peter England', 'Van Heusen', 'Allen Solly', 'Levi\'s', 'Pepe Jeans', 'Manyavar', 'Sabyasachi'], 'subcategories': ['Kurtas', 'Sarees', 'Jeans', 'T-Shirts', 'Formal Shirts', 'Dresses', 'Footwear', 'Accessories', 'Ethnic Wear', 'Western Wear']},
    'Home & Furniture': {'brands': ['IKEA', 'Godrej', 'Nilkamal', 'Durian', 'Urban Ladder', 'Pepperfry', 'HomeTown', 'Sleepwell', 'Kurlon', 'Wipro Furniture', 'Spacewood'], 'subcategories': ['Sofas', 'Beds', 'Dining Tables', 'Wardrobes', 'Kitchen Appliances', 'Home Decor', 'Mattresses', 'Lighting', 'Storage Solutions', 'Garden Furniture']},
    'Beauty & Personal Care': {'brands': ['Lakme', 'Maybelline', 'L\'Oreal', 'Nykaa', 'Mamaearth', 'Himalaya', 'Dabur', 'Patanjali', 'Nivea', 'Dove', 'Forest Essentials', 'Biotique'], 'subcategories': ['Skincare', 'Makeup', 'Hair Care', 'Fragrances', 'Men\'s Grooming', 'Ayurvedic Products', 'Body Care', 'Nail Care', 'Tools & Accessories']},
    'Food & Beverages': {'brands': ['Amul', 'Britannia', 'Parle', 'ITC', 'Nestle', 'Coca-Cola', 'PepsiCo', 'Haldiram\'s', 'MTR', 'Maggi', 'Tata Tea', 'Mother Dairy', 'Everest'], 'subcategories': ['Snacks', 'Beverages', 'Dairy Products', 'Ready-to-Eat', 'Spices & Condiments', 'Tea & Coffee', 'Sweets & Desserts', 'Health Foods', 'Organic Products']},
    'Books & Stationery': {'brands': ['Penguin', 'Oxford', 'Cambridge', 'Classmate', 'Reynolds', 'Camlin', 'Faber-Castell', 'Navneet', 'Apsara', 'Cello'], 'subcategories': ['Fiction', 'Non-Fiction', 'Educational', 'Children\'s Books', 'Stationery', 'Art Supplies', 'Notebooks', 'Writing Instruments', 'Academic Books']},
    'Sports & Fitness': {'brands': ['Adidas', 'Nike', 'Puma', 'Reebok', 'Decathlon', 'Nivia', 'Cosco', 'Yonex', 'Li-Ning', 'Victor', 'Spalding'], 'subcategories': ['Cricket Equipment', 'Fitness Equipment', 'Athletic Wear', 'Outdoor Sports', 'Yoga & Wellness', 'Badminton', 'Football', 'Basketball', 'Swimming']},
    'Automotive': {'brands': ['Maruti Suzuki', 'Hyundai', 'Tata Motors', 'Mahindra', 'Hero', 'Bajaj', 'TVS', 'Bosch', 'MRF', 'Apollo Tyres', 'Castrol'], 'subcategories': ['Car Accessories', 'Bike Parts', 'Tyres', 'Engine Oil', 'Car Care Products', 'Interior Accessories', 'Safety Equipment', 'Performance Parts']},
    'Health & Wellness': {'brands': ['Dabur', 'Himalaya', 'Patanjali', 'Zandu', 'Revital', 'Centrum', 'Protinex', 'Complan', 'Horlicks', 'Baidyanath'], 'subcategories': ['Ayurvedic Medicine', 'Vitamins', 'Supplements', 'First Aid', 'Personal Hygiene', 'Health Drinks', 'Herbal Products', 'Medical Devices']},
    'Toys & Games': {'brands': ['Funskool', 'Mattel', 'Hasbro', 'Lego', 'Fisher-Price', 'Hot Wheels', 'Barbie', 'Nerf', 'Play-Doh'], 'subcategories': ['Educational Toys', 'Action Figures', 'Board Games', 'Dolls', 'Electronic Toys', 'Building Blocks', 'Puzzles', 'Outdoor Toys', 'Soft Toys']}
}

INDIAN_CITIES = {
    'Metro Cities': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad'],
    'Tier 2 Cities': ['Surat', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Patna', 'Bhopal', 'Ludhiana', 'Agra', 'Vadodara', 'Coimbatore', 'Kochi', 'Visakhapatnam', 'Madurai']
}

ALL_INDIAN_CITIES = INDIAN_CITIES['Metro Cities'] + INDIAN_CITIES['Tier 2 Cities']
REGIONS = ['North India', 'South India', 'West India', 'East India', 'Central India', 'Northeast India']
PAYMENT_METHODS = ['Cash', 'Credit Card', 'Debit Card', 'UPI']
ORDER_STATUSES = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Exchanged', 'Refunded']
CHANNELS = ['Online', 'In-Store', 'Mobile App']
CURRENCIES = ['INR']
RETURN_REASONS = ['Defective', 'Wrong Size', 'Not as Described', 'Changed Mind', 'Damaged in Shipping', 'Better Price Found', 'Quality Issues']
PRODUCT_STATUSES = ['Active', 'Discontinued', 'Out of Stock', 'Limited Stock']
STORE_TYPES = ['Flagship Store', 'Outlet', 'Online Only']
CUSTOMER_SEGMENTS = ['Regular', 'VIP', 'One-time']
STORAGE_TYPES = ['Cold Storage', 'Dry Storage', 'General']
MACHINE_TYPES = ['Textile Loom', 'CNC Machine', 'Injection Molding', 'Packaging Machine', 'Food Processing Unit', 'Assembly Line', 'Quality Control Station', 'Printing Press', 'Welding Station']
SHIFTS = ['Morning', 'Evening', 'Night', 'General']
ROLES = ['Operator', 'Technician', 'Supervisor', 'Quality Inspector', 'Maintenance', 'Floor Manager', 'Safety Officer', 'Driver', 'Warehouse Manager', 'Inventory Clerk', 'Sales Associate', 'HR Specialist', 'IT Support', 'Logistics Coordinator', 'Store Manager']
DEPARTMENTS = ['Manufacturing', 'Logistics', 'Sales', 'Human Resources', 'Information Technology', 'Inventory Management', 'Store Management']
SHIPMENT_STATUSES = ['Delivered', 'In Transit', 'Failed', 'Pending', 'Out for Delivery', 'Returned']
VEHICLE_TYPES = ['Truck', 'Mini Truck', 'Container Truck']
TRAFFIC_LEVELS = ['Low', 'Medium', 'High', 'Very High']
WEATHER_CONDITIONS = ['Clear', 'Rain', 'Heavy Rain', 'Fog', 'Cloudy', 'Stormy', 'Hot', 'Humid']
DRIVER_AVAILABILITY = ['Available', 'On Trip', 'Off Duty', 'On Break']
MACHINE_STATUSES = ['Active', 'Maintenance', 'Out of Service', 'Repair']
DOWNTIME_REASONS = ['Scheduled Maintenance', 'Material Shortage', 'Technical Issue', 'Operator Break', 'Quality Check', 'Power Outage', 'Equipment Failure']
WAREHOUSE_LOCATIONS = ['Gurgaon', 'Pune', 'Chennai', 'Bangalore', 'Mumbai', 'Ahmedabad', 'Hyderabad', 'Kolkata', 'Surat', 'Indore', 'Coimbatore', 'Noida', 'Faridabad', 'Manesar']
INDIAN_FIRST_NAMES = [
    'Amit', 'Raj', 'Priya', 'Sunita', 'Rahul', 'Neha', 'Vikram', 'Kavya', 'Arjun', 'Pooja', 'Ravi', 'Meera', 'Sanjay', 'Deepika',
    'Anil', 'Shweta', 'Rohan', 'Anita', 'Suresh', 'Nisha', 'Karan', 'Sneha', 'Ajay', 'Ritu', 'Varun', 'Preeti', 'Manoj', 'Divya',
    'Ashok', 'Geeta', 'Nitin', 'Sakshi', 'Ramesh', 'Shreya', 'Gaurav', 'Anjali', 'Pavan', 'Aarti', 'Naveen', 'Ruchi', 'Sachin', 'Jyoti'
]
INDIAN_LAST_NAMES = [
    'Sharma', 'Patel', 'Singh', 'Kumar', 'Agarwal', 'Gupta', 'Jain', 'Bansal', 'Mittal', 'Shah', 'Mehta', 'Malhotra', 'Kapoor', 'Chopra',
    'Joshi', 'Verma', 'Yadav', 'Reddy', 'Nair', 'Iyer', 'Menon', 'Krishnan', 'Rao', 'Bose', 'Ghosh', 'Mukherjee', 'Chatterjee', 'Das'
]

class UnifiedDataGenerator:
    def __init__(self, num_records=10000):
        self.num_records = num_records
        self.data = {}

    def clamp_value(self, value, min_value=0):
        return max(min_value, value)

    def generate_indian_name(self):
        first_name = random.choice(INDIAN_FIRST_NAMES)
        last_name = random.choice(INDIAN_LAST_NAMES)
        return f"{first_name} {last_name}"

    def generate_indian_phone(self):
        return f"+91 {random.randint(70000, 99999)}{random.randint(10000, 99999)}"

    def generate_indian_address(self):
        city = random.choice(ALL_INDIAN_CITIES)
        area_types = ['Nagar', 'Colony', 'Society', 'Apartments', 'Residency', 'Heights', 'Park', 'Plaza']
        area_name = f"{random.choice(INDIAN_FIRST_NAMES)} {random.choice(area_types)}"
        return f"{random.randint(1, 999)} {area_name}, {city}"

    def generate_marketing_spend(self, num_spends=100):
        today = datetime.now().date()
        marketing_spends = []
        channels = ['Facebook', 'Google Ads', 'Email', 'Instagram', 'LinkedIn']
        for i in range(num_spends):
            spend_date = fake.date_between(start_date=today - timedelta(days=365), end_date=today)
            marketing_spends.append({
                'SpendID': f'SPEND_{i+1:04d}',
                'Date': spend_date,
                'Channel': random.choice(channels),
                'CampaignName': f'Campaign_{fake.word().title()}_{i+1}',
                'Amount': round(random.uniform(1000, 50000), 2)
            })
        self.data['marketing_spend'] = pd.DataFrame(marketing_spends)
        print(f"Generated {len(marketing_spends)} marketing spend records.")
        return self.data['marketing_spend']

    def generate_finance_transactions(self, num_transactions=200):
        today = datetime.now().date()
        finance_transactions = []
        categories = ['Expense', 'Income', 'Marketing', 'Rent']
        subcategories = {
            'Expense': ['Salary', 'Hosting', 'Shipping'],
            'Income': ['Sales', 'Service'],
            'Marketing': ['Ads', 'Promotions'],
            'Rent': ['Office', 'Warehouse']
        }
        payment_methods = ['UPI', 'Bank Transfer', 'Cash']
        for i in range(num_transactions):
            trans_date = fake.date_between(start_date=today - timedelta(days=730), end_date=today)
            category = random.choice(categories)
            finance_transactions.append({
                'TransactionID': f'TRANS_{i+1:06d}',
                'Date': trans_date,
                'Amount': round(random.uniform(500, 100000), 2),
                'Category': category,
                'SubCategory': random.choice(subcategories[category]),
                'Type': 'Debit' if category == 'Expense' else 'Credit',
                'PaymentMethod': random.choice(payment_methods)
            })
        self.data['finance_transactions'] = pd.DataFrame(finance_transactions)
        print(f"Generated {len(finance_transactions)} finance transaction records.")
        return self.data['finance_transactions']

    def generate_stores(self, num_stores=50):
        stores = []
        for i in range(num_stores):
            city = random.choice(ALL_INDIAN_CITIES)
            region = random.choice(REGIONS)
            store_names = [
                f"Big Bazaar {city}", f"Reliance Digital {city}", f"Shoppers Stop {city}",
                f"Lifestyle {city}", f"Future Store {city}", f"Brand Factory {city}",
                f"Central Mall {city}", f"Express Avenue {city}"
            ]
            store = {
                'StoreID': f'STORE_{i+1:04d}',
                'Name': random.choice(store_names),
                'Region': region,
                'StoreType': random.choice(STORE_TYPES),
                'ManagerID': None,
                'IsActive': random.choice([True, False]),
                'InventoryCapacity': random.randint(1000, 20000) if random.choice(STORE_TYPES) != 'Online Only' else 0
            }
            stores.append(store)
        self.data['stores'] = pd.DataFrame(stores)
        return self.data['stores']

    def generate_customers(self, num_customers=10000):
        customers = []
        for i in range(num_customers):
            signup_date = fake.date_between(start_date='-3y', end_date='today')
            customer = {
                'CustomerID': f'CUST_{i+1:06d}',
                'Name': self.generate_indian_name(),
                'Email': fake.email(),
                'Phone': self.generate_indian_phone() if random.random() > 0.05 else None,
                'Location': random.choice(ALL_INDIAN_CITIES),
                'SignupDate': signup_date,
                'CustomerSegment': random.choice(CUSTOMER_SEGMENTS)
            }
            customers.append(customer)
        self.data['customers'] = pd.DataFrame(customers)
        return self.data['customers']

    def generate_products(self, num_products=500):
        products = []
        cost_price_ranges = {
            'Electronics': (5000, 100000), 'Clothing & Fashion': (300, 10000), 'Home & Furniture': (2000, 50000),
            'Beauty & Personal Care': (100, 2000), 'Food & Beverages': (50, 1000), 'Books & Stationery': (100, 2000),
            'Sports & Fitness': (500, 15000), 'Automotive': (500, 20000), 'Health & Wellness': (200, 5000),
            'Toys & Games': (200, 5000)
        }
        markup_ranges = {
            'Electronics': (1.1, 1.5), 'Clothing & Fashion': (2.0, 3.5), 'Home & Furniture': (1.5, 2.5),
            'Beauty & Personal Care': (1.8, 3.0), 'Food & Beverages': (1.2, 2.0), 'Books & Stationery': (1.3, 1.8),
            'Sports & Fitness': (1.5, 2.5), 'Automotive': (1.3, 2.0), 'Health & Wellness': (1.5, 2.5),
            'Toys & Games': (1.8, 3.0)
        }
        for i in range(num_products):
            category = random.choice(list(PRODUCT_BRAND_MAPPING.keys()))
            category_data = PRODUCT_BRAND_MAPPING[category]
            brand = random.choice(category_data['brands'])
            subcategory = random.choice(category_data['subcategories'])
            cost_min, cost_max = cost_price_ranges.get(category, (100, 5000))
            cost_price = round(random.gauss((cost_min + cost_max) / 2, (cost_max - cost_min) / 6), 2)
            cost_price = max(cost_min, min(cost_max, cost_price))
            markup_min, markup_max = markup_ranges.get(category, (1.2, 2.5))
            sell_price = round(cost_price * random.uniform(markup_min, markup_max) / 10) * 10
            product_name = f"{brand} {subcategory} {fake.word().title()}"
            product = {
                'SKU': f'SKU_{i+1:06d}',
                'Name': product_name,
                'Category': category,
                'Subcategory': subcategory,
                'Brand': brand,
                'CostPrice': cost_price,
                'SellPrice': sell_price,
                'Status': random.choice(PRODUCT_STATUSES),
                'LaunchDate': fake.date_between(start_date='-5y', end_date='today'),
                'AverageRating': round(random.uniform(3.0, 5.0), 1)
            }
            products.append(product)
        self.data['products'] = pd.DataFrame(products)
        return self.data['products']

    def generate_warehouses(self, num_warehouses=30):
        warehouses = []
        for i in range(num_warehouses):
            location = random.choice(WAREHOUSE_LOCATIONS)
            suffixes = ['Distribution Center', 'Logistics Hub', 'Warehouse', 'Fulfillment Center']
            warehouse = {
                'WarehouseID': f'WH_{i+1:03d}',
                'Name': f'{location} {random.choice(suffixes)}',
                'Location': location,
                'Capacity': random.randint(20000, 100000),
                'StorageType': random.choices(STORAGE_TYPES, weights=[0.1, 0.3, 0.6], k=1)[0]
            }
            warehouses.append(warehouse)
        self.data['warehouses'] = pd.DataFrame(warehouses)
        return self.data['warehouses']

    def generate_machines(self, num_machines=300):
        machines = []
        machine_brands = {
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
        manufacturing_roles = ['Operator', 'Technician', 'Maintenance', 'Quality Inspector']
        eligible_employee_ids = self.data['employees'][self.data['employees']['Role'].isin(manufacturing_roles)]['EmployeeID'].tolist() if 'employees' in self.data and not self.data['employees'].empty else []
        for i in range(num_machines):
            machine_type = random.choice(MACHINE_TYPES)
            machine_brand = random.choice(machine_brands.get(machine_type, ['Generic']))
            machine = {
                'MachineID': f'MACH_{i+1:03d}',
                'MachineType': machine_type,
                'MachineBrand': machine_brand,
                'PurchaseDate': fake.date_between(start_date='-10y', end_date='-1y'),
                'Location': random.choice(WAREHOUSE_LOCATIONS),
                'Status': random.choice(MACHINE_STATUSES),
                'EmployeeID': random.choice(eligible_employee_ids + [None]) if eligible_employee_ids else None
            }
            machines.append(machine)
        self.data['machines'] = pd.DataFrame(machines)
        return self.data['machines']

    def generate_orders_details(self, num_orders=None):
        if num_orders is None:
            num_orders = self.num_records
        orders_details = []
        detail_id = 1
        today = datetime.now().date()
        start_date = today - timedelta(days=2*365)
        festive_periods = [
            ('diwali_2023', 0.2, (datetime(2023, 10, 1).date(), datetime(2023, 11, 30).date())),
            ('christmas_2023', 0.1, (datetime(2023, 12, 1).date(), datetime(2023, 12, 31).date())),
            ('diwali_2024', 0.2, (datetime(2024, 10, 1).date(), datetime(2024, 11, 30).date())),
            ('christmas_2024', 0.1, (datetime(2024, 12, 1).date(), datetime(2024, 12, 31).date())),
            ('diwali_2025', 0.2, (datetime(2025, 10, 1).date(), datetime(2025, 11, 30).date())),
            ('christmas_2025', 0.1, (datetime(2025, 12, 1).date(), datetime(2025, 12, 31).date())),
            ('non_festive', 0.3, (start_date, today))
        ]
        valid_periods = [(name, weight, (start, min(end, today))) for name, weight, (start, end) in festive_periods if start <= today]
        eligible_roles = ['Sales Associate', 'Store Manager', 'Logistics Coordinator']
        eligible_employee_ids = self.data['employees'][self.data['employees']['Role'].isin(eligible_roles)]['EmployeeID'].tolist() if 'employees' in self.data and not self.data['employees'].empty else []
        qty_ranges = {
            'Food & Beverages': (1, 10), 'Beauty & Personal Care': (1, 10), 'Clothing & Fashion': (1, 5), 'Books & Stationery': (1, 5),
            'Toys & Games': (1, 5), 'Electronics': (1, 2), 'Home & Furniture': (1, 2), 'Sports & Fitness': (1, 2), 'Automotive': (1, 2), 'Health & Wellness': (1, 2)
        }
        discount_ranges = {
            'Electronics': (0, 0.2), 'Clothing & Fashion': (0.1, 0.5), 'Food & Beverages': (0, 0.15), 'Beauty & Personal Care': (0.05, 0.3),
            'Home & Furniture': (0.05, 0.25), 'Books & Stationery': (0, 0.2), 'Sports & Fitness': (0, 0.2), 'Automotive': (0, 0.2),
            'Health & Wellness': (0, 0.2), 'Toys & Games': (0, 0.2)
        }
        gst_rates = {
            'Food & Beverages': 0.05, 'Books & Stationery': 0.05, 'Clothing & Fashion': 0.12, 'Beauty & Personal Care': 0.12,
            'Electronics': 0.18, 'Home & Furniture': 0.18, 'Sports & Fitness': 0.18, 'Automotive': 0.18, 'Health & Wellness': 0.18, 'Toys & Games': 0.18
        }
        for i in range(num_orders):
            period = random.choices([p[0] for p in valid_periods], weights=[p[1] for p in valid_periods], k=1)[0]
            start, end = next(p[2] for p in valid_periods if p[0] == period)
            if start >= end:
                start = end - timedelta(days=1)
            order_date = fake.date_between(start_date=start, end_date=end)
            store_id = random.choice(self.data['stores']['StoreID'].tolist())
            customer_id = random.choice(self.data['customers']['CustomerID'].tolist())
            employee_id = random.choice(eligible_employee_ids) if eligible_employee_ids else None
            payment_method = random.choices(PAYMENT_METHODS, weights=[0.2, 0.4, 0.3, 0.5], k=1)[0]
            status = random.choices(['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Exchanged', 'Refunded'], weights=[0.3, 0.3, 0.25, 0.1, 0.02, 0.02, 0.03])[0]
            currency = random.choice(CURRENCIES)
            delivery_type = random.choices(['Standard', 'Express', 'Same-Day'], weights=[0.6, 0.3, 0.1])[0]
            order_id = f'ORD_{i+1:08d}'
            num_items = random.randint(1, 4)
            for _ in range(num_items):
                detail_id_str = f'DET_{detail_id:08d}'
                sku = random.choice(self.data['products']['SKU'].tolist())
                product = self.data['products'][self.data['products']['SKU'] == sku].iloc[0]
                category = product['Category']
                cost_price = float(product['CostPrice'])
                unit_cost = round(cost_price * random.uniform(0.95, 1.05), 2)
                unit_price = round(unit_cost * random.uniform(1.2, 1.8), 2)
                discount_min, discount_max = discount_ranges.get(category, (0, 0.2))
                discount = round(random.uniform(discount_min, discount_max) * unit_price, 2)
                qty = random.randint(*qty_ranges.get(category, (1, 5)))
                tax_rate = gst_rates.get(category, 0.18)
                base_amount = max(0, qty * (unit_price - discount))
                tax_amount = round(base_amount * tax_rate, 2)
                shipping_fee = round(random.uniform(40, 300), 2) if base_amount < 1000 else round(random.uniform(150, 500), 2)
                total_amount = round(base_amount + tax_amount + shipping_fee, 2)
                if status in ['Refunded', 'Exchanged']:
                    delivered_detail = {
                        'DetailID': detail_id_str,
                        'OrderID': order_id,
                        'OrderDate': order_date,
                        'StoreID': store_id,
                        'CustomerID': customer_id,
                        'EmployeeID': employee_id,
                        'TotalAmount': total_amount,
                        'PaymentMethod': payment_method,
                        'Status': 'Delivered',
                        'Currency': currency,
                        'DeliveryType': delivery_type,
                        'TaxAmount': tax_amount,
                        'ShippingFee': shipping_fee,
                        'SKU': sku,
                        'Qty': qty,
                        'UnitPrice': unit_price,
                        'Discount': discount,
                        'Returned': False,
                        'ReturnReason': None,
                        'UnitCost': unit_cost
                    }
                    orders_details.append(delivered_detail)
                    detail_id += 1
                    return_detail_id = f'DET_{detail_id:08d}'
                    return_detail = {
                        'DetailID': return_detail_id,
                        'OrderID': order_id,
                        'OrderDate': order_date + timedelta(days=random.randint(1, 30)),
                        'StoreID': store_id,
                        'CustomerID': customer_id,
                        'EmployeeID': employee_id,
                        'TotalAmount': -total_amount,
                        'PaymentMethod': payment_method,
                        'Status': status,
                        'Currency': currency,
                        'DeliveryType': delivery_type,
                        'TaxAmount': -tax_amount,
                        'ShippingFee': -shipping_fee,
                        'SKU': sku,
                        'Qty': qty,
                        'UnitPrice': unit_price,
                        'Discount': discount,
                        'Returned': True,
                        'ReturnReason': status,
                        'UnitCost': unit_cost
                    }
                    orders_details.append(return_detail)
                    detail_id += 1
                else:
                    detail = {
                        'DetailID': detail_id_str,
                        'OrderID': order_id,
                        'OrderDate': order_date,
                        'StoreID': store_id,
                        'CustomerID': customer_id,
                        'EmployeeID': employee_id,
                        'TotalAmount': total_amount,
                        'PaymentMethod': payment_method,
                        'Status': status,
                        'Currency': currency,
                        'DeliveryType': delivery_type,
                        'TaxAmount': tax_amount,
                        'ShippingFee': shipping_fee,
                        'SKU': sku,
                        'Qty': qty,
                        'UnitPrice': unit_price,
                        'Discount': discount,
                        'Returned': False,
                        'ReturnReason': None,
                        'UnitCost': unit_cost
                    }
                    orders_details.append(detail)
                    detail_id += 1
        self.data['orders_details'] = pd.DataFrame(orders_details)
        print(f"Generated {len(orders_details)} order details records.")
        return self.data['orders_details']

    def generate_orders_summary(self):
        if 'orders_details' not in self.data or self.data['orders_details'].empty:
            print("Warning: No orders_details data available to generate summary!")
            return pd.DataFrame()
        available_cols = self.data['orders_details'].columns.tolist()
        desired_cols = {
            'OrderDate': 'first',
            'StoreID': 'first',
            'CustomerID': 'first',
            'EmployeeID': 'first',
            'TotalAmount': 'sum',
            'PaymentMethod': 'first',
            'Status': lambda x: x.iloc[-1] if len(x) > 1 else x.iloc[0],
            'Currency': 'first',
            'DeliveryType': 'first',
            'TaxAmount': 'sum',
            'ShippingFee': 'sum'
        }
        agg_dict = {col: agg_func for col, agg_func in desired_cols.items() if col in available_cols}
        summary = self.data['orders_details'].groupby('OrderID').agg(agg_dict).reset_index()
        self.data['orders_summary'] = summary
        print(f"Generated {len(summary)} unique orders in orders_summary with columns: {summary.columns.tolist()}")
        return self.data['orders_summary']

    def generate_inventory_levels(self):
        inventory = []
        warehouse_totals = {wh: 0 for wh in self.data['warehouses']['WarehouseID']}
        inventory_ranges = {
            'Electronics': (50, 1000), 'Clothing & Fashion': (200, 5000), 'Food & Beverages': (500, 10000),
            'Beauty & Personal Care': (100, 2000), 'Books & Stationery': (50, 1500), 'Sports & Fitness': (50, 1500),
            'Automotive': (50, 1500), 'Health & Wellness': (50, 1500), 'Toys & Games': (50, 1500), 'Home & Furniture': (50, 1500)
        }
        for _, product in self.data['products'].iterrows():
            selected_warehouses = random.sample(self.data['warehouses']['WarehouseID'].tolist(), random.randint(1, min(3, len(self.data['warehouses']))))
            for warehouse_id in selected_warehouses:
                warehouse = self.data['warehouses'][self.data['warehouses']['WarehouseID'] == warehouse_id].iloc[0]
                warehouse_capacity = warehouse['Capacity']
                storage_type = warehouse['StorageType']
                if product['Category'] == 'Food & Beverages' and storage_type != 'Cold Storage':
                    continue
                for weeks_back in range(0, 104, 1):
                    date = datetime.now() - timedelta(weeks=weeks_back)
                    category = product['Category']
                    inv_min, inv_max = inventory_ranges.get(category, (50, 1500))
                    base_inventory = int(random.gauss((inv_min + inv_max) / 2, (inv_max - inv_min) / 6))
                    base_inventory = max(inv_min, min(inv_max, base_inventory))
                    if warehouse_totals[warehouse_id] + base_inventory <= warehouse_capacity * 0.7:
                        on_hand = base_inventory
                        warehouse_totals[warehouse_id] += on_hand
                    else:
                        on_hand = max(0, int(warehouse_capacity * 0.7 - warehouse_totals[warehouse_id]))
                        warehouse_totals[warehouse_id] += on_hand
                    reserved = random.randint(0, min(int(on_hand * 0.05), 500))
                    safety_stock = int(random.uniform(0.1, 0.2) * inv_max)
                    reorder_point = int(max(safety_stock, on_hand * 0.3 + reserved))
                    city = warehouse['Location']
                    product_city = random.choice(ALL_INDIAN_CITIES)
                    if city == product_city:
                        days_to_restock = min(30, random.randint(1, 7))
                    elif city in INDIAN_CITIES['Metro Cities'] and product_city in INDIAN_CITIES['Metro Cities']:
                        days_to_restock = min(30, random.randint(7, 15))
                    else:
                        days_to_restock = min(30, random.randint(15, 30))
                    shelf_life = random.randint(30, 365) if product['Category'] in ['Food & Beverages', 'Beauty & Personal Care', 'Health & Wellness'] else None
                    inventory_record = {
                        'SKU': product['SKU'],
                        'WarehouseID': warehouse_id,
                        'Date': date.date(),
                        'OnHandQty': on_hand,
                        'ReservedQty': reserved,
                        'ReorderPoint': reorder_point,
                        'SafetyStock': safety_stock,
                        'DaysToRestock': days_to_restock,
                        'ShelfLifeDays': shelf_life
                    }
                    inventory.append(inventory_record)
        self.data['inventory_levels'] = pd.DataFrame(inventory)
        return self.data['inventory_levels']

    def generate_production_runs(self, num_runs=5000):
        runs = []
        production_ranges = {
            'Food & Beverages': (200, 2000), 'Beauty & Personal Care': (200, 2000), 'Clothing & Fashion': (100, 1000),
            'Books & Stationery': (50, 500), 'Sports & Fitness': (50, 500), 'Automotive': (50, 500),
            'Health & Wellness': (50, 500), 'Toys & Games': (50, 500), 'Home & Furniture': (50, 500), 'Electronics': (50, 500)
        }
        for i in range(num_runs):
            machine_id = random.choice(self.data['machines']['MachineID'].tolist())
            manufacturing_employees = self.data['employees'][self.data['employees']['Department'] == 'Manufacturing']['EmployeeID'].tolist()
            employee_id = random.choice(manufacturing_employees) if manufacturing_employees else None
            sku = random.choice(self.data['products']['SKU'].tolist())
            category = self.data['products'][self.data['products']['SKU'] == sku]['Category'].iloc[0]
            plan_min, plan_max = production_ranges.get(category, (50, 500))
            planned_units = int(random.gauss((plan_min + plan_max) / 2, (plan_max - plan_min) / 6))
            planned_units = max(plan_min, min(plan_max, planned_units))
            efficiency = random.uniform(0.85, 0.95)
            actual_units = max(0, int(planned_units * efficiency))
            scrap_units = random.randint(0, int(actual_units * 0.05))
            run = {
                'ProdRunID': f'PROD_{i+1:06d}',
                'Date': fake.date_between(start_date='-2y', end_date='today'),
                'MachineID': machine_id,
                'SKU': sku,
                'PlannedUnits': planned_units,
                'ActualUnits': actual_units,
                'ScrapUnits': scrap_units,
                'DowntimeMins': random.randint(0, 480),
                'DowntimeReason': random.choice(DOWNTIME_REASONS) if random.random() > 0.6 else None,
                'EmployeeID': employee_id,
                'Shift': random.choice(SHIFTS)
            }
            runs.append(run)
        self.data['production_runs'] = pd.DataFrame(runs)
        return self.data['production_runs']

    def generate_shipments(self, num_shipments=8000):
        shipments = []
        delay_reasons = ['Traffic', 'Weather', 'Vehicle Issue', 'Address Issue', 'Festival Holiday', 'Strike', 'Road Condition']
        today = datetime.now().date()
        eligible_roles = ['Driver', 'Warehouse Manager', 'Logistics Coordinator']
        eligible_employee_ids = self.data['employees'][self.data['employees']['Role'].isin(eligible_roles)]['EmployeeID'].tolist() if 'employees' in self.data and not self.data['employees'].empty else []
        if 'orders_details' not in self.data or self.data['orders_details'].empty:
            print("Warning: No orders_details data available!")
            return pd.DataFrame()
        unique_orders = self.data['orders_details'].groupby('OrderID')['OrderDate'].first().reset_index()
        if not pd.api.types.is_datetime64_any_dtype(unique_orders['OrderDate']):
            unique_orders['OrderDate'] = pd.to_datetime(unique_orders['OrderDate'])
        order_ids = unique_orders['OrderID'].tolist()
        for i in range(num_shipments):
            selected_order = unique_orders.sample(1).iloc[0]
            order_id = selected_order['OrderID']
            order_date = selected_order['OrderDate'].date() if hasattr(selected_order['OrderDate'], 'date') else selected_order['OrderDate']
            warehouse_id = random.choice(self.data['warehouses']['WarehouseID'].tolist())
            employee_id = random.choice(eligible_employee_ids) if eligible_employee_ids else None
            customer_id = self.data['orders_details'][self.data['orders_details']['OrderID'] == order_id]['CustomerID'].iloc[0]
            warehouse_city = self.data['warehouses'][self.data['warehouses']['WarehouseID'] == warehouse_id]['Location'].iloc[0]
            customer_city = self.data['customers'][self.data['customers']['CustomerID'] == customer_id]['Location'].iloc[0]
            if warehouse_city == customer_city:
                delivery_days = random.randint(2, 3)
            elif (warehouse_city in INDIAN_CITIES['Metro Cities'] and customer_city in INDIAN_CITIES['Metro Cities']):
                delivery_days = random.randint(3, 4)
            elif (warehouse_city in INDIAN_CITIES['Tier 2 Cities'] and customer_city in INDIAN_CITIES['Tier 2 Cities']):
                delivery_days = random.randint(3, 5)
            else:
                delivery_days = random.randint(4, 7)
            ship_date = order_date + timedelta(days=1)
            delivery_date = order_date + timedelta(days=delivery_days)
            if delivery_date > today:
                days_from_order_to_today = (today - order_date).days
                if days_from_order_to_today >= 2:
                    delivery_date = today
                else:
                    continue
            actual_gap = (delivery_date - order_date).days
            if actual_gap < 2:
                delivery_date = order_date + timedelta(days=2)
                if delivery_date > today:
                    continue
            distance = round(random.uniform(5, 1500), 2)
            shipping_cost = max(0, round(random.uniform(50, 2000) * (distance / 500), 2))
            shipment = {
                'ShipmentID': f'SHIP_{i+1:08d}',
                'OrderID': order_id,
                'WarehouseID': warehouse_id,
                'ShipDate': ship_date,
                'DeliveryDate': delivery_date,
                'DistanceKM': distance,
                'Status': random.choice(SHIPMENT_STATUSES),
                'DelayReason': random.choice(delay_reasons) if random.random() > 0.8 else None,
                'ShippingCost': shipping_cost,
                'EmployeeID': employee_id
            }
            shipments.append(shipment)
        self.data['shipments'] = pd.DataFrame(shipments)
        validation_df = pd.merge(self.data['shipments'], unique_orders, on='OrderID', how='left')
        validation_df['DeliveryDate'] = pd.to_datetime(validation_df['DeliveryDate'])
        validation_df['OrderDate'] = pd.to_datetime(validation_df['OrderDate'])
        validation_df['FulfillmentDays'] = (validation_df['DeliveryDate'] - validation_df['OrderDate']).dt.days
        negative_fulfillment = validation_df[validation_df['FulfillmentDays'] < 0]
        if len(negative_fulfillment) > 0:
            print(f"ERROR: {len(negative_fulfillment)} shipments have negative fulfillment days!")
            print(negative_fulfillment[['ShipmentID', 'OrderID', 'OrderDate', 'DeliveryDate', 'FulfillmentDays']].head())
        else:
            print(f"SUCCESS: All {len(shipments)} shipments have positive fulfillment days (2-7 days)")
            print(f"Fulfillment days range: {validation_df['FulfillmentDays'].min()} to {validation_df['FulfillmentDays'].max()}")
        return self.data['shipments']

    def generate_routes(self):
        routes = []
        driver_employee_ids = self.data['employees'][self.data['employees']['Role'] == 'Driver']['EmployeeID'].tolist()
        for i, shipment in enumerate(self.data['shipments'].iterrows()):
            _, shipment_data = shipment
            distance = shipment_data['DistanceKM']
            employee_id = shipment_data['EmployeeID']
            vehicle_type = self.data['employees'][self.data['employees']['EmployeeID'] == employee_id]['VehicleType'].iloc[0] if employee_id in driver_employee_ids else random.choice(VEHICLE_TYPES)
            if distance <= 50:
                estimated_time = random.randint(30, 120)
            elif distance <= 500:
                estimated_time = random.randint(120, 360)
            else:
                estimated_time = random.randint(360, 720)
            traffic_factor = {'Low': random.uniform(1.0, 1.3), 'Medium': random.uniform(1.3, 1.7), 'High': random.uniform(1.7, 2.0), 'Very High': random.uniform(2.0, 2.5)}
            traffic_level = random.choice(TRAFFIC_LEVELS)
            actual_time = max(estimated_time, int(estimated_time * traffic_factor[traffic_level]))
            route_cost = round(random.uniform(100, 5000) * (distance / 500) * (1.5 if vehicle_type in ['Truck', 'Container Truck'] else 1.0), 2)
            order_id = shipment_data['OrderID']
            customer_id = self.data['orders_details'][self.data['orders_details']['OrderID'] == order_id]['CustomerID'].iloc[0] if 'orders_details' in self.data and not self.data['orders_details'].empty else random.choice(self.data['customers']['CustomerID'].tolist())
            customer = self.data['customers'][self.data['customers']['CustomerID'] == customer_id]
            end_location = customer['Location'].iloc[0] if not customer.empty else random.choice(WAREHOUSE_LOCATIONS)
            start_location = self.data['warehouses'][self.data['warehouses']['WarehouseID'] == shipment_data['WarehouseID']]['Location'].iloc[0]
            ship_date = pd.to_datetime(shipment_data['ShipDate'])
            start_hour = random.randint(8, 18)
            start_time = ship_date + pd.Timedelta(hours=start_hour, minutes=random.randint(0, 59))
            end_time = start_time + pd.Timedelta(minutes=actual_time)
            route = {
                'RouteID': f'ROUTE_{i+1:08d}',
                'ShipmentID': shipment_data['ShipmentID'],
                'StartLocation': start_location,
                'EndLocation': end_location,
                'EstimatedTimeMin': estimated_time,
                'ActualTimeMin': actual_time,
                'TrafficLevel': traffic_level,
                'WeatherCondition': random.choice(WEATHER_CONDITIONS),
                'EmployeeID': employee_id,
                'RouteCost': route_cost,
                'StartTime': start_time,
                'EndTime': end_time
            }
            routes.append(route)
        self.data['routes'] = pd.DataFrame(routes)
        print(f"Routes DataFrame (first 5): {self.data['routes'].head()}")
        return self.data['routes']

    def generate_employees(self, num_employees=250):
        employees = []
        department_mapping = {
            'Operator': 'Manufacturing', 'Technician': 'Manufacturing', 'Supervisor': 'Manufacturing',
            'Quality Inspector': 'Manufacturing', 'Maintenance': 'Manufacturing', 'Floor Manager': 'Manufacturing',
            'Safety Officer': 'Manufacturing', 'Driver': 'Logistics', 'Warehouse Manager': 'Inventory Management',
            'Inventory Clerk': 'Inventory Management', 'Sales Associate': 'Sales', 'HR Specialist': 'Human Resources',
            'IT Support': 'Information Technology', 'Logistics Coordinator': 'Logistics', 'Store Manager': 'Store Management'
        }
        salary_ranges = {
            'Operator': (20000, 30000), 'Technician': (25000, 35000), 'Supervisor': (40000, 60000),
            'Quality Inspector': (30000, 40000), 'Maintenance': (25000, 35000), 'Floor Manager': (45000, 60000),
            'Safety Officer': (30000, 40000), 'Driver': (25000, 35000), 'Warehouse Manager': (40000, 55000),
            'Inventory Clerk': (20000, 30000), 'Sales Associate': (25000, 35000), 'HR Specialist': (35000, 50000),
            'IT Support': (30000, 45000), 'Logistics Coordinator': (30000, 40000), 'Store Manager': (40000, 60000)
        }
        availability_options = {
            'Operator': ['Available', 'On Duty', 'Off Duty'], 'Technician': ['Available', 'On Duty', 'Off Duty'],
            'Supervisor': ['Available', 'On Duty', 'Off Duty'], 'Quality Inspector': ['Available', 'On Duty', 'Off Duty'],
            'Maintenance': ['Available', 'On Duty', 'Off Duty'], 'Floor Manager': ['Available', 'On Duty', 'Off Duty'],
            'Safety Officer': ['Available', 'On Duty', 'Off Duty'], 'Driver': ['Available', 'On Trip', 'Off Duty'],
            'Warehouse Manager': ['Available', 'On Duty', 'Off Duty'], 'Inventory Clerk': ['Available', 'On Duty', 'Off Duty'],
            'Sales Associate': ['Available', 'On Duty', 'Off Duty'], 'HR Specialist': ['Available', 'On Duty', 'Off Duty'],
            'IT Support': ['Available', 'On Duty', 'Off Duty'], 'Logistics Coordinator': ['Available', 'On Duty', 'Off Duty'],
            'Store Manager': ['Available', 'On Duty', 'Off Duty']
        }
        if 'machines' not in self.data or self.data['machines'].empty:
            self.generate_machines(num_machines=num_employees)
        machine_ids = self.data['machines']['MachineID'].tolist()
        random.shuffle(machine_ids)
        existing_employees = self.data['employees'].to_dict('records') if 'employees' in self.data and not self.data['employees'].empty else []
        existing_count = len(self.data.get('employees', pd.DataFrame()).index)
        start_id = existing_count + 1
        eligible_roles = ['Driver', 'Warehouse Manager', 'Logistics Coordinator']
        eligible_shipment_ids = self.data['shipments']['ShipmentID'].tolist() if 'shipments' in self.data and not self.data['shipments'].empty else []
        manufacturing_roles = ['Operator', 'Technician', 'Maintenance', 'Quality Inspector']
        num_manufacturing = max(50, int(num_employees * 0.3))
        remaining_employees = num_employees - len(existing_employees) - num_manufacturing
        for i in range(num_manufacturing):
            role = random.choice(manufacturing_roles)
            department = department_mapping[role]
            salary_min, salary_max = salary_ranges[role]
            performance_score = round(max(0.0, min(5.0, random.gauss(3.5, 0.75))), 1)
            employee_location = random.choice(WAREHOUSE_LOCATIONS)
            employee_id = f'EMP_{start_id + i:04d}'
            machine_id = machine_ids[i % len(machine_ids)] if machine_ids else None
            shipment_id = random.choice(eligible_shipment_ids) if role in eligible_roles and eligible_shipment_ids else None
            employee = {
                'EmployeeID': employee_id,
                'Name': self.generate_indian_name(),
                'Role': role,
                'Department': department,
                'HireDate': fake.date_between(start_date='-5y', end_date='today'),
                'Salary': round(random.uniform(salary_min, salary_max), 2),
                'Status': random.choices(['Active', 'On Leave', 'Terminated'], weights=[70, 20, 10], k=1)[0],
                'Location': employee_location,
                'Shift': random.choice(SHIFTS),
                'PerformanceScore': performance_score,
                'VehicleType': random.choice(VEHICLE_TYPES) if role == 'Driver' else None,
                'LicenseNumber': f"{random.choice(['KA', 'MH', 'DL', 'TN', 'GJ', 'UP', 'RJ'])}{random.randint(10, 99)}{random.choice(['A', 'B', 'C'])}{random.randint(1000, 9999)}" if role == 'Driver' else None,
                'Availability': random.choice(availability_options[role]),
                'MachineID': machine_id,
                'ShipmentID': shipment_id,
                'Phone': self.generate_indian_phone() if random.random() > 0.05 else None,
                'Email': fake.email(),
                'DateOfBirth': fake.date_between(start_date='-60y', end_date='-20y'),
                'Gender': random.choice(['Male', 'Female', 'Other']),
                'AttendanceRate': round(max(0.0, min(1.0, random.gauss(0.9, 0.05))), 2)
            }
            employees.append(employee)
        for i in range(remaining_employees):
            role = random.choice(ROLES)
            department = department_mapping[role]
            salary_min, salary_max = salary_ranges[role]
            performance_score = round(max(0.0, min(5.0, random.gauss(3.5, 0.75))), 1)
            employee_location = random.choice(WAREHOUSE_LOCATIONS)
            employee_id = f'EMP_{start_id + num_manufacturing + i:04d}'
            machine_id = machine_ids[(start_id + num_manufacturing + i - 1) % len(machine_ids)] if role in manufacturing_roles and machine_ids else None
            shipment_id = random.choice(eligible_shipment_ids) if role in eligible_roles and eligible_shipment_ids else None
            employee = {
                'EmployeeID': employee_id,
                'Name': self.generate_indian_name(),
                'Role': role,
                'Department': department,
                'HireDate': fake.date_between(start_date='-5y', end_date='today'),
                'Salary': round(random.uniform(salary_min, salary_max), 2),
                'Status': random.choices(['Active', 'On Leave', 'Terminated'], weights=[70, 20, 10], k=1)[0],
                'Location': employee_location,
                'Shift': random.choice(SHIFTS),
                'PerformanceScore': performance_score,
                'VehicleType': random.choice(VEHICLE_TYPES) if role == 'Driver' else None,
                'LicenseNumber': f"{random.choice(['KA', 'MH', 'DL', 'TN', 'GJ', 'UP', 'RJ'])}{random.randint(10, 99)}{random.choice(['A', 'B', 'C'])}{random.randint(1000, 9999)}" if role == 'Driver' else None,
                'Availability': random.choice(availability_options[role]),
                'MachineID': machine_id,
                'ShipmentID': shipment_id,
                'Phone': self.generate_indian_phone() if random.random() > 0.05 else None,
                'Email': fake.email(),
                'DateOfBirth': fake.date_between(start_date='-60y', end_date='-20y'),
                'Gender': random.choice(['Male', 'Female', 'Other']),
                'AttendanceRate': round(max(0.0, min(1.0, random.gauss(0.9, 0.05))), 2)
            }
            employees.append(employee)
        if 'employees' not in self.data or self.data['employees'].empty:
            self.data['employees'] = pd.DataFrame(employees)
        else:
            self.data['employees'] = pd.concat([self.data['employees'], pd.DataFrame(employees)], ignore_index=True)
        if 'shipments' in self.data and 'employees' in self.data:
            shipment_employees = self.data['shipments']['EmployeeID'].dropna().unique().tolist()
            if shipment_employees:
                for index, employee in self.data['employees'].iterrows():
                    if employee['EmployeeID'] in shipment_employees and employee['Role'] in eligible_roles:
                        matching_shipments = self.data['shipments'][self.data['shipments']['EmployeeID'] == employee['EmployeeID']]
                        if not matching_shipments.empty:
                            shipment_id = matching_shipments['ShipmentID'].iloc[0]
                            self.data['employees'].at[index, 'ShipmentID'] = shipment_id
        if 'stores' in self.data and not self.data['stores'].empty:
            manager_roles = ['Store Manager']
            eligible_managers = self.data['employees'][self.data['employees']['Role'].isin(manager_roles)]['EmployeeID'].tolist()
            for index, store in self.data['stores'].iterrows():
                if eligible_managers:
                    self.data['stores'].at[index, 'ManagerID'] = random.choice(eligible_managers)
                else:
                    self.data['stores'].at[index, 'ManagerID'] = None
        return self.data['employees']

    def generate_initial_employees(self, num_drivers=50):
        employees = []
        role = 'Driver'
        department = 'Logistics'
        salary_range = (25000, 35000)
        availability_options = {'Driver': ['Available', 'On Trip', 'Off Duty', 'On Break']}
        existing_count = len(self.data.get('employees', pd.DataFrame()).index)
        start_id = existing_count + 1
        for i in range(num_drivers):
            performance_score = round(max(0.0, min(5.0, random.gauss(3.5, 0.75))), 1)
            employee_location = random.choice(WAREHOUSE_LOCATIONS)
            employee_id = f'EMP_{start_id + i:04d}'
            employee = {
                'EmployeeID': employee_id,
                'Name': self.generate_indian_name(),
                'Role': role,
                'Department': department,
                'HireDate': fake.date_between(start_date='-5y', end_date='today'),
                'Salary': round(random.uniform(*salary_range), 2),
                'Status': random.choices(['Active', 'On Leave', 'Terminated'], weights=[70, 20, 10], k=1)[0],
                'Location': employee_location,
                'Shift': random.choice(SHIFTS),
                'PerformanceScore': performance_score,
                'VehicleType': random.choice(VEHICLE_TYPES),
                'LicenseNumber': f"{random.choice(['KA', 'MH', 'DL', 'TN', 'GJ', 'UP', 'RJ'])}{random.randint(10, 99)}{random.choice(['A', 'B', 'C'])}{random.randint(1000, 9999)}",
                'Availability': random.choice(availability_options[role]),
                'MachineID': None,
                'ShipmentID': None,
                'Phone': self.generate_indian_phone() if random.random() > 0.05 else None,
                'Email': fake.email(),
                'DateOfBirth': fake.date_between(start_date='-60y', end_date='-20y'),
                'Gender': random.choice(['Male', 'Female', 'Other']),
                'AttendanceRate': round(max(0.0, min(1.0, random.gauss(0.9, 0.05))), 2)
            }
            employees.append(employee)
        if 'employees' not in self.data or self.data['employees'].empty:
            self.data['employees'] = pd.DataFrame(employees)
        else:
            self.data['employees'] = pd.concat([self.data['employees'], pd.DataFrame(employees)], ignore_index=True)
        print(f"Generated {len(employees)} initial drivers")
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
        print("16. Generating inventory snapshots...")
        financial_columns = ['TotalAmount', 'TaxAmount', 'ShippingFee', 'UnitPrice', 'UnitCost']
        for table_name, df in self.data.items():
            if any(col in df.columns for col in financial_columns):
                negative_cols = [col for col in financial_columns if col in df.columns]
                if negative_cols:
                    conditions = [df[col] < 0 for col in negative_cols]
                    combined_condition = conditions[0]
                    for condition in conditions[1:]:
                        combined_condition = combined_condition | condition
                    negative_rows = df[combined_condition]
                    if not negative_rows.empty:
                        print(f"Warning: {len(negative_rows)} negative values found in {table_name}")
        print("Data generation complete!")
        return self.data

    def save_to_csv(self, output_dir='data'):
        if not os.access(output_dir, os.W_OK):
            print(f"Warning: No write permission for {output_dir}. Using C:\\Users\\admin\\Documents\\ECommerceData instead.")
            output_dir = os.path.join('C:\\Users\\admin\\Documents', 'ECommerceData')
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
            except PermissionError as e:
                print(f"Error creating directory {output_dir}: {e}")
                return
        financial_columns = ['TotalAmount', 'TaxAmount', 'ShippingFee', 'UnitPrice', 'UnitCost', 'ShippingCost', 'RouteCost', 'Salary']
        for table_name, df in self.data.items():
            existing_financial_cols = [col for col in financial_columns if col in df.columns]
            if existing_financial_cols:
                conditions = [df[col] < 0 for col in existing_financial_cols]
                if conditions:
                    combined_condition = conditions[0]
                    for condition in conditions[1:]:
                        combined_condition = combined_condition | condition
                    negative_rows = df[combined_condition]
                    if not negative_rows.empty:
                        print(f"Critical: {len(negative_rows)} negative values found in {table_name} before save:")
                        print(f"Columns checked: {existing_financial_cols}")
                        print(negative_rows.head())
                        for col in existing_financial_cols:
                            df[col] = df[col].apply(lambda x: max(0, x) if pd.notna(x) else x)
                        print(f"Corrected negative values in {table_name}.")
            file_path = os.path.join(output_dir, f'{table_name}.csv')
            try:
                df.to_csv(file_path, index=False)
                print(f"Saved {table_name} to {file_path} ({len(df)} records)")
            except PermissionError as e:
                print(f"Error saving {table_name} to {file_path}: {e}")
            except Exception as e:
                print(f"Unexpected error saving {table_name} to {file_path}: {e}")

    def get_summary(self):
        summary = {}
        for table_name, df in self.data.items():
            summary[table_name] = {
                'records': len(df),
                'columns': len(df.columns),
                'memory_usage': df.memory_usage(deep=True).sum()
            }
        return summary

if __name__ == "__main__":
    generator = UnifiedDataGenerator(num_records=10000)
    data = generator.generate_all_data()
    generator.save_to_csv()
    summary = generator.get_summary()