# Project: ChronosMatch
# Zero-Copy High-Frequency Trading Engine

# Create an empty list to store orders
orders = []

# Function to add a trading order
def add_order(order_id, symbol, side, price, quantity):
    order = {
        "order_id": order_id,
        "symbol": symbol,
        "side": side,
        "price": price,
        "quantity": quantity
    }

    # Save the order in the list
    orders.append(order)

    # Display the order
    print("Order added:", order)

# Add a sample buy order
add_order(1, "AAPL", "BUY", 150.0, 10)

# Display the total number of orders
print("Total orders:", len(orders))
