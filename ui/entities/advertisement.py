from dataclasses import dataclass
from typing import Optional

@dataclass
class Advertisement:
    ad_type: str
    ad_link: Optional[str] = None
    ad_text: Optional[str] = None
