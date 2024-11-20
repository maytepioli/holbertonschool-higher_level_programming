#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, 'r') as a:
        deserializado = json.load(a)
        return deserializado
