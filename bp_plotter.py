import matplotlib.pyplot as plt
from datetime import datetime

def plot(bp_data):
    converted = []
    for ts, bp in bp_data.items():
        time_str = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S")
        sys, dia = map(int, bp.split('/'))
        converted.append((time_str, sys, dia))

    converted.sort(key=lambda x: x[0])

    times = [x[0] for x in converted]
    sys_values = [x[1] for x in converted]
    dia_values = [x[2] for x in converted]

    plt.figure(figsize=(10, 5))
    plt.plot(times, sys_values, marker='o', linestyle='-', color='red', label='Systolic')
    plt.plot(times, dia_values, marker='o', linestyle='--', color='blue', label='Diastolic')

    plt.title("Blood Pressure Readings")
    plt.xlabel("Time (24-hour format)")
    plt.ylabel("Blood Pressure (mmHg)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()
