# GDP per capita values (USD)
nigeria_gdp = 2200
ghana_gdp = 2400
kenya_gdp = 2100
south_africa_gdp = 7000
seychelles_gdp = 15000

# User input
country = input("Enter an African country: ").lower()

# Match country to GDP
if country == "nigeria":
    gdp = nigeria_gdp
elif country == "ghana":
    gdp = ghana_gdp
elif country == "kenya":
    gdp = kenya_gdp
elif country == "south africa":
    gdp = south_africa_gdp
elif country == "seychelles":
    gdp = seychelles_gdp
else:
    print("Country not in database")
    exit()

# Categorise GDP
if gdp < 1000:
    category = "Low income"
elif gdp <= 10000:
    category = "Middle income"
else:
    category = "High income"

# Output
print("GDP per capita:", gdp)
print("Income category:", category)