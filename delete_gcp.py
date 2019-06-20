# Imports the Google Cloud client library
from google.cloud import storage
# Instantiates a client
storage_client = storage.Client()

bucket = storage_client.get_bucket("akashb1")
blob = bucket.blob("abc_copt1.txt")

#deleting the file from source bucket
blob.delete()
print('Blob {} deleted.'.format("abc_copt1.txt"))
