import requests
import json
import os


languages = ["spanish", "portuguese", "german"]


os.makedirs("flags", exist_ok=True)

results = {}

for lang in languages:
    
    url = f"https://restcountries.com/v3.1/lang/{lang}"
    response = requests.get(url)
    countries = response.json()

    
    filtered = [
        {
            "name": c.get("name", {}).get("common"),
            "capital": c.get("capital", ["Нет данных"])[0],
            "area": c.get("area", 0),
            "population": c.get("population", 0),
            "flag_url": c.get("flags", {}).get("png")
        }
        for c in countries if c.get("area", 0) > 100000
    ]

    
    results[lang] = filtered

    
    if filtered:
        largest = max(filtered, key=lambda x: x["area"])
        print(f"Для языка {lang} самая большая страна: {largest['name']} (площадь {largest['area']})")

        
        flag_url = largest["flag_url"]
        if flag_url:
            flag_response = requests.get(flag_url)
            flag_path = os.path.join("flags", f"{lang}_flag.png")
            with open(flag_path, "wb") as f:
                f.write(flag_response.content)
            print(f"Флаг сохранён: {flag_path}")


with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Данные сохранены в results.json")
