# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for Prod_index in products:
    price_str,qty_str = products[Prod_index]
    price_float = float(price_str)
    qty_int = int(qty_str)
    total_sale = price_float * qty_int
    total_sales_list.append(total_sale)
    print(f"Total sales for {Prod_index}: ${total_sale}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
#print(total_sum)
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
#print(min(total_sales_list))
#print(max(total_sales_list))