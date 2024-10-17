from django.shortcuts import render

# Create your views here.
def register(request):
    # return HttpResponse(slug)
    context = {
        'active_link': 'users/register'
    }
    return render(request, 'register.html', context)