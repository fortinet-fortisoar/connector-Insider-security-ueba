""" Copyright start
Copyright (C) 2008 - 2023 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """
from .make_rest_api_call import MakeRestApiCall


def _check_health(config: dict) -> bool:
    try:
        endpoint = "/api/token/alerts"
        method = "GET"
        params = {"index": "*", "limit": "5"}
        MS = MakeRestApiCall(config=config)
        MS.make_request(endpoint=endpoint, method=method,params=params)
        return True
    except Exception as e:
        raise Exception(e)