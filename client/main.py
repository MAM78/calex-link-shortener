import emoji
import json
import requests
import os
import typer

import utils

from pprint import pprint


app = typer.Typer()


@app.command()
def write(path: str, longurl: str) -> None:
    """
    Write an entry into Azure Table Storage that can be used to map a URL path to a longer url.

    Ultimately, the entries within the Azure Table are used for link shortening.
    """

    # validation & setup
    utils.validate_url(longurl)
    azure_full_url = utils.create_azure_url(
        "AZURE_WRITESHORTURL_URL", path, longurl=longurl
    )

    # GET request
    try:
        r = requests.get(azure_full_url)
    except:
        print(emoji.emojize(":x:  ", use_aliases=True), end="", flush=True)
        typer.echo("Something went wrong when submitting GET request!")
        raise typer.Exit(-1)

    # write result
    utils.print_response_status(r)


@app.command()
def get() -> None:
    """
    Retrieve all entries from Azure Table Storage.
    """

    azure_url: str = os.getenv("AZURE_GETALLURLS_URL")

    # GET request
    try:
        r = requests.get(azure_url)
    except:
        print(emoji.emojize(":x:  ", use_aliases=True), end="", flush=True)
        typer.echo("Something went wrong when submitting GET request!")
        raise typer.Exit(-1)

    # write status
    utils.print_response_status(r)

    # print json
    pprint(r.json())


@app.command()
def delete(path: str) -> None:
    """
    Delete an entry from Azure Table Storage.
    """

    azure_full_url = utils.create_azure_url("AZURE_WRITESHORTURL_URL", path)

    # GET request
    try:
        r = requests.get(azure_full_url)
    except:
        print(emoji.emojize(":x:  ", use_aliases=True), end="", flush=True)
        typer.echo("Something went wrong when submitting GET request!")
        raise typer.Exit(-1)

    # write result
    utils.print_response_status(r)


if __name__ == "__main__":
    app()
