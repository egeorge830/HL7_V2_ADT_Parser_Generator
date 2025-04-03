from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion, HL7apyException
import datetime
import os
from pathlib import Path

# Define the directory where the HL7 files are stored
data_dir = Path.cwd() / "data"


def read_hl7_file(file_path):
    """
    Reads the content of an HL7 file.

    Args:
        file_path (str or Path): Path to the HL7 file.

    Returns:
        str: The raw HL7 message as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        return f.read()


def parse_hl7_message(hl7_raw):
    """
    Parses an HL7 message string using hl7apy.

    Args:
        hl7_raw (str): Raw HL7 message.

    Returns:
        hl7apy.core.Message: Parsed HL7 message object.

    Handles:
        UnsupportedVersion: If the version is not recognized, attempts to fix segment separators.
    """
    try:
        return parser.parse_message(hl7_raw)
    except UnsupportedVersion:
        # Replace newline with carriage return and try again
        return parser.parse_message(hl7_raw.replace("\n", "\r"))


def extract_metadata(message):
    """
    Extracts relevant metadata from an HL7 message object.

    Args:
        message (hl7apy.core.Message): Parsed HL7 message.

    Returns:
        dict: Metadata extracted from the HL7 message.

    Raises:
        ValueError: If required fields are missing or timestamp format is incorrect.
    """
    try:
        return {
            "type": message.msh.msh_9.value,  # Message type (e.g., ADT^A01)
            "client_app": message.msh.msh_3.value,  # Sending application
            "client_fac": message.msh.msh_4.value,  # Sending facility
            "control_id": message.msh.msh_10.value,  # Message control ID
            "process_id": message.msh.msh_11.value,  # Processing ID
            "timestamp": datetime.datetime.strptime(  # Message timestamp
                message.msh.msh_7.value, "%Y%m%d%H%M%S%f"
            ),
            "hl7": message  # Original HL7 message object
        }
    except (AttributeError, ValueError) as e:
        raise ValueError(f"Failed to extract metadata from HL7 message: {e}")


def main():
    """
    Main function to load, parse, and extract metadata from an HL7 file.
    """
    file_path = data_dir / 'sample.hl7'  # Construct full path to HL7 file
    try:
        hl7_raw = read_hl7_file(file_path)  # Read file content
        message = parse_hl7_message(hl7_raw)  # Parse raw HL7 message
        incoming_hl7 = extract_metadata(message)  # Extract metadata
        print(incoming_hl7)  # Output metadata
    except (FileNotFoundError, HL7apyException, ValueError) as e:
        # Handle and report common errors during processing
        print(f"Error processing HL7 message: {e}")


# Ensure main runs only when the script is executed directly
if __name__ == "__main__":
    main()