import requests

# query = '''select "cartodb_id","title","description","address","uri","permalink" from (SELECT * FROM sxlocation where type not in ('PROVIDER', 'INVESTOR', 'COWORKING', 'COMMUNITY', 'INCUBATOR', 'ACCELERATOR', 'EDUCATION')) as _cartodbjs_alias where cartodb_id = 21891'''
query1 = '''select "type","title","address","uri" from sxlocation where region_code in ('Basque Country')'''
url = 'https://spainstartupmap.carto.com/api/v1/sql?q={}'.format(query1)

response = requests.get(url)
# print(response.status_code)
array = response.json()['rows']
num = 0
for element in array:
    if element['type'] == 'COMMUNITY':
        print(element)
        num += 1
print(num)
