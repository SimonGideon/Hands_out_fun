from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = '.templates/forms.html'
    def get_context_data(self, **kwargs):
        kwargs['Enviroment'] = 'Prodution'
        return super().get_context_data(**kwargs)

# Create your views here.
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
        else:
            form = NameForm()
    return render(request, 'forms.html', {'form': form})


from .forms import ContactForm
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
