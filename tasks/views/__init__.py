from .label_views import (
    LabelCreateView,
    LabelDeleteView,
    LabelListView,
    LabelUpdateView,
)
from .status_views import (
    IndexView,
    StatusCreateView,
    StatusDeleteView,
    StatusListView,
    StatusUpdateView,
)
from .task_views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)

__all__ = [
    "IndexView",
    "StatusListView",
    "StatusCreateView",
    "StatusUpdateView",
    "StatusDeleteView",
    "LabelListView",
    "LabelCreateView",
    "LabelUpdateView",
    "LabelDeleteView",
    "TaskListView",
    "TaskCreateView",
    "TaskUpdateView",
    "TaskDeleteView",
    "TaskDetailView",
]
