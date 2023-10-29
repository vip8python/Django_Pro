from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexitem, name='detail'),
    path('additem/', add_item, name='add_item'),
    path('updateitem/<int:my_id>/', update_item, name='update_item'),

]
