"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        neos_arr = []
        reader = csv.DictReader(infile)

        for row in reader:
            if row["name"]:
                name = row["name"]
            else:
                name = None
            if row["diameter"]:
                diameter = float(row["diameter"])
            else:
                diameter = float('nan')
            if row["pha"] == "Y":
                hazardous = True
            else:
                hazardous = False
            neos_arr.append(NearEarthObject(row['pdes'], name=name, diameter=diameter, hazardous=hazardous))
    return neos_arr


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        out_arr = []
        contents = json.load(infile)
        header = contents['fields']
        # out_arr.append(header)
        for approach in contents['data']:
            if approach[4]:
                distance = float(approach[4])
            else:
                distance = float('nan')
            if approach[7]:
                velocity = float(approach[7])
            else:
                velocity = float('nan')
            out_arr.append(CloseApproach(approach[3], distance=distance,
                                         velocity=velocity, designation=str(approach[0])))

    return out_arr
