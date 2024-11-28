import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_amazon_sales_data(num_rows=50000):
    # Define possible values
    countries = ['USA', 'India', 'UK', 'Germany', 'Canada', 'Australia', 'France', 'Japan', 'Brazil', 'China']
    regions = ['North America', 'Asia', 'Europe', 'South America', 'Oceania']
    product_categories = ['Electronics', 'Books', 'Clothing', 'Home & Kitchen', 'Toys', 'Sports', 'Beauty']
    subcategories = {
        'Electronics': ['Smartphones', 'Laptops', 'Tablets', 'Accessories'],
        'Books': ['Fiction', 'Non-Fiction', 'Academic', 'Children'],
        'Clothing': ["Men's Wear", "Women's Wear", 'Kids', 'Sportswear'],
        'Home & Kitchen': ['Appliances', 'Furniture', 'Cookware', 'Decor'],
        'Toys': ['Educational', 'Action Figures', 'Board Games', 'Puzzles'],
        'Sports': ['Fitness Equipment', 'Outdoor Gear', 'Team Sports', 'Athletic Wear'],
        'Beauty': ['Skincare', 'Makeup', 'Haircare', 'Fragrance']
    }
    customer_segments = ['Prime', 'Regular', 'Business']

    # Initialize data
    data = []
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2024, 12, 31)

    for _ in range(num_rows):
        # Random date generation
        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)
        random_date = start_date + timedelta(days=random_days)

        # Select random values
        country = random.choice(countries)
        region = random.choice(regions)
        category = random.choice(product_categories)
        subcategory = random.choice(subcategories[category])
        
        # Sales and profit calculations
        base_sales = random.uniform(10000, 100000)
        profit_margin = round(random.uniform(0.15, 0.25), 2)
        total_sales = round(base_sales, 2)
        total_profit = round(total_sales * profit_margin, 2)
        num_orders = int(base_sales / random.uniform(50, 500))
        avg_order_value = round(total_sales / num_orders, 2)
        shipping_cost = round(total_sales * 0.05, 2)
        customer_segment = random.choice(customer_segments)

        # Data row
        row = {
            'Year': random_date.year,
            'Month': random_date.strftime('%B'),
            'Quarter': f'Q{(random_date.month-1)//3 + 1}',
            'Day': random_date.day,
            'Country': country,
            'Region': region,
            'Product_Category': category,
            'Subcategory': subcategory,
            'Total_Sales': total_sales,
            'Total_Profit': total_profit,
            'Number_of_Orders': num_orders,
            'Average_Order_Value': avg_order_value,
            'Profit_Margin': profit_margin,
            'Shipping_Cost': shipping_cost,
            'Customer_Segment': customer_segment
        }
        data.append(row)

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

# Generate and save dataset
sales_data = generate_amazon_sales_data(50000)
sales_data.to_csv('amazon_sales_dataset.csv', index=False)
print(f"Dataset generated with {len(sales_data)} rows")