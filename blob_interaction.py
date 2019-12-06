from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os, uuid

class BlobStorage():

    def blob_client(self):

        blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=bfh41wbwrsg001stg001;AccountKey=drzpBI8PVPodb8USV9pmv9FEndoo9NnBDdVkYvEIhoOpZrV6PYDwTmrlZy6nGiljZbNvQgMIiPiBkgHX78c/eA==;EndpointSuffix=core.windows.net')
        blob_client = blob_service_client.get_blob_client(container='25nanoleaf', blob='25_for_nanoleaf.json')
        download_file_path = os.path.join('blob.json')
        print("\nDownloading blob to \n\t" + download_file_path)

        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

    def __init__(self):
        pass
