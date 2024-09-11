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

def details(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))