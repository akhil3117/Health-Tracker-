import matplotlib.pyplot as plt
from datetime import datetime

def plot(total_data, intake_data, burnt_data):
    def convert_timestamps(data):
        return {
            datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S"): val
            for ts, val in data.items()
        }

    if not total_data:
        print("No total calorie data available. Cannot plot")
    else:
        total_data = convert_timestamps(total_data)
        intake_data = convert_timestamps(intake_data) if intake_data else {}
        burnt_data = convert_timestamps(burnt_data) if burnt_data else {}

        all_times = sorted(total_data.keys())

        total_values = [total_data.get(t, None) for t in all_times]
        intake_values = [intake_data.get(t, None) for t in all_times] if intake_data else None
        burnt_values = [burnt_data.get(t, None) for t in all_times] if burnt_data else None

        plt.figure(figsize=(10, 6))

        plt.plot(all_times, total_values, marker='o', linestyle='-', label='Total Calories', color='purple')

        if intake_values:
            plt.plot(all_times, intake_values, marker='s', linestyle='--', label='Calorie Intake', color='green')

        if burnt_values:
            plt.plot(all_times, burnt_values, marker='^', linestyle=':', label='Calories Burnt', color='orange')

        plt.title("Calorie Readings")
        plt.xlabel("Time (24-hour format)")
        plt.ylabel("Calories")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()