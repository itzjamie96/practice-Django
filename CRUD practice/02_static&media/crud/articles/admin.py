from django.contrib import admin
# 관리할 모델 가져오기
from .models import *

# Register your models here.
admin.site.register(Article)