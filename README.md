# CSV Batch Splitter

This Python script splits a CSV file into smaller batches of specified sizes. It generates new CSV files with a naming convention that includes the original file name and the batch number.

## Features

- Accepts a CSV file as input.
- Allows the user to specify the batch size (default is 100 records).
- Includes column names in each output batch.

## Prerequisites

- Python 3.x
- [Pandas](https://pandas.pydata.org/) library

## Installation

1. Clone this repository or download the script file.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python library if you haven't already:

   ```bash
   pip install pandas
   ```

## Usage

To use the script, run it from the command line with the following syntax:

```bash
python split_csv.py <input_file.csv> [<batch_size>]
```

### Parameters

- `<input_file.csv>`: The path to the CSV file you want to split.
- `[<batch_size>]`: (Optional) The number of records per batch. If not provided, the default batch size is 100.

### Example

1. To split a CSV file named `my_file.csv` into batches of 100 records:

   ```bash
   python split_csv.py my_file.csv
   ```

2. To split the same file into batches of 50 records:

   ```bash
   python split_csv.py my_file.csv 50
   ```

## Output

The output files will be named in the following format:

```
<original_file_name>_<batch_number>.csv
```

For example, if the input file is `my_file.csv`, the output files will be:

- `my_file_0001.csv`
- `my_file_0002.csv`
- ...

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.