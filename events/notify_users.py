import json
import base64

def pubsub_notify(event, context):
    """
    Cloud Function triggered by Pub/Sub.
    This function is triggered whenever a message is published to a Pub/Sub topic.
    """
    # Decode the Pub/Sub message
    message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    
    # Log the received message
    print(f"Received message: {message}")

    # You can now process the message here, for example:
    event_id = message.get('event_id')
    notification_message = message.get('message', 'No message provided')
    
    # Perform actions, like sending notifications, storing info, etc.
    print(f"Event ID: {event_id}")
    print(f"Notification message: {notification_message}")
