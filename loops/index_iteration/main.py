prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [0.9,0.8,0.85,0.95]
for index in range(len(prices)):
    #print(prices[index])
    if index == 0:
        prices[index]= prices[index] * discount_factor[index]
    elif index == 1:
        prices[index]= prices[index] * discount_factor[index]
    elif index == 2:
        prices[index]= prices[index] * discount_factor[index]
    else:
        prices[index]=prices[index] * discount_factor[index]
    print(f"Updated price for item {index}: ${prices[index]:.2f}")




