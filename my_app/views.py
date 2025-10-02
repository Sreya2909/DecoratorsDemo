# Create your views here.
from django.shortcuts import render 

from django.contrib.auth.decorators import login_required, permission_required 

from django.views.decorators.http import require_http_methods 

from django.views.decorators.cache import cache_page 

from django.http import HttpResponse 

import datetime 

 

# 1. @login_required 

@login_required 

def dashboard(request): 

    return HttpResponse(f"Hello {request.user.username}, welcome to your dashboard!") 

 

# 2. @permission_required 

@permission_required('my_app.can_add_user') 

def add_user(request): 

    return HttpResponse(" You have permission to add a user.") 

 

# 3. @require_http_methods 

@require_http_methods(["GET", "POST"]) 

def contact(request): 

    if request.method == "POST": 

        return HttpResponse(" Thank you for your message!") 

    return HttpResponse(" Please submit the contact form.") 

 

# 4. @cache_page 

@cache_page(60 * 5) 

def static_content(request): 

    current_time = datetime.datetime.now() 

    return HttpResponse(f"This page was generated at: {current_time}") 