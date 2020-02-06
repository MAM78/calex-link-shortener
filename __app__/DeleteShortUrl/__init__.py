import json
import logging
import os

from azure.cosmosdb.table.tableservice import TableService
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    def get_param(req: func.HttpRequest, param: str) -> str:
        param_value = req.params.get(param)
        if not param_value:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                param_value = req_body.get(param)
        return param_value

    path = get_param(req, "path")

    logging.info(f"Parsed the following parameters from the HTTP request: path={path}.")

    if path:
        rowKey = path
        partitionKey = "links"
        tableName = "links"

        # connect to table
        storage_account_name = os.environ["STORAGE_ACCOUNT_NAME"]
        storage_account_key = os.environ["STORAGE_ACCOUNT_KEY"]

        table_service = TableService(
            account_name=storage_account_name, account_key=storage_account_key
        )

        # try to delete the entity - if it does not exist, throw
        try:
            table_service.delete_entity(tableName, partitionKey, rowKey)
            logging.info(
                f"Deleted the following from Azure Table Storage: PartitionKey={partitionKey}, RowKey={rowKey}"
            )
            resp = {
                "Status": "Ok",
                "Message": f"Deleted the following from Azure Table Storage: PartitionKey={partitionKey}, RowKey={rowKey}",
            }
        except:
            logging.info(
                f"Skipped deletion of the following from Azure Table Storage as the entity does not exist: PartitionKey={partitionKey}, RowKey={rowKey}"
            )
            resp = {
                "Status": "Ok",
                "Message": f"Skipped deletion of the following from Azure Table Storage as it does not exist: PartitionKey={partitionKey}, RowKey={rowKey}",
            }
            pass

        resp_json = json.dumps(resp)

        return func.HttpResponse(body=resp_json, mimetype="application/json")
    else:
        resp = {
            "Status": "Error",
            "Message": "Did not delete any entities from Azure Table Storage",
        }

        resp_json = json.dumps(resp)

        return func.HttpResponse(
            body=resp_json, mimetype="application/json", status_code=400
        )
