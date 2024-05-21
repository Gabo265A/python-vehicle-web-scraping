import json
import sys
import os

#brand = sys.argv[1]

file_path = os.path.join('vehicles',brand, f'{brand}.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    for field in ['description', 'model', 'name']:
        item[field] = item[field].replace('\u00e1', 'á')
        item[field] = item[field].replace('\u00e9', 'é')
        item[field] = item[field].replace('\u00ed', 'í')
        item[field] = item[field].replace('\u00f3', 'ó')
        item[field] = item[field].replace('\u00fa', 'ú')
        item[field] = item[field].replace('\u00f1', 'ñ')
        item[field] = item[field].replace('\u00c1', 'Á')
        item[field] = item[field].replace('\u00c9', 'É')
        item[field] = item[field].replace('\u00cd', 'Í')
        item[field] = item[field].replace('\u00d3', 'Ó')
        item[field] = item[field].replace('\u00da', 'Ú')
        item[field] = item[field].replace('\u00d1', 'Ñ')
        item[field] = item[field].replace('ë', 'é')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('Special letters replaced successfully!')