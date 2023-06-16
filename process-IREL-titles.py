import csv
import pandas as pd
import argparse
import requests
from datetime import datetime

# Define the URL
url = "https://docs.google.com/spreadsheets/d/1l8jbDcYkSjmXIWkiJoOpOlSC-9bS4JmnU8-JX3LlGt0/export?format=csv&gid=0"

# Download the CSV data from the URL
response = requests.get(url)
input_data_lines = response.content.decode('utf-8').splitlines()

# -------------------------


# Parse command-line argument
parser = argparse.ArgumentParser()
parser.add_argument('column', help='The column to filter by')
args = parser.parse_args()

# Define a flag to indicate when we've found the start of the CSV data
found_start = False

# Find the line where CSV data starts
for i, line in enumerate(input_data_lines):
    if line.strip() == 'Journal title,e-ISSN,ISSN,Publisher ,Further information,Journal notes,Agreement notes,ATU,DCU,DKIT,IADT,MIC,MTU,MU,RCSI,SETU,TCD,Teagasc,TU Dublin,TUS,UCC,UCD,UG,UL':
        found_start = True
        start_line = i
        break

if found_start:
    # Read the lines from the start of the CSV data into a CSV reader
    # data_lines = lines[start_line:]
    # data = csv.reader(input_data_lines)

    # Read the lines from the start of the CSV data into a CSV reader
    data = csv.reader(input_data_lines[start_line:])

    # Convert the CSV reader into a pandas DataFrame
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]  # Set DataFrame columns using first row
    df = df[1:]  # Remove first row

    # Check if we need to filter the data
    if args.column != 'ALL':
        df = df[df[args.column] != 'N']

    # Only keep specified columns
    df = df[['Journal title', 'e-ISSN', 'ISSN', 'Publisher ']]

    # Get the number of rows
    num_rows = len(df)

    # Convert DataFrame to HTML table and add ID and class attributes
    table_html = df.to_html(index=False, header=True, table_id='myTable')
    table_html = table_html.replace('<tr style="text-align: right;">', '<tr class="header" style="text-align: right;">', 1)

    # Read the header and footer HTML files
    with open('./header.html', 'r') as f:
        header_html = f.read()
    with open('./footer.html', 'r') as f:
        footer_html = f.read()

    # Get current date
    current_date = datetime.now().strftime('%B %d, %Y, %H:%M')

    # Write the header, table, and footer to the output HTML file
    with open('IREL-Journals.html', 'w') as f:
        f.write(header_html)
        f.write('<h1>Approved List of Journals for APC Waiver Under IReL Agreement for {}</h1>\n'.format(args.column)) 
        f.write(f'<p><em>This file was created on {current_date}.</em></p>')
        f.write('<div id="notice">\n')
        f.write('<p>The data is derived from the IReL database <a href="https://docs.google.com/spreadsheets/d/1l8jbDcYkSjmXIWkiJoOpOlSC-9bS4JmnU8-JX3LlGt0/edit#gid=0" target="_blank">here</a>.  Please note that the number of titles is subject to change at the discretion of the publishers.  For the most up to date information consult the IReL spreadsheet, or contact <a href="mailto:david.kane@setu.ie">David Kane</a> in the library for a more recent version of this file and for any other specific queries.</p>\n'.format(args.column))
        f.write('<ul>')
        f.write('<li>Current number of eligible journal titles: <strong>{}</strong></li>\n'.format(num_rows))
        f.write('<li>Corresponding authors affiliated with participating IReL member institutions can publish articles open access at no cost in these journals</li>')
        f.write('<li>The list will be updated periodically as publishers may add or remove journals from their lists during an agreement</li>')
        f.write('<li>Corresponding authors must be a current staff or student at a participating institution at the time the article is accepted for publication</li>')
        f.write('<li>OA is subject to approval by member institutions and any limits to the number of articles per publisher per year</li>')
        f.write('<li><strong>These journals aren\'t the only path to making your work OA.</strong> Your institution\'s library can advice on this.</li>')
        f.write('</ul>')
        f.write('<p>The <strong>e-ISSN,  ISSN,  IReL Agreement</strong> are all clickable links to more information about the journal and the relevant publisher agreement with IReL.</p>\n</div>')
        f.write('<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for journal titles..">')
        f.write(table_html)
        f.write(footer_html)
else:
    print("Could not find the start of the CSV data in the file.")
