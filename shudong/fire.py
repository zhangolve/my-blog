import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage


cred = credentials.Certificate('./auth2.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': '13823zxw.appspot.com'
})


def upload_blob(source_file_name, destination_blob_name):
    bucket = storage.bucket()

    blob = bucket.blob(destination_blob_name)
    blob.chunk_size = 5 * 1024 * 1024 # Set 5 MB blob size
    blob.upload_from_filename(source_file_name, content_type='image/jpeg', timeout=(6.05, 60), num_retries=5)
    blob.make_public()
    return blob.public_url
    # blob.upload_from_file(file)


# upload_blob('./auth.json', 'auth.json')

