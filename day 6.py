transactions = []
n = int(input("Enter number of transactions: "))
total_amount = 0
for i in range(n):
    amount = int(input("Enter transaction amount: "))
    transactions.append(amount)
    total_amount +=amount
count = len(transactions)
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
for amt in transactions:
    if amt <= 0:
        categories["invalid"].append(amt)
    elif amt <= 500:
        categories["normal"].append(amt)
    elif amt <= 2000:
        categories["large"].append(amt)
    else:
        categories["high_risk"].append(amt)
risk_score = 0
if count > 5:
    risk_score += 2
if total_amount > 5000:
    risk_score += 2
if len(categories["high_risk"]) >= 3:
    risk_score += 2
if risk_score == 0:
    risk_level = "Low Risk"
elif risk_score == 2:
    risk_level = "Moderate Risk"
else:
    risk_level = "High Risk"
print("\nTransaction Categories:", categories)
print("Total Amount Spent:", total_amount)
print("Number of Transactions:", count)
print("Risk Score:", risk_score)
print("summary:",(total_amount,count))
print("Final Risk Level:", risk_level)