import json
from pathlib import Path

json_path = Path("7.json")
with open(json_path, "r", encoding="utf-8") as f:
    data_json = json.load(f)

accounts = data_json["accounts"]  
def find_accounts_by_id_pattern(data, pattern):
    return [acc for acc in data if acc["account_id"].startswith(pattern)]
def count_accounts_by_status(data):
    counts = {}
    for acc in data:
        status = acc["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts
def calculate_avg_storage_used(data):
    storages = [acc["storage_used"] for acc in data]
    return sum(storages) / len(storages)
print("\nАккаунты с id начинающимся на 'acc_abc':", find_accounts_by_id_pattern(accounts, "acc_abc"))
print("Количество аккаунтов по статусам:", count_accounts_by_status(accounts))
print("Средний объём хранилища:", calculate_avg_storage_used(accounts))
filtered = find_accounts_by_id_pattern(accounts, "acc_abc")
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=4)

