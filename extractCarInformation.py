from colorama import Fore
import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
import runpy
import os

brands = ['mazda', 'ford', 'kia', 'volkswagen', 'cupra', 'seat', 'suzuki', 'citroen']
car_information = []
car_information_json = json.dumps(car_information, ensure_ascii=False)
print(Fore.GREEN + 'Extracting information...' + Fore.WHITE)
for brand in brands:
    
    url = f'https://www.autoland.com.co/autoland_marcas/{brand}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_='tarjeta')
    pbar = tqdm(total=len(divs), desc=f"Extracting {brand} information", unit="car")
    for div in divs:
        url = div.find('a')['href']
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        if(soup.find('div', class_='descripcion') != None):
            image_url = div.find('div', class_='foto_miniatura').find('img')['src']
            image_response = requests.get(image_url)
            model = div.find('div', class_='nombre').text
            image_file = os.path.join('vehicles', brand, f'{brand} {model}.jpg')
            os.makedirs(os.path.dirname(image_file), exist_ok=True)
            with open(image_file, 'wb') as f:
                f.write(image_response.content)
            price = div.find('div', class_='precio').find('span').text.replace('$', '').replace('.', '')
            description = soup.find('div', class_='descripcion').text
            car_information.append({
                'brand': brand,
                'price': price,
                'model': model,
                'name': f'{brand} {model}',
                'description': description})
        pbar.update()

    car_information_json = json.dumps(car_information, indent=4)
    with open(os.path.join('vehicles', brand, f'{brand}.txt'), 'w', encoding='utf-8') as f:
        f.write(car_information_json)
    pbar.close()
    runpy.run_path('replaceSpecialLetter.py', init_globals={'brand': brand})
    car_information = []
    print(Fore.GREEN + f'{brand.capitalize()} information extracted successfully!' + Fore.WHITE)

print(Fore.GREEN + 'All information extracted successfully!' + Fore.WHITE)