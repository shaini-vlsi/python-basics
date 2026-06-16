# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock, price in stocks.items():
    print(f"{stock} : ₹{price}")

total_investment = 0

while True:
    stock_name = input("\nEnter Stock Name (or type EXIT to finish): ").upper()

    if stock_name == "EXIT":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))

        investment = stocks[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ₹{investment}")
    else:
        print("Stock not found!")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ₹{total_investment}")

# Save report to file
with open("investment_report.txt", "w") as file:
    file.write("Stock Portfolio Tracker Report\n")
    file.write(f"Total Investment Value: ₹{total_investment}\n")

print("DEBUG:", total_investment)
print("Report saved as investment_report.txt")
