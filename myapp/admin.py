# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category
from .models import Item
# from .models import Enviroment
admin.site.register(Category)
admin.site.register(Item)
# admin.site.register(Enviroment)
# Register your models here.
