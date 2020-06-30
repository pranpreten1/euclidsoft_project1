from django.shortcuts import render
from k_admin.models import Module


def module_list(request):
    modules = Module.objects.all()
    return render(request, 'k_admin/module_list.html', {'modules':modules})
