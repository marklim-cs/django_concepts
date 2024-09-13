from django.http import HttpResponse
from django.template import loader
from .models import User

def all_users(request):
    users = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    user = User.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    users = User.objects.filter(lastname__istartswith='l').values() # same as __startswith but case insensitive
    members = User.objects.order_by('-firstname', 'id').values() # - for reverse order
    template = loader.get_template('test.html')
    context = {
        'users': users,
        'members': members,
    }
    return HttpResponse(template.render(context, request))