""" Copyright start
Copyright (C) 2008 - 2023 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """
from .make_rest_api_call import MakeRestApiCall
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger("Insider-security-ueba")

def get_alerts(config: dict, params: dict) -> dict:
    endpoint = "/api/token/alerts"
    method = "GET"

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def data_enrichment(config: dict, params: dict) -> dict:
    endpoint = "/api/token/alerts"
    method = "GET"

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


operations = {
    "get_alerts": get_alerts,
    "data_enrichment": data_enrichment
}
