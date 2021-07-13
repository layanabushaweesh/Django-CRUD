from django.urls import path
from .views import SnackListView
from .views import  SnackDetailView ,SnackCreateView ,SnackUpdateView ,SnackDeleteView

urlpatterns = [
    path('', SnackListView.as_view(),name='snack_list'),
    path('<int:pk>',SnackDetailView.as_view(), name='snack_detail'),
    path("create/", SnackCreateView.as_view(), name="create_snack"),

    path('<int:pk>/update/' ,SnackUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", SnackDeleteView.as_view(), name="delete"),

    
]