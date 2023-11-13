from django.urls import path
#
from . import views
#
#
#
urlpatterns = [
        path('category_path'      , views.category_DEF       , name='category-URL'),
        path('category_sub_path'  , views.sub_category_DEF   , name='sub_category-URL'),
        path('category_menu_path'  , views.filtering_products_Based_on_category_DEF   , name='category_menu-URL'),


]





# category_path = category_path
#            = category_sub_path