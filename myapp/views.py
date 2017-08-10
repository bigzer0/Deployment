# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from myapp.models import Category
from myapp.models import Item
# from myapp.models import Enviroment
from  myapp.forms import ItemForm
from subprocess import Popen
from subprocess import PIPE
import subprocess
import os
import paramiko
import sys

# Create your views here.
# def index(request):
#     number = 10
#     categories = Category.objects.all()
#     return render(request, 'index.html',
#                   { 'categories': categories
#                     })

def index(request):
    items = Category.objects.all()
    return render(request,'index.html', {'items': items })

# def list_cat_uatvn1(request,id):
#     list_cats = Category.objects.filter(id=id())
#     return render(request,'list_cat_uatvn1.html',{'list_cats': list_cats})
######################################### BO SYSTEM #######################################################################
def bo_view(request):
    bo_items = Item.objects.filter(i_subsystem__contains='bo_')
    return render(request, 'bo.html',{'bo_items': bo_items})

def item_detail_bo(request,name):
    item_detail = Item.objects.get(i_name=name)
    return render(request,'bo_item_detail.html',{'item_detail' : item_detail})

def show_log_bo(request,name):
    log_item = Item.objects.get(i_name=name)
    ip = log_item.i_host
    port = 22
    username = 'root'
    password = '123456'
    cmd = 'tail -n100 /var/log/secure'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    return render(request, 'show_log_bo.html', {'resp': resp})
    # NOTE: khi truyen bien sang template thi ten bien la "log_detail" chu khong phai "resp"

def edit_detail_bo(request, name):
    item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=item)
        link = request.POST.get('i_link_source')
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
#       args_1 = ['ssh', '192.168.127.128']
#       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('bo_item_detail', name=item.i_name)
    else:
        form = form_class(instance=item)
    return render(request,'edit_detail_bo.html',{'item': item, 'form': form,})

def ntd_view(request):
    ntd_items = Item.objects.filter(i_subsystem__contains='ntd_')
    return render(request, 'ntd.html',{'ntd_items': ntd_items})


def item_detail_ntd(request,name):
    ntd_item_detail = Item.objects.get(i_name=name)
    return render(request,'ntd_item_detail.html',{'ntd_item_detail' :  ntd_item_detail})

def edit_detail_ntd(request, name):
    ntd_item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=ntd_item)
        link = request.POST.get('i_link_source')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
#       args_1 = ['ssh', '192.168.127.128']
#       subprocess.call('args_1')
        location = '/tmp/'
        url = link
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
        #       args_1 = ['ssh', '192.168.127.128']
        #       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('ntd_item_detail', name=ntd_item.i_name)
    else:
        form = form_class(instance=ntd_item)
    return render(request,'edit_detail_ntd.html',{'ntd_item': ntd_item, 'form': form,})

######################################### SOCIAL SYSTEM #######################################################################
def social_view(request):
    social_items = Item.objects.filter(i_subsystem__contains='social_')
    return render(request, 'social.html',{'social_items': social_items})



def item_detail_social(request,name):
    social_item_detail = Item.objects.get(i_name=name)
    return render(request,'social_item_detail.html',{'social_item_detail' :  social_item_detail})




def edit_detail_social(request, name):
    social_item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=social_item)
        link = request.POST.get('i_link_source')
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
        #       args_1 = ['ssh', '192.168.127.128']
        #       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('social_item_detail', name=social_item.i_name)
    else:
        form = form_class(instance=social_item)
    return render(request,'edit_detail_social.html',{'social_item':social_item, 'form': form,})

######################################### BATCH SYSTEM #######################################################################
def batch_view(request):
    batch_items = Item.objects.filter(i_subsystem__contains='batch_')
    return render(request, 'batch.html',{'batch_items': batch_items})


def item_detail_batch(request,name):
    batch_item_detail = Item.objects.get(i_name=name)
    return render(request,'batch_item_detail.html',{'batch_item_detail' :  batch_item_detail})

def edit_detail_batch(request, name):
    batch_item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=batch_item)
        link = request.POST.get('i_link_source')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
#       args_1 = ['ssh', '192.168.127.128']
#       subprocess.call('args_1')
        location = '/tmp/'
        url = link
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
        #       args_1 = ['ssh', '192.168.127.128']
        #       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('social_item_detail', name=batch_item.i_name)
    else:
        form = form_class(instance=batch_item)
    return render(request,'edit_detail_batch.html',{'social_item':batch_item, 'form': form,})

