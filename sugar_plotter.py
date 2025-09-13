import matplotlib.pyplot as plt
from datetime import datetime

def plot(data):
    converted_data = {
        datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S"): value
        for ts, value in data.items()
    }

    sorted_times = sorted(converted_data.keys())
    sorted_readings = [converted_data[time] for time in sorted_times]

    plt.figure(figsize=(10, 5))
    plt.plot(sorted_times, sorted_readings, marker='o', linestyle='-', color='blue')

    plt.title("Sugar Readings")
    plt.xlabel("Time (24-hour format)")
    plt.ylabel("Sugar Reading (mg/dL)")
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()