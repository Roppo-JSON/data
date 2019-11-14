import json
import glob

from jsonschema import validate, ValidationError


def main():

    with open('schema.json', 'r') as schema_file:
        json_schema = json.load(schema_file)

    for file_name in glob.glob('dist/*'):

        with open(file_name, 'r') as data_file:
            data = json.load(data_file)

        try:
            print('Validating:', file_name)
            validate(data, json_schema)
        except ValidationError as error:
            print(error.message)

    print('Finished')


if __name__ == "__main__":
    main()
