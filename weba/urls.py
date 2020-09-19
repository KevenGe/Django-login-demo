from django.urls import include, path
from . import views

urlpatterns = [
    path("gg/", views.web1, name="gg"),
    path("ll/", views.web1, name="ll"),
    path("ans/<int:question_id>", views.getChoices, name="detail"),
    path("login/", views.login),
    path("status/", views.status, name="status")
]
