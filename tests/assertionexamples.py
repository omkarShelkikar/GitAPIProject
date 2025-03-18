import requests

url = "https://dummyjson.com/products"
res = requests.get(url)
json_data = res.json()

# get total no of products
products = json_data["products"]
print(len(products))
#print(products)

# get product price >10
# count  = 0
# for product in products:
#     if product["price"]>10:
#         count +=1
# print(count)

## Get product name with highest rating
# product_name  = None
# product_rating  = 0.00
#
# for product in products:
#     rating  = float(product["rating"])
#     if rating > product_rating:
#         product_rating = rating
#         product_name = product["title"]
# print(f"Product with highest rating: {product_name}")
# print(f"Rating: {product_rating}")


## find products woth rating more than 4
# product_names  = []
# product_rating  = 0.00
#
# for product in products:
#     rating  = float(product["rating"])
#     if rating > 4:
#         product_names.append(product["title"])
# print(*product_names, sep = "\n")

## sort product based on price
product_dict  = {}
product_price  = 0.00

for product in products:
    price = float(product["price"])
    title  = product["title"]
    product_dict[price] = title
sorted_dict  = dict(sorted(product_dict.items(),reverse=True))
print(sorted_dict)

