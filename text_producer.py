import os
import sys
import time
from kafka import KafkaProducer
import argparse


def publish_text(file_path, topic):

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    file = open(file_path, 'rb')
    
    for line in file.readlines():
        print("publishing text...")
        producer.send(topic, line )

        
        time.sleep(0.5)

    print("Publish Completed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', required=True)
    parser.add_argument('--topic', required=True)

    args = parser.parse_args()

    publish_text(args.filepath, args.topic)