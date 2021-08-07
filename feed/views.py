from django.shortcuts import render, redirect

from .models import Feed


def index(request):
    context = {
        'feeds': Feed.objects.all(),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        Feed.objects.create(
            content=request.POST.get('content'),
            image=request.FILES.get('image')
        )
        return redirect('feed:index')
    else:
        return render(request, 'form.html')
