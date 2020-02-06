# calex-link-shortener

Azure Functions link shortener for `calex.dev`

[![Build Status](https://dev.azure.com/curtisalexander/calex-link-shortener/_apis/build/status/curtisalexander.calex-link-shortener?branchName=master)](https://dev.azure.com/curtisalexander/calex-link-shortener/_build/latest?definitionId=6&branchName=master)

## Requirements

### Local

Requires the following environment variables be set within `local.settings.json`.

- `BASE_URL` = Base url (e.g. `https://links.mydomain.com`) used to create the short url (e.g. `https://links.mydomain.com/a`)
- `STORAGE_ACCOUNT_NAME` = Azure storage account name where the Azure table will be stored
- `STORAGE_ACCOUNT_KEY` = Azure storage account key where the Azure table will be stored

### Azure

Requires the following environment variables be set within the Azure Function Application settings.

- `BASE_URL` = Base url (e.g. `https://links.mydomain.com`) used to create the short url (e.g. `https://links.mydomain.com/a`)
- `STORAGE_ACCOUNT_NAME` = Azure storage account name where the Azure table will be stored
- `STORAGE_ACCOUNT_KEY` = Azure storage account key where the Azure table will be stored

## Client

There is a simple Python client within the `client` directory that can be used to call the `WriteShortUrl` and `GetAllUrls` Azure Functions.

The following environment variable must be set locally.

- `AZURE_WRITESHORTURL_URL` = Azure Function url
- `AZURE_GETALLURLS_URL` = Azure Function url

```sh
python main.py g https://www.google.com
```

## Inspiration

- [Build a Serverless Link Shortener with Analytics Faster than Finishing your Latte](https://blog.jeremylikness.com/blog/2017-09-04_build-a-serverless-link-shortener-with-analytics-faster-than-finishing-your-latte/)
- [Azure Functions: Less-Server and More Code](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Azure-Functions-Less-Server-and-More-Code?utm_source=jeliknes&utm_medium=blog&utm_campaign=linkshortener&WT.mc_id=linkshortener-blog-jeliknes)
