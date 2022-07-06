#-*- coding: utf-8 -*-
__author__ = "Hiral shah (Srce Cde)"
__license__ = "MIT"
__email__ = "hiralshah11199@gmail.com"
__maintainer__ = "Hiral Shah (Srce Cde)"

import json
import requests

def handler(event, context):

    # TODO implementation
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Lambda Container image invoked!",
                            "event": event})
    }
