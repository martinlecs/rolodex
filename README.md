<a name="readme-top"></a>

## Disclaimer

This is an MMVP. This project represents the bare minimum to get something up and running in the least amount of time possible.

Further improvements include:

- Proper input validation
- More robust error handling
- Toggleable debug logging
- Better documentation accessible within the CLI prompt
- Automated CI and tag creation for distribution

This tool is very easy to break if you go outside the happy path! Use at your own peril!

## Setting up

This project was built for python3.9 but should work just fine with later versions of python3.

Since this project was built using [Poetry](https://python-poetry.org/), I would recommend you use that if you have that installed. Otherwise I've generated a `requirements.txt` that you can use with most package installers.

#### With Poetry

1. Install [Poetry](https://python-poetry.org/)
2. Install [poetry-exec-plugin](https://github.com/keattang/poetry-exec-plugin) with the command: `poetry self add poetry-exec-plugin`
3. Run `poetry install`. Poetry will automatically create a venv and install your dependencies into it.

#### With Pip

1. Create new venv
2. Run
   `pip install -r requirements.txt`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Load a file, filter for names that match the glob pattern `*3` and then export the result to json:

```sh
python3 -m rolodex.cli tests/integration/data/test1.csv -f "name=*3" -o output.json
```

Load multiple files, apply multiple filters, add a record, create an output, and then display the results to the screen as a table:

```sh
python3 -m rolodex.cli tests/integration/data/test1.csv tests/integration/data/test2.json -a "Martin,this is my address,111000111" -f "name=Martin*" -f "address=*Sydney*" -o output.csv -d table
```

_For more information, please refer to the [Documentation](./DOCUMENTATION.md)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
