import tensorflow as tf
from tensorflow.keras.layers import (
    Dense, Flatten, Conv2D
)
import numpy as np
import datetime
from tensorflow.keras import Model
from tensorflow.keras import LSTM
"""
Please do not mind the incompleteness or if something kinda seems wrong, I am currently reviewing the paper
and will update the work soon. TF 2.0 makes this process a whole lot easier.
"""


class NTM(Model):
    def __init__(self, memory, input, numread, numwrite):
        super(NTM, self).__init__(name='')
        self.read_heads = read_heads(numread, memory)
        self.write_heads = write_heads(numwrite, memory)
        self.content_address = content_address(memory, ...) #these will probably be functions
        self.location_address = location_address(memory, ...) #these will probably be functions
        self.controller_network = LSTM(input)

    def call(self, ... list of parameters here for the various missing parts ):
        ...
        ## basically everytime the NTM is called, the memory bank is passed through it again and
        ##the model then gets called to train. If Memory bank is set to untrainable, as in the tf tutorials and should be fine.

    def predict():
        ...
        #predicts based on input sequence or something

class read_heads(object):
    def __init__(self, num_heads, memory):
        self.num_heads = num_heads
        self.memory = memory

    def read():
        print("READ")


class write_heads(object):
    def __init__(self, num_heads, memory):
        self.num_heads = num_heads
        self.memory = memory

    def write_heads():
        print("WRITE")
