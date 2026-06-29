from http.client import HTTPResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required,login_required
from django.views.decorators.http import (require_http_methods , require_GET , require_POST)
from django.views.decorators.cache import cache_page
from django.contrib.admin.views.decorators import staff_member_required
from django.db import models

@login_required
def dashboard(request):
    return HTTPResponse("Dashboard")

@permission_required
def delete_required(request):
    pass
@csrf_exempt
def webhook(request):
    pass

@require_GET
def submit_form(request):
    pass

@require_POST
def name(args):
 pass

@require_http_methods
def name(args):
 pass


@cache_page(60 * 15)
def article_list(request):
    pass

@staff_member_required
def name(args):
 pass

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# استفاده:
User.full_name


