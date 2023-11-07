from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from product.models import *
from django.contrib.auth.models import User


# def categories_all_DEF(request):
#     category_VAR = CategoryMODEL.objects.all()
#     sub_category_VAR = SubCategoryMODEL.objects.all()
#     context={'category_VAR':category_VAR , 'sub_category_VAR':sub_category_VAR}
#     print(category_VAR)

#     return render(request, "dashboard/index.html", context)

def category_DEF(request):
    products = None
    
    categories = CategoryMODEL.objects.all()
    
    categoryID = request.GET.get('category_item')
    
    if categoryID:
        print(categoryID)
        products = ProductMODEL.get_all_products_by_categoryid(categoryID)
    else:
        products = ProductMODEL.objects.all();
        
    context={'categories':categories , 'products_all_VAR':products}
    
    return render(request, "dashboard/index.html", context)


def sub_category_DEF(request):
    products = None
    
    sub_categories_VAR = SubCategoryMODEL.objects.all()
    
    sub_category_id_VAR = request.GET.get('category_sub_item')
    
    if sub_category_id_VAR:
        print(sub_category_id_VAR)
        products = ProductMODEL.get_all_products_by_categoryid(sub_category_id_VAR)
    else:
        products = ProductMODEL.objects.all();
        
    context={'sub_categories_VAR':sub_categories_VAR , 'products_all_VAR':products}
    
    return render(request, "dashboard/index.html", context)


