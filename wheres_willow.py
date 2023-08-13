import csv
import random
from datetime import datetime, timedelta
import numpy as np, numpy.random

# Variables

start_date = datetime(1987, 1, 1)
end_date = datetime(1987, 12, 31)

name = "Willow"

country = [
    "United States",
    "Canada",
    "United Kingdom",
    "Australia",
    "Germany",
    "France",
    "Japan",
    "China",
    "India",
    "Brazil"
]

hat = "Bobble hat"

hat_brands = [
    "The North Face",
    "Canada Goose",
    "Columbia",
    "Patagonia",
    "Carhartt",
    "Barts",
    "Fjällräven",
    "UGG",
    "Beanie Babies",
    "Woolrich"
]

hat_col = "Red and white"

glasses_brands = [
    "Ray-Ban",
    "Oakley",
    "Prada",
    "Gucci",
    "Versace",
    "Dolce & Gabbana",
    "Chanel",
    "Tom Ford",
    "Burberry",
    "Michael Kors"
]

glasses = "Round Glasses"

glasses_col = "Black"

shirt_brands = [
    "Ralph Lauren",
    "Tommy Hilfiger",
    "Calvin Klein",
    "Hugo Boss",
    "Brooks Brothers",
    "Lacoste",
    "Levi's",
    "Gap",
    "J.Crew",
    "H&M"
]

shirt = "Long-sleeve"

bag_brands = [
    "Louis Vuitton",
    "Gucci",
    "Chanel",
    "Hermès",
    "Prada",
    "Burberry",
    "Michael Kors",
    "Coach",
    "Fendi",
    "Yves Saint Laurent"
]

bag = 'Messenger bag'

bag_col = 'Brown' 
shirt_col = 'Red and white stripes'

jean_brands = [
    "Levi's",
    "Wrangler",
    "Lee",
    "Diesel",
    "Guess",
    "Calvin Klein Jeans",
    "American Eagle Outfitters",
    "True Religion",
    "AG Jeans",
    "J Brand"
]

jeans =  "Straight Leg Jeans"

jeans_col = 'Blue'

cane = 'Wood'

shoe_brands = [
    "Nike",
    "Adidas",
    "Puma",
    "Reebok",
    "Converse",
    "Vans",
    "New Balance",
    "Under Armour",
    "Jordan",
    "Skechers"
]

shoes =  "Casual Shoes"

shoes_col = 'Brown'

# CSV

csv_path = r'/Users/aidanastridge/Documents/wheres_willow_example.csv'
header = [
    "id", "Name", "Birth Date", "Country", "Hat", "Hat Brand", "Hat Colour", "Glasses", "Glasses Brand", "Glasses Colour", "Shirt", "Shirt brand", "Shirt colour", "Jeans", "Jeans brand", "Jeans colour", "Bag", "Bag Brand", "Bag Colour", "Cane", "Shoes", "Shoes Brand", "Shoes colour"
]

# Functions
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

country_gen = np.random.dirichlet(np.ones(10))
hat_gen = np.random.dirichlet(np.ones(10))
glass_gen = np.random.dirichlet(np.ones(10))
shirt_gen = np.random.dirichlet(np.ones(10))
bag_gen = np.random.dirichlet(np.ones(10))
jean_gen = np.random.dirichlet(np.ones(10))
shoe_gen = np.random.dirichlet(np.ones(10))

# Size
total_rows = 1000  # Desired total rows

 # Simulate
 # CSV

with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    for _ in range(total_rows):
                  index_sim = _
                  name_sim = name
                  birth_date_sim = random_date(start_date, end_date).strftime("%d/%m/%Y")
                  country_sim = random.choices(country, weights = country_gen)[0]
                  hat_sim = hat
                  hat_brands_sim = random.choices(hat_brands, weights = hat_gen)[0]
                  hat_col_sim = hat_col
                  glassess_sim = glasses
                  glasses_brands_sim = random.choices(glasses_brands, weights = glass_gen)[0]
                  glasess_col_sim = glasses_col
                  bag_sim = bag
                  bag_brands_sim = random.choices(bag_brands, weights = bag_gen)[0]
                  bag_col_sim = bag_col
                  shirt_sim = shirt
                  shirt_brands_sim = random.choices(shirt_brands, weights = shirt_gen)[0]
                  shirt_col_sim = shirt_col
                  jeans_sim = jeans
                  jean_brands_sim = random.choices(jean_brands, weights = jean_gen)[0]
                  jean_col_sim = jeans_col
                  cane_sim = cane
                  shoes_sim = shoes
                  shoe_brands_sim = random.choices(shoe_brands, weights = shoe_gen)[0]
                  shoes_col_sim = shoes_col
                  
                  row_data = [
                        index_sim,
                        name_sim,
                        birth_date_sim,
                        country_sim,
                        hat_sim,
                        hat_brands_sim,
                        hat_col_sim,
                        glassess_sim, 
                        glasses_brands_sim, 
                        glasess_col_sim, 
                        shirt_sim, 
                        shirt_brands_sim, 
                        shirt_col_sim,
                        jeans_sim,
                        jean_brands_sim, 
                        jean_col_sim,
                        bag_sim,
                        bag_brands_sim,
                        bag_col_sim,
                        cane_sim, 
                        shoes_sim,
                        shoe_brands_sim, 
                        shoes_col_sim
                        ]
                  
                  writer.writerow(row_data)
      
print("CSV file generated successfully.")