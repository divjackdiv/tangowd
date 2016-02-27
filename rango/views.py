from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import *
from rango.forms import *
from django.contrib.auth.decorators import login_required

def bienvenue(request):
    emessage_list = EMessage.objects.all().order_by("-id")

    print len(emessage_list)

    return render(request, 'bienvenue.html', {'emessage_list': emessage_list})

@login_required
def account(request):
<<<<<<< HEAD
    context_dooct = {}

    try:
        user = request.user
        account = Account.objects.get(user = user)
        context_dooct['user'] = user
        context_dooct['account'] = account
    except Account.DoesNotExist:
        pass

    return render(request, 'rango/account.html', context_dooct)


@login_required
def emessage(request):
    context_doooct = {}
    form = EMessageForm(request.POST)

    if request.method == "POST":
        new_emessage = form.save(commit = False)
        new_emessage.author = request.user
        new_emessage.save()

        return redirect('account')
    else:
        form = EMessageForm()

    context_doooct['form'] = form

    return render(request, 'emessage.html', context_doooct)
=======
    return render(request, 'rango/account.html')
>>>>>>> eb71a171e7603838f9a32f4513a662b7e0da5efc
