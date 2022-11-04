"""
take today's number, then amount of rain per square meter (kg) for each day of the month.
print number and percentage of rainy days
print average amount of rain per day
"""
# variables and first input
today = int(input("Enter today: "))
total_rain = 0
rainy_days = 0

# loop
for i in range(1, today+1):
    rain = int(input("Enter rain: "))
    if rain > 0:
        rainy_days += 1
        total_rain += rain

# calculations
percentage = rainy_days / today * 100
average_rain_per_day = total_rain / today

# printing
print(f"Rainy days: {rainy_days}")
print(f"Percentage of rainy days: %{percentage}")
print(f"Average amount of rain per day: {average_rain_per_day:.2f}")
