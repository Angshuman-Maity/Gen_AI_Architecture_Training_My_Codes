"""
This module has response cards format for telcogpt.
There are three cards defined 
1. Definition
2. Troubleshooting
3. Design
"""
import re

#Basic routing using regex 

_RGX_DEF = re.compile (f"(?i)\b (what is |define|explain)\b")
_RGX_TRB = re.compile (f"(?i)\b (error|alarm|fail|downtime|outage|degrade)\b")

CARD_DEF = """ <<CARD=Definition>>
Return exactly five bullets 
1. Concept <= 30 words
2. Technology domain (RAN | OSS/BSS | DEVICE)
3. 3GPP sepc ref
4. Key Parameters (<5)
5. Typical use cases

 """