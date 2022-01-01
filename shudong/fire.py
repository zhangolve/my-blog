import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from tenacity import retry, stop_after_attempt, wait_random

cred = credentials.Certificate('./auth2.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': '13823zxw.appspot.com'
})


@retry(stop=stop_after_attempt(3), wait=wait_random(min=1, max=5))
def get_bucket():
    bucket = storage.bucket()
    return bucket


@retry(stop=stop_after_attempt(3), wait=wait_random(min=1, max=5))
def upload_file_to_bucket(bucket, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.chunk_size = 5 * 1024 * 1024 # Set 5 MB blob size
    blob.upload_from_filename(source_file_name, content_type='image/jpeg',)
    blob.make_public()
    return blob.public_url



def upload_blob(source_file_name, destination_blob_name):
    bucket = get_bucket()
    return upload_file_to_bucket(bucket, source_file_name, destination_blob_name)

