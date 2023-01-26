import csv

from fastapi import Response


def generate_csv(products):
    csv_lines = []
    header = ["id", "name", "description", "price", "quantity"]
    csv_lines.append(header)
    for product in products:
        csv_lines.append(
            [
                str(product.id),
                product.name,
                product.description,
                str(product.price),
                str(product.quantity),
            ]
        )
    csv_file = "\n".join([",".join(line) for line in csv_lines])
    return Response(content=csv_file, media_type="text/csv")
