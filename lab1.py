while true:
    item+input("Enter item name (or press Enter to finish):").strip()
    if item=="":
        break
    while true:
        try:
            price=float(input(f"Enter price for{item}(0-200)"))
            if 0<= price<=200:
                item_names.append(item)
                item_prices.append(price)
                break
            else:
                print("Error: price must be between 0 and 200.")
        except ValueError:
            print("please enter a valid number.")        
print (f"Total items: {len(item_names)}")
if item_prices:
    avg_price= sum(item_prices)/ len(item_prices)
    print(f"Average price:{avg_price:2f}")
    
    max_price= max(item_price)
    min_price=min(item_price)
    max_item= item_names[item_prices.index(max_price)]
    min_item=item_names[item_prices.index(min_price)]
    
    print(f"highest price :{max_item}{max_price}")
    print(f"lowest price: {min_item}{max_item}")
else:
    print("no items were entered")
    