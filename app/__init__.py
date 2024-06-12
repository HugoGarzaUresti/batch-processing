import csv

def read_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    # Example processing: add a new field "processed_age" which is age * 2
    for row in data:
        row['processed_age'] = int(row['age']) * 2
    return data

def write_data(file_path, data):
    if data:
        fieldnames = data[0].keys()
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'
    data = read_data(input_file)
    processed_data = process_data(data)
    write_data(output_file, processed_data)
    print('Data Succesfully processed')

if __name__ == "__main__":
    main()
