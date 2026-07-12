from .status_views import (
    IndexView,
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    StatusDeleteView,
)
from .label_views import (
    LabelListView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView,
)
from .task_views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
)

__all__ = [
    'IndexView',
    'StatusListView',
    'StatusCreateView',
    'StatusUpdateView',
    'StatusDeleteView',
    'LabelListView',
    'LabelCreateView',
    'LabelUpdateView',
    'LabelDeleteView',
    'TaskListView',
    'TaskCreateView',
    'TaskUpdateView',
    'TaskDeleteView',
    'TaskDetailView',
]
