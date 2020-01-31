# client

### Requirements

The following environment variable must be set locally.

- `AZURE_WRITESHORTURL_URL` = Azure Function url

### Run

Run the client to execute the `WriteShortUrl` Azure Function.

```
python main.py g https://www.google.com
```

### Help

To get help, run the following.

```
python main.py --help
```

### Built with

Built using [Typer](https://typer.tiangolo.com/).
