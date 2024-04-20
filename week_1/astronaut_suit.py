import urllib.request, json

astro_IDs = []

for i in range(2000):
    num = str(i)
    URL = 'https://scrappyart.s3.ap-south-1.amazonaws.com/json/' + num
    
    with urllib.request.urlopen(URL) as url:
        data = json.load(url)
        
        for trait in data['attributes']:
            if trait['trait_type'] == 'Clothes':
                if trait['value'].endswith('Astronaut Suit'):
                    print(data['name'])
                    print(trait['value'])
                    astro_IDs.append(data['name'])
        # print(data['attributes'][-1]['value'])
        
        # if data['attributes'][-1]['value'] == 'Astronaut':
        #     astro_IDs.append(data['id'])

print(astro_IDs)
            
