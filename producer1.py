from kafka import KafkaProducer
import snscrape.modules.twitter as sntwitter
import pandas as pd

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
query = "(from:*) until:2022-01-01 since:2020-01-01"
tweets = []
limit = 55
i=1
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        print("tweet",i)
        ack = producer.send(topicName, bytes(str(tweet.content), 'utf-8'))
        metadata = ack.get()
        i=i+1

    
    


 