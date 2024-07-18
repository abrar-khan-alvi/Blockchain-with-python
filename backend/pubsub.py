import time
import uuid
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-9558d4ce-6e89-40ca-ae6a-3c4c78fc77aa'
pnconfig.publish_key = 'pub-c-6d9cacdb-91fa-41b8-bbfe-9dfdfe99d03a'
pnconfig.uuid = str(uuid.uuid4()) 


TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')



class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides Communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub=PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self,channel,message):
        """
        Publish the message object to the channel.
        """ 
        self.pubnub.publish().channel(TEST_CHANNEL).message(message).sync() # Use self.pubnub here
def main():
    pubsub = PubSub()

    time.sleep(1)
    pubsub.publish(TEST_CHANNEL,{'foo':'bar'})
    

if __name__ == '__main__':
    main()