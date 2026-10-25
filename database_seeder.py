import sqlite3
import random
from datetime import datetime, timedelta

def create_mock_database():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS trending_products (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            supplier_price REAL,
            selling_price REAL,
            profit_margin REAL,
            order_volume INTEGER,
            trend_score INTEGER
        )
    ''')
    
    # Clear existing data for a fresh seed
    c.execute('DELETE FROM trending_products')
    
    categories = [
        "Adaptive Daily Living Aids", 
        "Ergonomic Kitchen Tools", 
        "Space-Saving Furniture", 
        "Smart Home Tech"
    ]
    
    products = [
        ("Pull-Down Cabinet Shelf Organizer", "Space-Saving Furniture"),
        ("Arthritis-Friendly Jar Opener", "Adaptive Daily Living Aids"),
        ("Ergonomic Silicone Whisks", "Ergonomic Kitchen Tools"),
        ("One-Handed Cutting Board", "Adaptive Daily Living Aids"),
        ("Over-Sink Roll-Up Dish Drying Rack", "Ergonomic Kitchen Tools"),
        ("Motion Sensor Cabinet Lights", "Smart Home Tech"),
        ("Button Hook & Zipper Pull", "Adaptive Daily Living Aids"),
        ("Adjustable Standing Desk Converter", "Space-Saving Furniture")
    ]
    
    for name, category in products:
        supplier_price = round(random.uniform(3.50, 15.00), 2)
        selling_price = round(supplier_price * random.uniform(2.5, 4.0), 2)
        profit_margin = round(selling_price - supplier_price, 2)
        order_volume = random.randint(500, 10000)
        trend_score = random.randint(70, 99)
        
        c.execute('''
            INSERT INTO trending_products 
            (product_name, category, supplier_price, selling_price, profit_margin, order_volume, trend_score)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, category, supplier_price, selling_price, profit_margin, order_volume, trend_score))
        
    conn.commit()
    conn.close()
    print("Database seeded successfully with trending products!")

if __name__ == "__main__":
    create_mock_database()
  
