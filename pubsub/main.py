# push implementation

# terminal
# export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()

# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"
project_id = 'foo'
topic_id = 'foo'
# To create a topic
topic_path = publisher.topic_path(project_id, topic_id)
topic = publisher.create_topic(request={"name": topic_path})

# To send message to a topic
topic_name = f'projects/{project_id}/topics/{topic}'
data = 'May the force be with you, aways'
future = publisher.publish(topic_name, data, spam='eggs')
future.result()