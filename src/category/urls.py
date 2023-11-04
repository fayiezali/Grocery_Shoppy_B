from django.urls import path
#
from . import views
#
#
#
urlpatterns = [
        # path('categories_all', views.store, name="categories_all-URL"),
        path('store_path', views.store_DEF , name='store-URL'),

]