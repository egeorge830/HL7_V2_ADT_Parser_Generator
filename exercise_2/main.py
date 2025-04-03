from hl7apy.core import Message
from pathlib import Path

# Define where to save the file
data_dir = Path.cwd() / "data"

# Create HL7 ADT_A03 message
hl7 = Message("ADT_A03", version="2.5")

# MSH Segment (Message Header)
hl7.msh.msh_1 = "|"
hl7.msh.msh_2 = "^~\\&"
hl7.msh.msh_3 = "EPIC"
hl7.msh.msh_4 = "EPICADT"
hl7.msh.msh_5 = "SMS"
hl7.msh.msh_6 = "SMSADT"
hl7.msh.msh_7 = "202211031408"
hl7.msh.msh_8 = "CHARRIS"
hl7.msh.msh_9 = "ADT^A04"
hl7.msh.msh_10 = "1817457"
hl7.msh.msh_11 = "D"
hl7.msh.msh_12 = "2.5"

# EVN Segment
hl7.evn.evn_1 = ""
hl7.evn.evn_2 = "202211030800"
hl7.evn.evn_3 = ""
hl7.evn.evn_4 = ""
hl7.evn.evn_5 = ""
hl7.evn.evn_6 = "202211030800"

# PID Segment
hl7.pid.pid_1 = ""
hl7.pid.pid_2 = "0493575^^^2^ID 1"
hl7.pid.pid_3 = "454721"
hl7.pid.pid_4 = ""
hl7.pid.pid_5 = "DOE^JOHN^^^^"
hl7.pid.pid_6 = "DOE^JOHN^^^^"
hl7.pid.pid_7 = "19480203"
hl7.pid.pid_8 = "M"
hl7.pid.pid_9 = ""
hl7.pid.pid_10 = "B"
hl7.pid.pid_11 = "254 MYSTREET AVE^^MYTOWN^OH^44123^USA"
hl7.pid.pid_12 = ""
hl7.pid.pid_13 = "(216)123-4567"
hl7.pid.pid_14 = ""
hl7.pid.pid_15 = ""
hl7.pid.pid_16 = "M"
hl7.pid.pid_17 = "NON"
hl7.pid.pid_18 = "400003403"

# NK1 Segment – using raw ER7 string
hl7.nk1 = "NK1|1|ROE^MARIE^^^^|SPO||(216)123-4567||EC|||||||||||||||||||||||||||"

# PV1 Segment – using raw ER7 string, match count exactly
hl7.pv1 = "PV1||O|||||277^ALLEN MYLASTNAME^BONNIE^^^^|||||||||| ||2688684|||||||||||||||||||||||||202211031408||||||002376853"

# Validate
if hl7.validate():
    print("HL7 message is valid.")

# Save to output.hl7
output_file = data_dir / "output.hl7"
with open(output_file, "w") as f:
    f.write(hl7.to_er7())

print(f"Message saved to: {output_file}")