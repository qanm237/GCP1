from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()
source_bucket = storage_client.get_bucket("akashb1")
source_blob = source_bucket.blob("abc_copy1.txt")
destination_bucket = storage_client.get_bucket("akashb2")
new_blob = source_bucket.copy_blob(source_blob, destination_bucket, "abccopied.py")
print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(source_blob.name, source_bucket.name, new_blob.name,destination_bucket.name))
