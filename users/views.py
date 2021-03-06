from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'users/register.html'


    def get(self, request):
        form = RegisterForm()

        args = {
            'title': 'Register',
            'form': form
        }

        return render(request, self.template_name, args)
    
    def post(self, request):

        # collects the POST request 
        form = RegisterForm(request.POST)

        # ensures that the form data conforms to certain validation checks
        if form.is_valid():
            email       = form.cleaned_data.get('email') # retrieving the data
            first_name  = form.cleaned_data.get('first_name')
            last_name   = form.cleaned_data.get('last_name')
            is_teacher  = form.cleaned_data.get('is_teacher')

            form.save() # saving to the DB
            messages.success(request, f'Account created for {first_name}!') # adding message session variable
            return redirect('login') # redirect to the login
        else:
            # if the form is invalid it will redirect to the same page with the populated form
            args = {
                'title': 'Register',
                'form': form
            }
        return render(request, self.template_name, args)