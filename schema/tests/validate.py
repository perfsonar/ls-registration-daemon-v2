from jsonschema import validate
import json
with open('schema.json') as file:
    schema = json.load(file)

#test data
with open('tests/interface.json') as file:
    record = json.load(file)

#validate
try:
    validate(instance=record, schema=schema)
    print('Validated')
except Exception as e:
    print(e)