import os
import pathlib

import numpy as np
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import models

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

DATASET_PATH = 'data/mini_speech_commands'

data_dir = pathlib.Path(DATASET_PATH)
if not data_dir.exists():
  tf.keras.utils.get_file(
      'mini_speech_commands.zip',
      origin="http://storage.googleapis.com/download.tensorflow.org/data/mini_speech_commands.zip",
      extract=True,
      cache_dir='.', cache_subdir='data')
  
commands = np.array(tf.io.gfile.listdir(str(data_dir)))
commands = commands[(commands != 'README.md') & (commands != '.DS_Store')]
print('Commands:', commands)

train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
    directory=data_dir,
    batch_size=64,
    validation_split=0.2,
    seed=0,
    output_sequence_length=16000,
    subset='both')

label_names = np.array(train_ds.class_names)
print()
print("label names:", label_names)

def squeeze(audio, labels):
  audio = tf.squeeze(audio, axis=-1)
  return audio, labels

train_ds = train_ds.map(squeeze, tf.data.AUTOTUNE)
val_ds = val_ds.map(squeeze, tf.data.AUTOTUNE)

test_ds = val_ds.shard(num_shards=2, index=0)
val_ds = val_ds.shard(num_shards=2, index=1)

for example_audio, example_labels in train_ds.take(1):  
  print(example_audio.shape)
  print(example_labels.shape)

label_names[[1,1,3,0]]











# from pythonosc.udp_client import SimpleUDPClient
# import time
# import tensorflow as tf
# import tensorflow
# import numpy as np

# # Define the model
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(units=1, input_shape=[1])
# ])

# print("Model defined!")

# # Compile the model
# model.compile(optimizer='sgd', loss='mean_squared_error')

# print ("Model compiled!")

# # Provide some sample data (inputs and expected outputs)
# xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# # Train the model
# model.fit(xs, ys, epochs=500, verbose=0)

# value = 10.0

# result = model.predict([value])

# # Configuration for the OSC client
# osc_ip = "192.168.1.98"  # The IP of the OSC server to send messages to
# osc_port = 7001  # The port of the OSC server
# osc_client = SimpleUDPClient(osc_ip, osc_port)  # Create the OSC client

# while True:
#     # Send an OSC message with a string "hello"
#     osc_client.send_message("/greeting", str(result))
#     print("OSC message {} sent to {}:{}".format(str(result), osc_ip, osc_port))
    
#     result = model.predict([value + 10.0])
#     print(str(result))
#     # Wait for 10 seconds before sending the next message
#     time.sleep(10)
