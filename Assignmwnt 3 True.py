cities = [
    ("Lagos", 15000000),
    ("Accra", 2500000),
    ("Kano", 4000000),
    ("Ibadan", 3500000),
    ("Nairobi", 5000000),
    ("Addis Ababa", 5000000),
    ("Khartoum", 6000000),
    ("Dar es Salaam", 7000000),
    ("Maputo", 1100000),
    ("Mogadishu", 2400000)
]
# Sort cities by population 
sorted_cities = sorted(cities, key=lambda x: x[1], reverse=True)

# Get top 3 using a for loop
top_3 = []
for i in range(3):
    top_3.append(sorted_cities[i])

# Print results
print("Top 3 largest cities:")
for city, population in top_3:
    print(city, "-", population)