import csv
with open("7.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    data_csv = list(reader)
for row in data_csv:
    for key, value in row.items():
        print(f"{key} → {value}")
    print("-" * 30)
def find_min_max_temperature(data):
    temps = [float(row["Temperature"]) for row in data]
    return min(temps), max(temps)
def count_high_humidity_days(data):
    return sum(1 for row in data if float(row["Humidity"]) > 80)
def calculate_avg_pressure(data):
    pressures = [float(row["Pressure"]) for row in data]
    return sum(pressures) / len(pressures)
def calculate_city_averages(data):
    city_stats = {}
    for row in data:
        city = row["City"]
        temp = float(row["Temperature"])
        hum = float(row["Humidity"])
        pres = float(row["Pressure"])
        if city not in city_stats:
            city_stats[city] = {"temps": [], "hums": [], "pressures": []}
        city_stats[city]["temps"].append(temp)
        city_stats[city]["hums"].append(hum)
        city_stats[city]["pressures"].append(pres)
    return {city: {
        "avg_temp": sum(stats["temps"]) / len(stats["temps"]),
        "avg_hum": sum(stats["hums"]) / len(stats["hums"]),
        "avg_pres": sum(stats["pressures"]) / len(stats["pressures"])
    } for city, stats in city_stats.items()}

print("\nТемпература min/max:", find_min_max_temperature(data_csv))
print("Дней с влажностью >80%:", count_high_humidity_days(data_csv))
print("Среднее давление:", calculate_avg_pressure(data_csv))
print("Средние показатели по городам:", calculate_city_averages(data_csv))
