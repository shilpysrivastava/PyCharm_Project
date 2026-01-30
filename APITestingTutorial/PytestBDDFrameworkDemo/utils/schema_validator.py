from jsonschema import validate
from jsonschema.exceptions import ValidationError

def validate_json_schema(response,schema):
    """
      Validate API response against JSON schema
      """
    try:
        validate(instance = response.json(), schema = schema)
    except ValidationError as e:
        assert False, e.message

