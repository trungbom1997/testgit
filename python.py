import requests,json

response = requests.get('https://teechip.com/rest/retail-products/groups/587d0d41cee36fd012c64a69/shop/men/t-shirts?limit=36&useCatalogSearch=true&recentViewAsShould=true')
data = response.text
jsondata = json.loads(data)
print ("sdfksjhfksfsdfsdfsdfsdsdhfskjdhfks")
