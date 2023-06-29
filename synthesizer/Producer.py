from kafka import KafkaProducer

bootstrap_servers = []
topicName = 'myTopic'

producer = KafkaProducer(bootstrap_servers='localhost:1234')
ack = producer.send(topicName, b'Hello World!!!!!!!!')
metadata = ack.get()

print(metadata.topic)
print(metadata.partition)
