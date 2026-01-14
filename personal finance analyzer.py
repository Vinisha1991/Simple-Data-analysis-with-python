import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv("expense_data.csv")
print(df.head())
df["Date"] = pd.to_datetime(df["Date"])
income = df[df["Category"] == "Income"]["Amount"].sum()
expenses_df = df[df["Category"] != "Income"]
total_expense = expenses_df["Amount"].sum()
savings = income - total_expense
# ---------------------------
# Category-wise analysis
# ---------------------------
category_summary = expenses_df.groupby("Category")["Amount"].sum()
# ---------------------------
# Display summary
# ---------------------------
print("----- PERSONAL FINANCE SUMMARY -----")
print(f"Total Income   : ₹{income}")
print(f"Total Expenses : ₹{total_expense}")
print(f"Total Savings  : ₹{savings}")
print("\nCategory-wise Expenses:")
print(category_summary)

# Visualization - Pie Chart
# ---------------------------

plt.figure()
category_summary.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Expense Distribution by Category")
plt.ylabel("")
plt.savefig("images/expense_pie.png")
plt.close()
# ---------------------------
# Visualization - Bar Chart
# ---------------------------
plt.figure()
category_summary.plot(kind="bar", color="skyblue")
plt.title("Category-wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.savefig("images/expense_bar.png")
plt.show()
# ---------------------------
# Budget Insight Logic
# ---------------------------
print("\n----- SMART INSIGHTS -----")
for category, amount in category_summary.items():
    percent = (amount / income) * 100
    if percent > 30:
        print(f"⚠ High spending on {category}: {percent:.1f}% of income")
if savings < income * 0.2:
    print("⚠ Savings below 20% — consider reducing discretionary expenses")
else:
    print("✅ Good savings habit maintained")