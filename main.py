import os
import pathlib
from pythonosc.udp_client import SimpleUDPClient
import time
from audio_processing import transcribe_audio, respond
from utils import start_tunnel, stop_tunnel

# Configuration for the OSC client
osc_ip = "192.168.1.98"  # The IP of the OSC server to send messages to
osc_port = 7001  # The port of the OSC server
osc_client = SimpleUDPClient(osc_ip, osc_port)  # Create the OSC client

if __name__ == "__main__":

    start_tunnel(
        remote_server="imagination.mat.ucsb.edu",
        remote_port=11434,
        local_port=12345,
    )

    try:
        audio_path = "garble.mp3"
        result = transcribe_audio(audio_path)
        response = respond(result)

        while True:
            osc_client.send_message("/greeting", str(response))
            print(f"Call :: {result}")
            print()
            print(f"Response :: {response}")
            print()
            # print(
            #     "OSC message {} sent to {}:{}".format(str(response), osc_ip, osc_port)
            # )

            time.sleep(10)

    finally:
        stop_tunnel()
