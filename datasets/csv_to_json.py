import csv, json

csv_files = ['ads.csv', 'categories.csv']

def csv_to_json(csv_file_path):
    data = {}
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            print(rows)
            id = rows['Id']
            data[id] = rows

    json_file_path = csv_file_path.split('.')[0] + '.json'
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

for csv_file_path in csv_files:
    csv_to_json(csv_file_path)
