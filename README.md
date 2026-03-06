Academic project developed during the M.S. in Health Informatics program at Indiana University.

### Exercise 1
#### Parse and extract data from an HL7 ADT^A01 message.
**Files**:
  - main_2.py: Extracted the diagnosis codes and dates from DG1 segments.
  - main_3.py: Extracted the LOINC code from the OBX segment.
- **LOINC Code Description**:
  - **Code**: 21612-7
  - **Description**: Reported Patient Age - Represents the age of the patient as reported, typically measured in years.

### Exercise 2
 Generate an HL7 ADT^A04 message.

In main.py: Creates a valid HL7 message with completion of PID segment and this was written into the `output.hl7`.
