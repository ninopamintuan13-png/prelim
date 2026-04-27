# ============================================
# Store Product Inventory System
# Name: Niño Pamintuan | 2nd Year IT
# ============================================

def get_price_category(price):
    # Determine if Budget, Mid-range, or Premium
    if price < 50:
        return "Budget"
    elif price < 200:
        return "Mid-range"
    else:
        return "Premium"


def check_stock_level(stock):
    # Determine if stock is sufficient
    if stock >= 10:
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"


def save_product(name, price, category, stock, stock_status):
    # Save data to file
    with open("inventory.txt", "a") as file:
        file.write(f"Product: {name} | Price: P{price:.2f} | Category: {category} | Stock: {stock} | Status: {stock_status}\n")


def main():  # Niño Pamintuan | 2nd Year IT
    while True:
        print("\n--- Enter Product Info ---")

        name = input("Product Name: ")

        try:
            price = float(input("Price (in pesos): "))
            stock = int(input("Stock quantity: "))
        except ValueError:
            print("Invalid input. Please enter correct numbers.")
            continue

        # PROCESSING
        category = get_price_category(price)
        stock_status = check_stock_level(stock)

        # OUTPUT
        print("\n--- Product Details ---")
        print(f"Product: {name}")
        print(f"Price: P{price:.2f}")
        print(f"Category: {category}")
        print(f"Stock: {stock}")
        print(f"Stock Status: {stock_status}")

        # SAVE
        save_product(name, price, category, stock, stock_status)
        print("Saved to inventory.txt successfully!")

        # LOOP
        choice = input("\nAdd another product? (yes/no): ").lower()
        if choice != "yes":
            print("Inventory program ended.")
            break


if __name__ == "__main__":
    main()