import base64
from google.cloud import storage
import pandas as pd
import json

def bucketandother(event, context):

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message = json.loads(pubsub_message)
    df = pd.DataFrame(message)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('module1capstoneegen-bucket')
    blob = bucket.blob('aapl.csv')
    blob.upload_from_string(data = df.to_csv(), content_type='csv')