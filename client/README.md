# client

### Requirements

The following environment variable must be set locally.

- `AZURE_WRITESHORTURL_URL` = Azure Function url
- `AZURE_GETALLURLS_URL` = Azure Function url
- `AZURE_DELETESHORTURL_URL` = Azure Function url

### Run

There are three subcommands that can be run:

- Write a short url into Azure Table Storage
- Get all entries from Azure Table Storage.
- Delete a short url from Azure Table Storage

#### `WriteShortUrl`

```sh
python main.py write g https://www.google.com
```

#### `GetAllUrls`

```sh
python main.py get
```

#### 'DeleteShortUrl`

```sh
python main.py delete g
```

### Help

To get help, run the following.

```sh
python main.py --help
```

Alternatively, run help for a specific subcommand.

```sh
python main.py write --help
```

```sh
python main.py get --help
```

```sh
python main.py delete --help
```

### Built with

Built using [Typer](https://typer.tiangolo.com/).
