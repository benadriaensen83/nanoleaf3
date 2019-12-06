from blob_interaction import BlobStorage
import time
import json
import run_google
import pickle
import pandas as pd
from io import StringIO

class run_from_dashboard:


    def fetch_blob(self):
        blob = BlobStorage()
        blob.blob_client()

        pass

    def main(self):
        dashboard.fetch_blob()
        with open('blob.json', 'rb') as f:
            f = f.read()
            f = json.loads(f)
            track_name = (f['track_name']['0'])
            track_name_string = track_name.lower()
        track_name = StringIO(track_name_string)

        with open('track_name.json', 'rb') as f:
            f = f.read()
            f = json.loads(f)
            track_name_arch = (f['0']['0'])
        print(track_name_arch)

        if not track_name_arch == track_name_string:
            run_google.main(track_name_string + 'colours')
            df = pd.DataFrame(track_name)
            df.to_json('track_name.json')

        time.sleep(5)
        dashboard.main()
        pass

dashboard = run_from_dashboard()
dashboard.main()





