import requests

class Serpapi:

    def image_search(self, query):

        url = "https://serpapi.com/search"


        querystring = {"q":query,"tbm":"isch","engine":"google","api_key":"afdc240a8d4231728dd5276242b371584fd6d2cd6b2ddaab391530fdf36e81f5"}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "071e5949-9c02-4cb3-b676-d74fe11e87cc,5e873bce-7571-4d1b-98fe-97b2e60df084",
            'Host': "serpapi.com",
            'Accept-Encoding': "gzip, deflate",
            'Cookie': "__cfduid=dfb181d85b527feb2c065ad5c0f752d251574872767",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        url_list = []
        for i in range(5):
            data = response.json()['images_results'][i]['original']
            url_list.append(data)

        return url_list