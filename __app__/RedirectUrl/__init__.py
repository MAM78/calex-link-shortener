import json
import logging
import os

from azure.cosmosdb.table.tableservice import TableService
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    path = req.route_params.get("path")
    if path is None:
        return func.HttpResponse(
            body=f"The url requested does not exist!", status_code=400
        )
    else:

        # connect to table
        storage_account_name = os.environ["STORAGE_ACCOUNT_NAME"]
        storage_account_key = os.environ["STORAGE_ACCOUNT_KEY"]

        table_service = TableService(
            account_name=storage_account_name, account_key=storage_account_key
        )

        # get longurl
        try:
            row = table_service.get_entity("links", "links", path)
        except:
            return func.HttpResponse(
                body=f"The url requested - {path} - does not exist!", status_code=400
            )
        else:
            longurl = row["LongUrl"]

            return func.HttpResponse(headers={"location": longurl}, status_code=302)
