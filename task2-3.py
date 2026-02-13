'''Task: Geographic Analysis
Plot the locations of restaurants on a
map using longitude and latitude
coordinates.
Identify any patterns or clusters of
restaurants in specific areas'''
import pandas as pd
import matplotlib.pyplot as plt

# ===== Step 1: Load Dataset =====
df = pd.read_csv("restaurants.csv")

# ===== Step 2: Remove rows with missing latitude or longitude =====
df = df.dropna(subset=['Latitude', 'Longitude'])

# ===== Step 3: Plot Restaurant Locations =====
plt.figure(figsize=(8,6))
plt.scatter(df['Longitude'], df['Latitude'], s=5)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographic Distribution of Restaurants")

plt.show()

# ===== Step 4: Basic Cluster Observation =====
print("===== Geographic Analysis =====")
print("Total restaurants plotted:", len(df))
print("By observing the map, dense areas represent clusters of restaurants.")
