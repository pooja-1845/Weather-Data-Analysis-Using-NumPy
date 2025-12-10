# Weather Data Analysis Using NumPy

import numpy as np

# Step 1: Simulate temperature data
n_cities = 5
days = 7
# Random temperatures between 20°C to 40°C
temps = np.random.randint(20, 41, size=(n_cities, days))
print("Temperature data (°C):\n", temps)

# Step 2: Average temperature per city
avg_temp = temps.mean(axis=1)
print("\nAverage temperature per city:", avg_temp)

# Step 3: Highest and lowest temperature per city
max_temp = temps.max(axis=1)
min_temp = temps.min(axis=1)
print("Highest temperature per city:", max_temp)
print("Lowest temperature per city:", min_temp)

# Step 4: City with highest temperature overall
overall_max_temp = temps.max()
city_index = np.argmax(temps.max(axis=1))
print("\nCity with highest temperature:", city_index, "with", overall_max_temp, "°C")

# Step 5: Days exceeding 35°C
hot_days = np.where(temps > 35)
print("\nDays with temperature above 35°C (city_index, day_index):", list(zip(hot_days[0], hot_days[1])))
