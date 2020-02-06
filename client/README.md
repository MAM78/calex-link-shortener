# client

### Requirements

The following environment variable must be set locally.

- `AZURE_WRITESHORTURL_URL` = Azure Function url

### Run

There are two subcommands that can be run &mdash; one to write a short url into Azure Table Storage. The other will return all entries in the Azure Table Storage.

#### `WriteShortUrl`

```sh
python main.py write g https://www.google.com
```

#### `GetAllUrls`

```
python main.py get
```

### Help

To get help, run the following.

```
python main.py --help
```

Alternatively, run help for a specific subcommand.

```
python main.py write --help
```

```
python main.py get --help
```

### Built with

Built using [Typer](https://typer.tiangolo.com/).
