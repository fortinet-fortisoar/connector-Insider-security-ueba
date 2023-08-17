""" Copyright start
Copyright (C) 2008 - 2023 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """
from .make_rest_api_call import MakeRestApiCall
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger("insider-security-ueba")

def get_alerts_by_id(config: dict, params: dict) -> dict:
    endpoint = "/api/token/alerts"
    method = "GET"
    params.update({"action": "get_meta"})

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def search_alerts(config: dict, params: dict) -> dict:
    endpoint = "/api/token/alerts"
    method = "GET"
    params.update({"action": "search_alert"})

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def search_data_enrichment(config: dict, params: dict) -> dict:
    endpoint = "/api/token/alerts"
    method = "GET"

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


operations = {
    "get_alerts_by_id": get_alerts_by_id,
    "search_data_enrichment": search_data_enrichment,
    "search_alerts": search_alerts
}
