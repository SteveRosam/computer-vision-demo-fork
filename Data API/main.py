import quixstreams as qx
import pandas as pd
from flask import Flask
import os

# init the flas app
app = Flask(__name__)


# Quix injects credentials automatically to the client.
# Alternatively, you can always pass an SDK token manually as an argument.
client = qx.QuixStreamingClient()

print("Opening input topic")
consumer_topic = client.get_topic_consumer(os.environ["input"])

def on_dataframe_received_handler(stream_consumer: qx.StreamConsumer, df: pd.DataFrame):
    print(df)


def on_stream_received_handler(stream_consumer: qx.StreamConsumer):
    print("new stream")
    stream_consumer.timeseries.on_dataframe_received = on_dataframe_received_handler



@app.route("/")
def index():
    return "<h1>Hello!</h1>"

if __name__ == "__main__":
    print("main..")
    from waitress import serve

    #qx.App.run()

    # you can use app.run for dev, but its not secure, stable or particularly efficient
    # app.run(debug=True, host="0.0.0.0", port=80)

    # use waitress instead for production
    serve(app, host="0.0.0.0", port=80)