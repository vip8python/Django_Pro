from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    # path('', index, name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('additem/', add_item, name='add_item'),
    path('updateitem/<int:my_id>/', update_item, name='update_item'),
    path('deleteitem/<int:my_id>/', delete_item, name='delete_item'),

]