######################################### ACTIVEMQ SYSTEM #######################################################################
def activemq_view(request):
    activemq_items = Item.objects.filter(i_subsystem__contains='activemq_')
    return render(request, 'activemq.html',{'activemq_items': activemq_items})


def item_detail_activemq(request,name):
    activemq_item_detail = Item.objects.get(i_name=name)
    return render(request,'activemq_item_detail.html',{'activemq_item_detail' : activemq_item_detail})

def edit_detail_activemq(request, name):
    activemq_item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=activemq_item)
        link = request.POST.get('i_link_source')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
#       args_1 = ['ssh', '192.168.127.128']
#       subprocess.call('args_1')
        location = '/tmp/'
        url = link
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
        #       args_1 = ['ssh', '192.168.127.128']
        #       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('activemq_item_detail', name=activemq_item.i_name)
    else:
        form = form_class(instance=activemq_item)
    return render(request,'edit_detail_activemq.html',{'activemq_item':activemq_item, 'form': form,})



#########################################  MEMCACHE SYSTEM #######################################################################
def memcache_view(request):
    memcache_items = Item.objects.filter(i_subsystem__contains='activemq_')
    return render(request, 'memcache.html',{'memcache_items': memcache_items})


def item_detail_memcache(request,name):
    memcache_item_detail = Item.objects.get(i_name=name)
    return render(request,'memcache_item_detail.html',{'memcache_item_detail' :memcache_item_detail})

def edit_detail_memcache(request, name):
    memcache_item = Item.objects.get(i_name=name)
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=memcache_item)
        link = request.POST.get('i_link_source')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
#       args_1 = ['ssh', '192.168.127.128']
#       subprocess.call('args_1')
        location = '/tmp/'
        url = link
        baseDir = request.POST.get('i_baseDir')
        ip_address = request.POST.get('i_host')
        # destination = 'root@'+ip_address+':/tmp/'
        #       args_1 = ['ssh', '192.168.127.128']
        #       subprocess.call('args_1')
        location = '/tmp/'
        # url = link
        arg_4 = baseDir
        arg_3 = link
        arg_1 = 'bash'
        arg_2 = '/tmp/deploy.sh'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.127.128', username='root', password='123456')
        command = '%s %s %s %s' % (arg_1, arg_2, arg_3, arg_4)
        stdin, stdout, stderr = ssh.exec_command(command)
        # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
        # subprocess.call(args)
#       subprocess.call(['ssh','192.168.127.128', 'cd /tmp/ && wget link'])
#       subprocess.call(['/tmp/find_file.sh', 'link'])
#       args = ['/usr/bin/scp', '/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', 'destination']
#       p = subprocess.Popen(["scp",'/tmp/svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip', destination])
#         if link:
#                 (filepath, filename) = os.path.split(link)
#                 a = find(filename,location)
#                 p = subprocess.Popen(["scp", a, destination])
# #       ./find_file.sh https://svn.nextop.asia/artifacts/nts-ams-api-controller-4.7.2-bin.zip 192.168.127.128
# #       out, err = p.communicate()
# #       exitcode = p.returncode
        if form.is_valid():
            form.save()
            return redirect('memcache_item_detail', name=memcache_item.i_name)
    else:
        form = form_class(instance=memcache_item)
    return render(request,'edit_detail_memcache.html',{'memcache_item':memcache_item, 'form': form,})









def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


# def edit_detail_bo(request, name):
#     item = Item.objects.get(i_name=name)
#     form_class = ItemForm
#     errrr = 'abc'
#
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=item)
#         link = request.POST.get('i_link_source')
#         # location = '/tmp/'
#         # url = link
#         # args = ['wget', 'r', '-l', '1', '-p', '-P', location, url]
#         #
#         if form.is_valid():
#             form.save()
#
#             return redirect('bo_item_detail', name=item.i_name,)
#     else:
#         form = form_class(instance=item)
#     return render(request,'edit_detail_bo.html',{'item': item, 'form': form,})










#
# Please help to do this task:
# 1. Requirement
#  - Using web interface to deploy.
#  - have a page for configuration management ( server, process name, port, base dir ...)
#  - Have a page for checking logs
#  - Have a page for check process status.
#  - Run script deploy with non root user.
# 2. Procedure:
#  - Have basically understand Java service: Middle services, Web ( Config, deploy, check log, stop/start) (1 days)
#  - How to deploy service on UAT env. (2 days)
#  - Python basic (2 days)
#  - Database basic (2 days)
#  - Python advance for web (10 days)
#  - Deployment page (7 days)
#  - Configuration management page (7 days)
#  - checking logs page (7 days)
#  - service status page (7 days)
#  - Test & optimize (15 days)
