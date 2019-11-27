import requests
import json

class AdobeStock:

    def fetch_image_url(self, query):
        url = "https://stock.adobe.io/Rest/Media/1/Search/Files"

        querystring = {"locale":"en_US%0A%20%20%20%20","search_parameters[words] ": query,"search_parameters[limit] ":"1","search_parameters[filters][premium] ":"all","search_parameters[filters][premium]%20":"all"}

        headers = {
            'x-api-key': "d13410a30a8a4287b3e5dc9207ad24ad",
            'x-product': "MySampleApp/1.0",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "fd104974-0d09-4f6b-b1e3-ccad02a7ac10,01e53aaf-18b5-4f54-9e64-1cc3a387aa2a",
            'Host': "stock.adobe.io",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        url = response.json()['files'][0]['thumbnail_url']

        print(url)

        return url