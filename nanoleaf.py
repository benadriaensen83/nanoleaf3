import requests
import json

class Nanoleaf():

    def display_scene(self, colours):

        url = "http://192.168.1.113:16021/api/v1/D4QJwBQrSb0ymZQwaxsOGijhq57ynCnQ/effects/write"

        payload = "{\n    \"write\": {\n        \"command\": \"display\",\n        \"version\": \"2.0\",\n        \"animType\": \"wheel\",\n        \"colorType\": \"HSB\",\n        \"palette\": [\n            {\n                \"hue\": 200,\n                \"saturation\": 100,\n                \"brightness\": 99,\n                \"probability\": 0\n            },\n            {\n                \"hue\": 182,\n                \"saturation\": 100,\n                \"brightness\": 100,\n                \"probability\": 0\n            },\n            {\n                \"hue\": 125,\n                \"saturation\": 100,\n                \"brightness\": 93,\n                \"probability\": 0\n            },\n            {\n                \"hue\": 62,\n                \"saturation\": 100,\n                \"brightness\": 100,\n                \"probability\": 0\n            },\n            {\n                \"hue\": 31,\n                \"saturation\": 100,\n                \"brightness\": 100,\n                \"probability\": 0\n            }\n        ],\n        \"pluginType\": \"color\",\n        \"pluginUuid\": \"6970681a-20b5-4c5e-8813-bdaebc4ee4fa\",\n        \"pluginOptions\": [\n            {\n                \"name\": \"delayTime\",\n                \"value\": 12\n            },\n            {\n                \"name\": \"direction\",\n                \"value\": \"left\"\n            },\n            {\n                \"name\": \"loop\",\n                \"value\": true\n            },\n            {\n                \"name\": \"transTime\",\n                \"value\": 20\n            }\n        ],\n        \"hasOverlay\": false\n    }\n}"

        data = json.loads(payload)
        palette = data['write']['palette']

        for i in range(len(palette)):
            palette[i]['hue'] = colours[i]['hue']
            palette[i]['brightness'] = colours[i]['brightness']
            palette[i]['saturation'] = colours[i]['saturation']
            palette[i]['probability'] = colours[i]['probability']


        payload = json.dumps(data, indent=2)
        print(payload)

        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "b786dd76-f3b4-4857-99fc-fabd78217587,279bf8e7-4d3b-47db-8107-ef0787210326",
            'Host': "192.168.1.113:16021",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "1817",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("PUT", url, data=payload, headers=headers)

        print(response)