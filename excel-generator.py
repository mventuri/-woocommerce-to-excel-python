from woocommerce import API
import pandas as pd
import json

wcdata = API(
    url='<BASE_URL>',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXX',
    version='wc/v3'
)

newJson = wcdata.get('customers').json()
with open('contacts.json', 'w') as f:
    json.dump(newJson, f, ensure_ascii=False, indent=4)

df_json = pd.read_json('contacts.json')

df_json.to_excel('customers_contacts.xlsx', index=False, columns=('first_name', 'email'))
