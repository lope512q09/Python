import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/san_francisco_2018_temperature.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the dates, and high and low temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data from {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "High and Low Temperature - 2018\nSan Fransisco, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.yticks(np.arange(0, 150, step=10))
plt.tick_params(axis='both', which='both', labelsize=16)

plt.show()
