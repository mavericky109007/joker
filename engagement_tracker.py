from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class EngagementMetrics:
    views: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0

class AnalyticsService:
    def __init__(self):
        self.metrics_store = {}
    
    def track_engagement(self, content_id: str, metrics: Dict[str, Any]):
        """
        Track engagement for a specific piece of content
        """
        if content_id not in self.metrics_store:
            self.metrics_store[content_id] = EngagementMetrics()
        
        current_metrics = self.metrics_store[content_id]
        current_metrics.views += metrics.get('views', 0)
        current_metrics.likes += metrics.get('likes', 0)
        # Add more metric tracking
    
    def get_content_analytics(self, content_id: str) -> EngagementMetrics:
        return self.metrics_store.get(content_id, EngagementMetrics())
