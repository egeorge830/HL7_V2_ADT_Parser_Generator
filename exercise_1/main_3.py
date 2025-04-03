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
    """
    Extracts the LOINC code from the OBX segment.
    """
    try:
        obx_segments = message.obx
        loinc_codes = []
        for obx in obx_segments:
            loinc_code = obx.obx_3.obx_3_1.value  # LOINC Code (OBX-3.1)
            loinc_codes.append(loinc_code)

        return loinc_codes
    except (AttributeError, ValueError) as e:
        raise ValueError(f"Failed to extract LOINC Code from HL7 message: {e}")


if __name__== '__main__':
    file_path = data_dir / 'sample.hl7'
    hl7_raw = read_hl7_file(file_path)
    parsed_message = parse_hl7_message(hl7_raw)
    loinc_codes = extract_data(parsed_message)

    # Print extracted LOINC codes
    for code in loinc_codes:
        print(f"LOINC Code: {code}")
