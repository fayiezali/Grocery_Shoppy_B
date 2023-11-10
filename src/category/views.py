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
    products_VAR = None
    
    categories_VAR = CategoryMODEL.objects.all()
    
    categoryID = request.GET.get('category_item')
    print(categoryID)
    if categoryID:
        products_VAR = ProductMODEL.get_all_products_by_categoryid(categoryID)
        print(categoryID)
        print(products_VAR)
    else:
        products_VAR = ProductMODEL.objects.all();
        print(products_VAR) 
        
    context={'categories_VAR':categories_VAR , 'products_all_VAR':products_VAR}
    
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


