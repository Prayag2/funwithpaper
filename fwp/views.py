from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'fwp/index.html')

class GamesView(generic.ListView):
    template_name = 'fwp/games.html'
    context_object_name = 'games_list'

    def get_queryset(self):
        return Game.objects.all().order_by('-id')

def game(request, game_id):
    g = Game.objects.get(id = game_id)
    g.user_views += 1
    g.save()
    context = {'game': g}
    return render(request, 'fwp/game.html', context)

def category(request, category_name):
    games_list = Game.objects.filter(category__name=category_name).order_by('-id')
    message = f'Category: {category_name}'
    context = {'games_list': games_list, 'message': message}
    return render(request, 'fwp/games.html', context)

def search(request):
    query = request.GET['q']
    games_list = Game.objects.filter(name__icontains=query)
    if not games_list.exists() or not query:
        context = {'message': "0 games found."}
        return render(request, 'fwp/games.html', context)
    else:
        plural = 's' if games_list.count() > 1 else ''
        context = {'games_list': games_list, 'message': f'{games_list.count()} game{plural} found.'}
        return render(request, 'fwp/games.html', context)

def request_game(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            suggestion=form.cleaned_data['suggestion']
            your_name=form.cleaned_data['your_name']

            existing_request = Request.objects.filter(suggestion=suggestion, your_name=your_name)
            if not existing_request.exists():
                form.save()
                messages.success(request, "Request Sent!")

                # Send Email
                subject="Fun With Paper New Game Request"
                body=f'A new request was made by "{your_name}" on Fun With Paper saying "{suggestion}"'
                send_mail(subject, body, settings.EMAIL_HOST_USER, ["prayagjain2@gmail.com"], fail_silently=False)
                return redirect('request_game')

            messages.error(request, "This request already exists!")
    else:
        form = RequestForm()

    return render(request, 'fwp/request.html', {'form': form})

def download(request, pk):
    download_link = Game.objects.get(id=pk).template_link
    return render(request, 'fwp/download_page.html', {'download_link': download_link})
