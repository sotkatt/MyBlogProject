from django.urls import path
from blog.views import index, index_detail


urlpatterns = [
    path("", index, name="main-page"),
    path("detail/<int:pk>", index_detail, name="detail-page"),
]
