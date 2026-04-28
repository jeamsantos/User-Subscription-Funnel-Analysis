import pandas as pd

# Load data
df = pd.read_csv('../data/users.csv')

# Basic overview
print("Total users:", len(df))

# Subscribers
subscribers = df[df['subscribed'] == 1]
print("Subscribers:", len(subscribers))

# Conversion rate
conversion_rate = len(subscribers) / len(df)
print("Conversion rate:", round(conversion_rate, 2))

# Churn rate
churn = df[df['canceled'] == 1]
churn_rate = len(churn) / len(subscribers)
print("Churn rate:", round(churn_rate, 2))

# Revenue
total_revenue = df['revenue'].sum()
avg_revenue = df['revenue'].mean()

print("Total revenue:", total_revenue)
print("Avg revenue per user:", round(avg_revenue, 2))

# Funnel analysis
funnel = {
    "Total Users": len(df),
    "Subscribed Users": len(subscribers),
    "Canceled Users": len(churn)
}

print("\nFunnel:", funnel)

# Conversion by plan
conversion_by_plan = df.groupby('plan').apply(
    lambda x: (x['subscribed'].sum() / len(x))
)

print("\nConversion by plan:\n", conversion_by_plan)
