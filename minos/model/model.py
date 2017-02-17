'''
Created on Feb 8, 2017

@author: julien
'''


class Layout(object):

    def __init__(self, input_size, output_size,
                 output_activation, block=None, block_input=None, rows=None):
        self.input_size = input_size
        self.output_size = output_size
        self.output_activation = output_activation
        self.block = block
        self.block_input = block_input
        self.rows = rows or list()

    def get_rows(self):
        return self.rows

    def get_blocks(self):
        return [
            block
            for row in self.rows
            for block in row.get_blocks()]

    def get_layers(self):
        return [
            layer
            for row in self.rows
            for layer in row.get_layers()]


class Row(object):

    def __init__(self, blocks=None):
        self.blocks = blocks or list()

    def get_blocks(self):
        return self.blocks

    def get_layers(self):
        return [
            layer
            for block in self.blocks
            for layer in block.get_layers()]


class Block(object):

    def __init__(self, layers=None):
        self.layers = layers or list()

    def get_layers(self):
        return self.layers


class Layer(object):

    def __init__(self, layer_type, parameters=None):
        self.layer_type = layer_type
        self.parameters = parameters or dict()


class Metric(object):

    def __init__(self, metric):
        self.metric = metric


class Objective(object):

    def __init__(self, objective):
        self.objective = objective


class Optimizer(object):

    def __init__(self, optimizer=None, parameters=None):
        self.optimizer = optimizer
        self.parameters = parameters or dict()