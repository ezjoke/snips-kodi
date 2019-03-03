#!/usr/bin/env python2
# coding: utf-8

from hermes_python.hermes import Hermes
from hermes_python.ontology import *

HOST_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(HOST_ADDR, str(MQTT_PORT))

class KodiAssistant(object):
    def __init__(self):
        # start listening to MQTT
        self.start_blocking()

    def turn_on_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "J'ai allumé la télé")

    def turn_off_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        print '[Received] intent: {}'.format(intent_message.intent.intent_name)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "J'ai allumé la télé")

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
	    if coming_intent  == 'TurnOn':
            self.turn_on_callback(hermes, intent_message)

	    elif coming_intent == 'TurnOff':
            self.turn_off_callback(hermes, intent_message)

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    KodiAssistant()
