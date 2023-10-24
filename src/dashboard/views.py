from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from product.models import *


# The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the dashboard Page
def dashboard_DEF(request):
    # Get All Products and Save In Variable
    products_all_VAR = ProductMODEL.objects.all()
    # Put the data to be displayed on the page in context
    context={'products_all_VAR':products_all_VAR}
    return render(request,'dashboard/index.html', context)
#
#
#
# # The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the about Page
# @login_required(login_url='login/')
# def about(request):
#     context={}
#     return render(request,'dashboard/about.html',context)




# def product_detail_DEF(request, product_id):
#     products_details_VAR=ProductMODEL.objects.get(id=product_id)
#     context={'products_details_VAR':products_details_VAR}
#     return render(request,"orders/product_details.html",context)

