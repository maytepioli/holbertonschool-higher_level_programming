#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(cvs_filename):
    fjson = 'data.json'
    try:
        with open(cvs_filename, 'r') as fcsv:
            csvread = csv.DictReader(fcsv)
            data = list(csvread)
        with open(fjson, 'w') as ff:
            json.dump(data, ff)
        return True
    except FileNotFoundError:
        return False
