# Get_IReL_Agreement_Titles
Gets a sortable html table of Journal Titles from any of the IReL subscribing institutions

This script downloads a CSV file from a specified URL and converts it into an HTML table. The CSV data used in this script is specific to an Irish Research eLibrary (IReL) list of journals.

## Features

- Download CSV file directly from a specified URL
- Filter rows based on a specified column
- Output the HTML table to a file
- Customizable ID and class attributes for the table and table header
- Display the current date, time, and filter parameter used at the top of the output
- Count the number of rows in the table

## Usage

The script requires one command-line argument which is the column to filter by. This should be one of the following values:

`ATU`, `DCU`, `DKIT`, `IADT`, `MIC`, `MTU`, `MU`, `RCSI`, `SETU`, `TCD`, `Teagasc`, `TU Dublin`, `TUS`, `UCC`, `UCD`, `UG`, `UL`

If you do not want to filter the data, you can use `ALL` as the argument.

Example usage:

```bash
python script.py ALL
```

The above command will convert the entire CSV data into an HTML table.

## Dependencies

This script requires the following Python modules:

- csv
- pandas
- argparse
- requests
- datetime

These can be installed using pip:

```bash
pip install pandas requests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

--- 

Feel free to modify the README to suit your project's needs.
