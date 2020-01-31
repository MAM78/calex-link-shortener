import json
import logging
import os

from azure.cosmosdb.table.tableservice import TableService
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")


    # connect to table
    storage_account_name = os.environ["STORAGE_ACCOUNT_NAME"]
    storage_account_key = os.environ["STORAGE_ACCOUNT_KEY"]

    table_service = TableService(
        account_name=storage_account_name, account_key=storage_account_key
    )

    # get all rows
    rows = table_service.query_entities("links")

    data = { "links": [] }

    for row in rows:
        _data = {
            "PartitionKey": row.PartitionKey
            "RowKey": row.RowKey,
            "ShortUrl": row.ShortUrl,
            "LongUrl": row.LongUrl,
        }
        
        data["links"].append(_data)

    ret_json = json.dumps(data)

    return func.HttpResponse(body=ret_json, mimetype="application/json")