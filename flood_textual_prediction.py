import numpy as np
import pandas as pd

# Set the number of samples
n_samples = 20000  # You can change this value for more or fewer samples

# Generate 50% no flood expected (Flood Occurred = 1) and 50% flood expected (Flood Occurred = 0)
n_no_flood = n_samples // 2
n_flood = n_samples - n_no_flood

# Generate no flood data (Flood Occurred = 1)
no_flood_data = {
    "Rainfall (mm)": np.random.uniform(0, 50, n_no_flood),
    "Temperature (°C)": np.random.uniform(15, 35, n_no_flood),
    "Humidity (%)": np.random.uniform(20, 70, n_no_flood),
    "River Discharge (m³/s)": np.random.uniform(0, 300, n_no_flood),
    "Water Level (m)": np.random.uniform(0, 3, n_no_flood),
    "Elevation (m)": np.random.uniform(50, 150, n_no_flood),
    "Historical Floods (0 or 1)": np.random.randint(0, 2, n_no_flood),
    "Flood Occurred (0 or 1)": np.ones(n_no_flood)
}

# Generate flood expected data (Flood Occurred = 0)
flood_data = {
    "Rainfall (mm)": np.random.uniform(80, 150, n_flood),
    "Temperature (°C)": np.random.uniform(20, 35, n_flood),
    "Humidity (%)": np.random.uniform(70, 100, n_flood),
    "River Discharge (m³/s)": np.random.uniform(500, 1000, n_flood),
    "Water Level (m)": np.random.uniform(4, 10, n_flood),
    "Elevation (m)": np.random.uniform(0, 50, n_flood),
    "Historical Floods (0 or 1)": np.random.randint(0, 2, n_flood),
    "Flood Occurred (0 or 1)": np.zeros(n_flood)
}

# Convert dictionaries to dataframes
df_no_flood = pd.DataFrame(no_flood_data)
df_flood = pd.DataFrame(flood_data)

# Concatenate no flood and flood data
df = pd.concat([df_no_flood, df_flood], ignore_index=True)

# Shuffle the dataset
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV file
df.to_csv("synthetic_flood_prediction_dataset.csv", index=False)

# Display the first few rows of the dataset
print(df.head())

# Load the dataset (if it's in a CSV file)
df = pd.read_csv("synthetic_flood_prediction_dataset.csv")

# Count the number of "Flood Expected" (Flood Occurred = 0)
flood_expected_count = df[df['Flood Occurred (0 or 1)'] == 0].shape[0]

# Count the number of "No Flood Expected" (Flood Occurred = 1)
no_flood_expected_count = df[df['Flood Occurred (0 or 1)'] == 1].shape[0]

# Print the counts
print(f"Flood Expected (Flood Occurred = 0): {flood_expected_count}")
print(f"No Flood Expected (Flood Occurred = 1): {no_flood_expected_count}")
