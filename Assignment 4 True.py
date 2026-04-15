# Countries and capitals
country = {
    "nigeria": "Abuja",
    "lesotho": "Maseru",
    "mali": "Bamako",
    "namibia": "Windhoek",
    "gabon": "Libreville",
    "burkina faso": "Ouagadougou",
    "zambia": "Lusaka",
    "madagascar": "Antananarivo",
    "botswana": "Gaborone",
    "eritrea": "Asmara"
}

# User input
country_input = input("Enter an African country: ").lower()

# Search for the capital
if country_input in country:
    print("Capital:", country[country_input])
else:
    print("Country not found")