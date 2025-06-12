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

CARD_TRB = """ <<CARD=Troubleshooting>>
Return exactly five bullets 
1. Root cause(s)
2. Impact on Network
3. KPIs affected 
4. Recommended Fix
5. Fallback

 """

CARD_DES = """ <<CARD=Design>>
Return exactly five bullets 
1. Objective
2. Required Inputs
3. Best Practices/Formula 
4. Example
5. Standards

 """

def detect_card_type(q: str) -> str:
    """Return the appropriate response card for the given query."""
    if _RGX_DEF.search(q):
        return CARD_DEF
    if _RGX_TRB.search(q):
        return CARD_TRB
    return CARD_DES
