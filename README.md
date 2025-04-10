# Pubmed_API_Projects


```markdown
# PubMed API Paper Fetcher

A command-line tool for fetching PubMed research papers based on user-defined queries. The tool retrieves papers with non-academic authors affiliated with pharmaceutical or biotech companies and exports the results to a CSV file.

## Features

- Search PubMed for papers using any query (supports PubMed query syntax).
- Extract paper details including title, publication date, non-academic authors, company affiliations, and corresponding author email.
- Output the results to the console or save them to a CSV file.
- Print debug information for troubleshooting.

## Requirements

- Python 3.9+
- `biopython` package

### Dependencies

The dependencies are managed using **Poetry**. To install dependencies, you need to have **Poetry** installed on your machine. See the installation guide below.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mrinalpy20/Pubmed_API_Projects.git
   cd Pubmed_API_Projects
   ```

2. Install dependencies using **Poetry**:

   If you haven't installed Poetry yet, follow the instructions [here](https://python-poetry.org/docs/#installation).

   Once Poetry is installed, run:

   ```bash
   poetry install
   ```

## Usage

To search for papers, run the following command:

```bash
poetry run get-papers-list "your-search-query"
```

### Options:
- `-h` or `--help`: Show the usage instructions.
- `-d` or `--debug`: Print debug information during execution.
- `-f` or `--file`: Specify the filename to save the results. If not provided, the results are printed to the console.

### Examples:

1. **Search for papers on cancer immunotherapy**:

   ```bash
   poetry run get-papers-list "cancer immunotherapy"
   ```

2. **Search for papers on vaccine development with debug info**:

   ```bash
   poetry run get-papers-list "vaccine development" --debug
   ```

3. **Save results to a CSV file**:

   ```bash
   poetry run get-papers-list "clinical trials" --file results.csv
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Mrinal Kalita (mrinalk1361@gmail.com)
```

---

### Customization:

- You can edit the project name, description, and examples as needed based on any changes you make to the project.
- If you want to add other sections like "Contributing," "Acknowledgements," or "Future Work," feel free to customize it.
- ChatGPT and PubMed API documentation was used to as external tools for this project

