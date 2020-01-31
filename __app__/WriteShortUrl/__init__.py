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
    longUrl = get_param(req, "longurl")

    logging.info(
        f"Parsed the following parameters from the HTTP request: path={path}, longurl={longUrl}."
    )

    if path and longUrl:
        rowKey = path
        baseUrl = os.environ["BASE_URL"]
        shortUrl = f"{baseUrl}/{path}"

        data = {
            "PartitionKey": "links",
            "RowKey": rowKey,
            "ShortUrl": shortUrl,
            "LongUrl": longUrl,
        }

        # connect to table
        storage_account_name = os.environ["STORAGE_ACCOUNT_NAME"]
        storage_account_key = os.environ["STORAGE_ACCOUNT_KEY"]

        table_service = TableService(
            account_name=storage_account_name, account_key=storage_account_key
        )

        # write to table
        table_service.insert_or_replace_entity("links", data)

        logging.info(
            f"Wrote the following to Azure Table Storage: PartitionKey={data['PartitionKey']}, RowKey={data['RowKey']}, ShortUrl={data['ShortUrl']}, LongUrl={data['LongUrl']}"
        )

        resp = {
            "Status": "Ok",
            "Message": f"Wrote the following to Azure Table Storage: PartitionKey={data['PartitionKey']}, RowKey={data['RowKey']}, ShortUrl={data['ShortUrl']}, LongUrl={data['LongUrl']}",
        }
        resp_json = json.dumps(resp)

        return func.HttpResponse(body=resp_json, mimetype="application/json")
    else:
        resp = {
            "Status": "Error",
            "Message": "Did not write any links to Azure Table Storage",
        }
        resp_json = json.dumps(resp)
        return func.HttpResponse(
            body=resp_json, mimetype="application/json", status_code=400
        )
