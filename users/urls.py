from django.urls import path
from .views import ChildActivityResponseRawAPI

urlpatterns = [
    path(
        "activity-response/",
        ChildActivityResponseRawAPI.as_view()
    )
]
