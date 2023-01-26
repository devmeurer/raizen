import csv
from app.database.models import Product

def process_csv(file):
    products = []
    file = file.decode("utf-8")
    reader = csv.DictReader(file.splitlines())
    for row in reader:
        product = Product(name=row["name"], description=row["description"], price=float(row["price"]), quantity=int(row["quantity"]))
        products.append(product)
    return products
