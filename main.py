import os
import pathlib
from pythonosc.udp_client import SimpleUDPClient
import time
from audio_processing import transcribe_audio, respond

# Configuration for the OSC client
osc_ip = "192.168.1.98"  # The IP of the OSC server to send messages to
osc_port = 7001  # The port of the OSC server
osc_client = SimpleUDPClient(osc_ip, osc_port)  # Create the OSC client

if __name__ == "__main__":

  audio_path = "garble.mp3"
  result = transcribe_audio(audio_path)
  response = respond(result)

  while True:
    # Send an OSC message with a string "hello"
    osc_client.send_message("/greeting", str(response))
    print("OSC message {} sent to {}:{}".format(str(response), osc_ip, osc_port))

    # Wait for 10 seconds before sending the next message
    time.sleep(10)


