import pandas as pd
from datetime import datetime

# Read Saturday and Sunday CSV files
saturday_data = pd.read_csv('data_2023-02-11.csv')
sunday_data = pd.read_csv('data_2023-02-12.csv')

# Combine data from both files
combined_data = pd.concat([saturday_data, sunday_data])

# Add a new column for the generation date of the combined file
combined_data['Generation_Date'] = datetime.now().strftime('%Y-%m-%d')

# Save the combined data to a new CSV file
combined_data.to_csv('combined_weekend_data.csv', index=False)

print("Combined weekend data saved successfully.")
