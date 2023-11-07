from django.urls import path
#
from . import views
#
#
#
urlpatterns = [
        path('category_path'      , views.category_DEF       , name='category-URL'),
        path('category_sub_path'  , views.sub_category_DEF   , name='sub_category-URL'),

]





# category_path = category_path
#            = category_sub_path