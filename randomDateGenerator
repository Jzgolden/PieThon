# Generates 10 random dates for Database challenge 162 

import random
from datetime import datetime, timedelta

# Generate 10 random timestamps
timestamps = []
for _ in range(10):
    # Generate a random datetime within a specific range
    start_date = datetime(2000, 1, 1)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()

    # Format the datetime as yyyy-mm-dd hh:mm:ss
    formatted_timestamp = random_date.strftime('%Y-%m-%d %H:%M:%S')

    # Append the formatted timestamp to the list
    timestamps.append(formatted_timestamp)

# Print the generated timestamps
for timestamp in timestamps:
    print(timestamp)

