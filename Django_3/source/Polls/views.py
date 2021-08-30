from django.shortcuts import render


# Create your views here.
def contact(request):
    form = contact(request)
    return render(request, 'form.html', {'form': form})
