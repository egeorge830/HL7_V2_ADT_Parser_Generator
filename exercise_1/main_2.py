from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion
import os
from pathlib import Path

# Define the directory where the HL7 files are stored
data_dir = Path.cwd() / "data"


def read_hl7_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        return f.read()


def parse_hl7_message(hl7_raw):
    try:
        return parser.parse_message(hl7_raw)
    except UnsupportedVersion:
        # Replace newline with carriage return and try again
        return parser.parse_message(hl7_raw.replace("\n", "\r"))


def extract_data(message):

    try:
        dg_segments = message.dg1
        diagnoses = []
        for item in dg_segments:
            diagnosis_code = item.dg1_3.dg1_3_1.value  # Diagnosis Code
            diagnosis_desc = item.dg1_3.dg1_3_2.value  # Diagnosis Description
            diagnosis_date = item.dg1_5.value  # Diagnosis Date
            diagnoses.append((diagnosis_code, diagnosis_desc, diagnosis_date))

        return diagnoses
    except (AttributeError, ValueError) as e:
        raise ValueError(f"Failed to extract data from HL7 message: {e}")


if __name__ == '__main__':
    file_path = data_dir / 'sample.hl7'
    hl7_raw = read_hl7_file(file_path)
    parsed_message = parse_hl7_message(hl7_raw)
    diagnoses = extract_data(parsed_message)

    # Print extracted diagnoses
    for code, desc, date in diagnoses:
        print(f"Diagnosis Code: {code}, Description: {desc}, Date: {date}")