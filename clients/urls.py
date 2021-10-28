from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    # index
    path('', views.index, name='index'),

    # crud 1
    path('create', views.create_client, name='create'),
    path('<int:cid>', views.details, name='details'),
    path('update/<int:cid>', views.update, name='update'),
    path('delete/<int:cid>', views.delete, name='delete'),

    # crud 2
    path('<int:cid>/create_case', views.create_case, name='create_case'),
    path('<int:case_id>/update_case', views.update_case, name='update_case'),
    path('<int:case_id>/delete_case', views.delete_case, name='delete_case'),
]
