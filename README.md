# getting-started-with-kafka

Steps to follow.

1. start zookeper: 
bin/zookeeper_server_start.sh config/zookeeper.properties

2. start Kafka: 
bin/kafka_server_start.sh config/server.properties

3. Create a topic for Image Data: 
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication_factor 1 --partiton 1 --topic image

4. Create a topic for Text Data: 
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication_factor 1 --partiton 1 --topic text

5. Check Kafka topics: 
bin/kafka-topics.sh --list --zookeeper localhost:2181


6. start the consumer: 
python consumer.py
7. start the image producer:
python image_producer.py --dir=<image_dir> --topic=image
8. start the text producer: 
python text_producer.py --filepath=<file_path> --topic=text

To view the output:
open "0.0.0.0:5000" in browser.
for consuming images enter: 0.0.0.0:5000/image
for consuming text enter: 0.0.0.0:5000/text
