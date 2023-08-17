""" Copyright start
Copyright (C) 2008 - 2023 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """
import datetime

from .make_rest_api_call import MakeRestApiCall
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger("insider-security-ueba")

def get_alerts_by_id(config: dict, params: dict) -> dict:
    params=_build_payload(params)
    endpoint = "/api/token/alerts"
    method = "GET"
    params.update({"action": "get_meta"})

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def search_alerts(config: dict, params: dict) -> dict:
    params=_build_payload(params)
    endpoint = "/api/token/alerts"
    method = "GET"
    params.update({"action": "search_alert"})
    params = _time_to_epoch(params, ["time_end"])

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def search_data_enrichment(config: dict, params: dict) -> dict:
    params=_build_payload(params)
    endpoint = "/api/token/alerts"
    method = "GET"
    params = _time_to_epoch(params, ["time_start", "time_end"])

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def _build_payload(params):
    return {key: val for key, val in params.items() if val is not None and val != ''}

def _time_to_epoch(params:dict, params_list:list):
    for p in params_list:
        if params.get(p) is not None:
            temp_date = datetime.datetime.strptime(params.get(p), "%Y-%m-%dT%H:%M:%S.%fZ")
            params.update({p: temp_date.timestamp()})

    return params

operations = {
    "get_alerts_by_id": get_alerts_by_id,
    "search_data_enrichment": search_data_enrichment,
    "search_alerts": search_alerts
}
