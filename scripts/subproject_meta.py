# Read and output subproject's meta information

import os
import sys
import json
import pprint
import argparse

def printmeta(meta):
    libs = meta["libraries"]
    for library in libs:
        print(f"library {library['name']}:")
        print(f"    description: {library['description']}")
        print(f"    version: {library['version']}")
        print(f"    c++ standard: {library['cpp_standard']}")
        print()

parser = argparse.ArgumentParser()
parser.add_argument("path", help = "The subproject's path")

if __name__ == "__main__":
    args = parser.parse_args()

    path = args.path

    meta = open(os.path.join(path, "meta", "libraries.json"))
    meta_data = json.load(meta)
    printmeta(meta_data)
    meta.close()