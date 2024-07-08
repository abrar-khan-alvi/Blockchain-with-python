from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-9558d4ce-6e89-40ca-ae6a-3c4c78fc77aa'
pnconfig.publish_key = 'pub-c-6d9cacdb-91fa-41b8-bbfe-9dfdfe99d03a'

pubnub = PubNub(pnconfig)
TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()

if __name__ == '__main__':
    main()
