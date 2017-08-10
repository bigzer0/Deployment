# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.

# class Enviroment(models.Model):
#     u_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.u_name

class Category(models.Model):
    c_name = models.CharField(max_length=100)
    # en = models.ForeignKey(Enviroment,on_delete=models.CASCADE)
    def __str__(self):
        return self.c_name

class Item(models.Model):
    i_name = models.CharField(max_length=30)
    i_host = models.CharField(max_length=30)
    i_service = models.IntegerField()
    # i_description = models.TextField(blank=True)
    i_link_source = models.CharField(max_length=300, blank=True)
    i_subsystem = models.CharField(max_length=50)
    i_processName = models.CharField(max_length=100)
    i_baseDir     = models.CharField(max_length=100)


    # i_conf_1 = models.CharField(max_length=300, blank=True)
    # i_conf_2 = models.CharField(max_length=300, blank=True)
    # i_file_3 = models.TextField(blank=True,null=True)
    # i_file_4 = models.TextField(blank=True,null=True)
    # i_file_5 = models.TextField(blank=True,null=True)

    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.i_name

