# This script was built to scrape webpages for the names of different medical practices that use Athena
# Portals to different clinics are delimited by the numbers in the URL

import requests
from bs4 import BeautifulSoup

def get_clinic_name(clinic_id):
    url = f'https://{clinic_id}.portal.athenahealth.com/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name

start = 12690
end = 12700

master_list = []

for clinic_id in range(start,end+1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != 'Payment Confirmation' and data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address.":
        master_list.append(data_dict)
    print(clinic_id)

master_list

import pandas as pd

df = pd.DataFrame(master_list)

df.to_csv('clinic_data.csv',index=False)