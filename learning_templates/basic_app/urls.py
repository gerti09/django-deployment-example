from django.urls import path  # Import path (or re_path for regex)
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),  # Updated to use path()
    path('other/', views.other, name='other'),
]
