from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'users/register.html'


    def get(self, request):
        form = UserCreationForm()

        args = {
            'title': 'Register',
            'form': form
        }

        return render(request, self.template_name, args)