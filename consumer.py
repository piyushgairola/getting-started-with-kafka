
import datetime
from flask import Flask, Response
from kafka import KafkaConsumer


# Set the consumer in a Flask App
app = Flask(__name__)

@app.route('/image', methods=['GET'])
def video():
    topic = "sample"

    return Response(
        get_video_stream(topic), 
        mimetype='multipart/x-mixed-replace; boundary=frame') #mimetype = multipart/x-mixed-replace, replace any old images with new values streaming through the pipeline.


def get_video_stream(topic):
    """
    recieve streamed images from the Kafka Server and convert them to a Flask-readable format.
    """
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for msg in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + msg.value + b'\r\n\r\n')




@app.route('/text', methods=['GET'])
def text():
    topic = "topic_name"

    return Response(
        get_text_stream(topic),
        mimetype='text/html')



def get_text_stream(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for msg in consumer:
        yield(msg.value)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)