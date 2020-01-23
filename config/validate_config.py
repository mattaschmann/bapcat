import json
import jsonschema
import urllib.request

from jsonschema import validate

# TODO: Change to deployed location of bapcat once that happens
BAPCAT_CONFIG_SCHEMA_URL = "http://localhost:5000/bapcat-config-schema.json"

with open("./config.json") as config_data:
    config = json.load(config_data)

    with urllib.request.urlopen(BAPCAT_CONFIG_SCHEMA_URL) as schema_data:
        schema = json.load(schema_data)

        try:
            validate(config, schema)
            print("\nConfig is Valid!")
        except jsonschema.exceptions.ValidationError as ve:
            print("\nConfig is invalid!\n")
            print(ve)
