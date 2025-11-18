print("Program: AQI Analyzer")
def calculate_average(aqi_list):

    total = 0
    for value in aqi_list:
        total += value
    return total / len(aqi_list)

print("=== AQI Monitoring System ===")

aqi_values = []
days = int(input("Enter number of days to record AQI: "))

for i in range(days):
    aqi = int(input("Enter AQI for Day no {i+1}:"))
    aqi_values.append(aqi)
average_aqi = calculate_average(aqi_values)

print("\n=== AQI Summary ===")
print("AQI values:", aqi_values)
print(f"Average AQI: {average_aqi:.2f}")

print("\nAir Quality Category based on Average AQI:")

if average_aqi <= 50:
    print("Good – Minimal impact")
elif average_aqi <= 100:
    print("Satisfactory – Minor breathing discomfort")
elif average_aqi <= 200:
    print("Moderate – Breathing discomfort to sensitive people")
elif average_aqi <= 300:
    print("Poor – Breathing discomfort to most people")
elif average_aqi <= 400:
    print("Very Poor – Respiratory illness on prolonged exposure")
else:
    print("Severe – Health impact even on healthy people")

highest_aqi = max(aqi_values)
worst_day = aqi_values.index(highest_aqi) + 1

print(f"\nWorst day: Day {worst_day} with AQI = {highest_aqi}")

threshold = int(input("\nEnter an AQI threshold to check for polluted days: "))
print("Days exceeding threshold:")

for i in range(days):
    if aqi_values[i] > threshold:
        print(f"- Day {i+1}: AQI = {aqi_values[i]}")

print("\nMonitoring Complete! Stay safe and help reduce air pollution.")
