#Get all filename for raw from source

from pathlib import Path
import csv
import pandas as pd

# Create a Path object for the directory to be listed
directory = Path("C:\\Users\\myazidagmyaakub.agmy\\Downloads\\PEDMS\\PEDMS\\PMA\\Resak")

# List all files in the directory
files = directory.glob("**/*")

# Export the DataFrame to a CSV file
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(["Filename", "FileExt","Path"])
    
    # Write the data rows
    for file in files:
        writer.writerow([file.name if file.name else "", file.suffix if file.suffix else "", 
                         file.parent if file.parent else ""])
