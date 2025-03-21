from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional, List, Dict, Any


@dataclass
class TradeEntry:
    id: str
    timestamp: datetime
    market: str
    side: str  # "buy" or "sell"
    size: float
    price: float
    tags: List[str]
    note: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["timestamp"] = self.timestamp.isoformat()
        return d

