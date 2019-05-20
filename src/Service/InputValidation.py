from jsonschema import validate


def verification_input(input_value):
    """
    validate input return verification result
    """
    schema = {
        "type": "object",
        "required": ["userId","bankName","fileName","file"],
        "properties": {
            "userId":{"type":"string","minLenght":1},
            "bankName":{"type":"string","minLength":1},
            "fileName":{"type":"string","minLength":1},
            "file":{"type":"string","minLength":1},
            "password":{"type":"string"}
        },
    }
    try:
        return validate(instance=input_value, schema=schema)
    except Exception as e:
        return e.message
