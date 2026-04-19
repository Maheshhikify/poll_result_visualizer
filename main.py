import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folders if not exist
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Generate Synthetic Poll Data
# -----------------------------
np.random.seed(42)

regions = ['North', 'South', 'East', 'West']
age_groups = ['18-25', '26-35', '36-45', '46+']
options = ['Product A', 'Product B', 'Product C']

rows = 300

data = {
    "Respondent_ID": range(1, rows + 1),
    "Date": pd.date_range(start="2026-01-01", periods=rows, freq="D"),
    "Region": np.random.choice(regions, rows),
    "Age_Group": np.random.choice(age_groups, rows),
    "Choice": np.random.choice(options, rows, p=[0.45, 0.35, 0.20])
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("data/poll_data.csv", index=False)

print("✅ Dataset Created Successfully")
print(df.head())

# -----------------------------
# Poll Summary
# -----------------------------
summary = df["Choice"].value_counts()
percentage = round(df["Choice"].value_counts(normalize=True) * 100, 2)

print("\n📊 Poll Results Summary:")
print(pd.DataFrame({
    "Votes": summary,
    "Percentage": percentage
}))

# -----------------------------
# Chart 1 - Bar Chart
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Choice", data=df, palette="viridis")
plt.title("Poll Results - Votes by Choice")
plt.savefig("outputs/bar_chart.png")
plt.show()

# -----------------------------
# Chart 2 - Pie Chart
# -----------------------------
plt.figure(figsize=(7,7))
summary.plot.pie(autopct='%1.1f%%')
plt.title("Poll Share")
plt.ylabel("")
plt.savefig("outputs/pie_chart.png")
plt.show()

# -----------------------------
# Chart 3 - Region Wise
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Region", hue="Choice", data=df)
plt.title("Region Wise Poll Results")
plt.savefig("outputs/region_chart.png")
plt.show()

# -----------------------------
# Chart 4 - Trend Chart
# -----------------------------
trend = df.groupby(["Date", "Choice"]).size().unstack().fillna(0)

trend.plot(figsize=(10,5))
plt.title("Poll Trend Over Time")
plt.savefig("outputs/trend_chart.png")
plt.show()

print("\n✅ All charts saved in outputs folder.")