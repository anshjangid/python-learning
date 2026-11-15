
budget = float(input())   
season = input()        
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * 0.30
        place = "Camp"
    else:
        spent = budget * 0.70
        place = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * 0.40
        place = "Camp"
    else:
        spent = budget * 0.80
        place = "Hotel"

else:
    destination = "Europe"
    spent = budget * 0.90
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {spent:.2f}")
