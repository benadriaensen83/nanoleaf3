import requests
import json
import sys

class Nanoleaf2:

    auth_token = 'wzX2GHF9T088yTSZnFvIIOO7CrPX06ye'
    ip_adress = 'http://192.168.178.31:16021'

    def start_christmas_rythm(self):
        url = "{}/api/v1/{}/effects".format(self.ip_adress, self.auth_token)

        payload = "{\"select\": \"Christmas\"}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "787b5262-d02b-41e2-bacd-8a46164b3f5e,e804c32e-9962-468c-a0c2-611ccfb19580",
            'Host': "192.168.178.30:16021",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "23",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("PUT", url, data=payload, headers=headers)

        print(response.text)

    def business_ambient(self, colours):

            url = "{}/api/v1/{}/effects/write".format(self.ip_adress, self.auth_token)

            payload = "{\"write\" : {\r\n\t\"command\" : \"display\",     \r\n\t\"version\": \"2.0\",\r\n    \"animType\": \"plugin\",\r\n    \"colorType\": \"HSB\",\r\n    \"palette\": [\r\n        {\r\n            \"hue\": 200,\r\n            \"saturation\": 100,\r\n            \"brightness\": 99,\r\n            \"probability\": 0.0\r\n        },\r\n        {\r\n            \"hue\": 182,\r\n            \"saturation\": 100,\r\n            \"brightness\": 100,\r\n            \"probability\": 0.0\r\n        },\r\n        {\r\n            \"hue\": 125,\r\n            \"saturation\": 100,\r\n            \"brightness\": 93,\r\n            \"probability\": 0.0\r\n        },\r\n        {\r\n            \"hue\": 62,\r\n            \"saturation\": 100,\r\n            \"brightness\": 100,\r\n            \"probability\": 0.0\r\n        },\r\n        {\r\n            \"hue\": 31,\r\n            \"saturation\": 100,\r\n            \"brightness\": 100,\r\n            \"probability\": 0.0\r\n        }\r\n    ],\r\n    \"pluginType\": \"color\",\r\n    \"pluginUuid\": \"70b7c636-6bf8-491f-89c1-f4103508d642\",\r\n    \"pluginOptions\": [\r\n         {\r\n            \"name\": \"delayTime\",\r\n            \"value\": 0\r\n        },\r\n        {\r\n            \"name\": \"mainColorProb\",\r\n            \"value\": 20\r\n        },\r\n        {\r\n            \"name\": \"transTime\",\r\n            \"value\": 50\r\n        }\r\n    ],\r\n    \"hasOverlay\": false}}"

            data = json.loads(payload)
            palette = data['write']['palette']

            for i in range(len(palette)):
                palette[i]['hue'] = colours[i]['hue']
                palette[i]['brightness'] = colours[i]['brightness']
                palette[i]['saturation'] = colours[i]['saturation']
                palette[i]['probability'] = 0

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


