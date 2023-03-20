from django.contrib import admin
from .models import Articles

# Register your models here.
# 관리자 사이트에 Articles 등록
admin.site.register(Articles)