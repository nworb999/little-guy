from pythonosc.udp_client import SimpleUDPClient
import time
import tensorflow as tf
import numpy as np

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

print("Model defined!")

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

print ("Model compiled!")

# Provide some sample data (inputs and expected outputs)
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Train the model
model.fit(xs, ys, epochs=500, verbose=0)

value = 10.0

result = model.predict([value])

# Configuration for the OSC client
osc_ip = "192.168.1.98"  # The IP of the OSC server to send messages to
osc_port = 7001  # The port of the OSC server
osc_client = SimpleUDPClient(osc_ip, osc_port)  # Create the OSC client

while True:
    # Send an OSC message with a string "hello"
    osc_client.send_message("/greeting", str(result))
    print("OSC message {} sent to {}:{}".format(str(result), osc_ip, osc_port))
    
    result = model.predict([value + 10.0])
    print(str(result))
    # Wait for 10 seconds before sending the next message
    time.sleep(10)
