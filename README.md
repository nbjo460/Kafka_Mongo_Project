[//]: # (docker run -d --name MONGODB -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=menachemYarhi --network kafkanet mongo)

[//]: # (docker build -t subscriber .)

[//]: # ()
[//]: # (docker run -d --name sub_interesting -p 8050:8050 --network kafkanet -e KAFKA_HOST=broker -e SELF_PORT=8050 -e MONGO_HOST=MONGODB -e KAFKA_TOPIC=interesting subscriber)

[//]: # (docker run -d --name sub_not_interesting -p 8051:8051 --network kafkanet -e KAFKA_HOST=broker -e SELF_PORT=8051 -e MONGO_HOST=MONGODB -e KAFKA_TOPIC=not_interesting subscriber)

[//]: # ()
[//]: # (docker build -t publisher .)

[//]: # (docker run -d --name pub -p 8020:8020 -e SELF_PORT=8020 -e KAFKA_HOST=broker --network kafkanet publisher)

## Table of contents
- [Producer](#producer)
- [Consumer Intreseting messages](#consumer_inter)
- [Consumer Not Intreseting messages](#consumer_not_inter)


## <a id="producer"></a>Introduction
Your repo introduction.

## <a id="consumer_inter"></a>Consumer Intreseting messages
- 
## <a id="consumer_not_inter"></a>Consumer Not Intreseting messages
- 
  

