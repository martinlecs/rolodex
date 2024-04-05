## Documentation

### Sypnosis

`cli [filenames...] [option...]`

### Options

The cli tool accepts the following command line arguments.

`filenames`: Specifies the location of a csv or json file. Multiple file names can be passed in at once.

`-a`,
`--add_record`: Adds a new record to the currently loaded dataset. Records must be a tuple in the form "name,address,phone_number". Spaces are allowed as long as the tuple is wrapped in quotations, however, commas are used as delimiters so do not add extraneous ones. You can define as many new records as you want in a single command.

`-f`,
`--filter`: Applies a filter over the dataset, on a specific field. This argument must have the form "field=pattern" where "field" represents one of [name, address, phone_number] and "pattern" is a Unix-like glob pattern thats supported by [fnmatch](https://docs.python.org/3/library/fnmatch.html). You can define as many filters as you want in a single command.

`-o`,
`--output`: Specifies the output location to write a file to. We currently only support outputting to CSV or JSON formats. The script will detect if you want to write to a csv if ".csv" is the output file location and likewise a json file will be created if ".json" is specified in the output location.

`-d`
`--display`: Select how you want your results to be displayed to the screen. If no output is specified, then the script will automatically print JSON to the screen. If output is specified, then nothing will be displayed to the screen. There are two display options: [json, table]

### Option order processing

The ordering of the options do not matter as options will always be processed in the following order:

1. Load files
2. Add records
3. Apply filters
4. Create outputs
5. Display to screen
