# getting-started-with-kafka

# start zookeper: 
bin/zookeeper_server_start.sh config/zookeeper.properties

# start Kafka: 
bin/kafka_server_start.sh config/server.properties

# Create a topic for Image Data: 
bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic image
# Create a topic for Text Data: 
bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic text

# Check Kafka topics: 
bin/kafka-topics.sh --list --zookeeper localhost:2181


# start the consumer: 
python consumer.py
# start the image producer:
python image_producer.py --dir=<image_dir> --topic=image
# start the text producer: 
python text_producer.py --filepath=<file_path> --topic=text
