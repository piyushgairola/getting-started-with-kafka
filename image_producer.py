import os
import sys
import time
import argparse
import cv2
from kafka import KafkaProducer



def publish_image(image_path, topic):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    for file in os.listdir(image_path):
        file_path = image_path+file
        img = cv2.imread(file_path)
        is_success, encode_img = cv2.imencode(".jpg", img)
        byte_im = encode_img.tobytes()
        
        print('publishing image...')
        producer.send(topic, byte_im)

        time.sleep(0.5)
    
    print('publish complete')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    parser.add_argument('--topic', required=True)

    args = parser.parse_args()

    publish_image(args.dir, args.topic)