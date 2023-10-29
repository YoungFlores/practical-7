import json
import csv
import os
import sys


def json_to_csv(input_json_filename):
    if not os.path.exists(input_json_filename):
        print(f"JSON файл '{input_json_filename}' не существует.")
        return
    base_filename = os.path.splitext(input_json_filename)[0]
    output_csv_filename = f"{base_filename}.csv"

    with open(input_json_filename, 'r') as json_file:
        data = json.load(json_file)

        with open(output_csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(data.keys())

            writer.writerow(data.values())

    print(f"Преобразование завершено. Результат сохранен в '{output_csv_filename}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
    else:
        input_json_filename = sys.argv[1]
        json_to_csv(input_json_filename)
