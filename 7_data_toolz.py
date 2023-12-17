# This code works perfectly for success path. 
# It will break in the middel of execution if there is something wrong
# Lets move to the next section that we will handle exception in a proper way
import csv
from toolz import curry, pipe
# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return [row for row in csv.reader(csvfile)]
    except FileNotFoundError as e:
        return None
    
# Extract 3 functions that do one thing and do it well
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except (ValueError, IndexError) as e:
        return None    

def remove_column(column_index, data):
    try:
        return data[column_index:]
    except IndexError as e:
        return None

def convert_to_float(data):
    try:
        return [float(item) for item in data] 
    except ValueError as e:
        return None
    
# Function to calculate average
def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError as e:
        return None    

data = read_csv_file('example.csv')  
extract_column_index = curry(extract_column)
extract_score = extract_column_index(1)


average_result = pipe(
    read_csv_file('example.csv'), 
    extract_score, 
    remove_header, 
    convert_to_float, 
    calculate_average
)

print(f"An average score is {average_result}")