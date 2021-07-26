from google.cloud import pubsub_v1
import os
from alpha_vantage.timeseries import TimeSeries

class Publish:
    def __init__(self):
        self.credential_path = 'C:/Users/Abhishek/Downloads/module1capstoneegen-411e52390df3.json'
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credential_path
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = 'projects/module1capstoneegen/topics/data_demo'

        self.api_key = 'QRY4X064BD8EQTV7'

    def operation(self):
        ts = TimeSeries(key=self.api_key, output_format='pandas')
        data, metadata = ts.get_intraday(symbol='AAPL', interval='60min', outputsize='compact')
        data = data.to_json()
        data = data.encode("utf-8")
        future = self.publisher.publish(self.topic_path, data, origin="AAPL-data")
        print(future.result())
        print(data)
        print(f"Published messages to {self.topic_path}.")

if __name__ == "__main__":

    publish_obj = Publish()
    publish_obj.operation()