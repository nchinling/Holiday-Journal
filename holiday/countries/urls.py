from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="countries"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("destination/<int:destination_id>/", views.destination, name="destination"),
    path("personal", views.personal, name="personal"),
    path("edit/<int:destination_id>/", views.edit, name="edit"),
    path("delete_journal/<int:destination_id>/", views.delete_journal, name="delete_journal"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('delete_photo/', views.delete_photo, name='delete_photo'),
    path("register", views.register_request, name="register"),
    path("search", views.search, name="search")
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)