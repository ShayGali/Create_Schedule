""" Extract tables from PDF file and save them as CSV files. """
import tabula

# Path to your pdf file
file = "data/src.pdf"

# Read PDF file
tables = tabula.read_pdf(file, pages="all", multiple_tables=True)

# Convert extracted tables into CSV file
for i, table in enumerate(tables):
    table.to_csv(f"data/table_{i}.csv", index=False)
