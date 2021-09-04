from django.shortcuts import render
from app.forms import SimpleForm, ContactForm
# Create your views here.

def home(request):
    form = SimpleForm()
    return render(request, "home.html", {"form": form})


from django.views.generic import CreateView, UpdateView
from .models import Person, Contact
from django.urls import reverse_lazy

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio', 'age')
    success_url = reverse_lazy('pcv')

# class PersonUpdateView(UpdateView):
#     model = Person
#     form_class = PersonForm
#     template_name = 'people/person_update_form.html'



def contact(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST['email'])
        print("abcd")
        form = ContactForm(request.POST)
        print("xyz")
        if form.is_valid():
            print("data is valid")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            c = Contact(name=name, email=email, message=msg)
            c.save()
        else:
            print("data is invalid")
            context = {"form" : form}
            return render(request, "contact.html", context)
 

    context = {"form" : ContactForm()}
    return render(request, "contact.html", context)


        
# is_valid() -- valid - True invalid - False
# clean_data -- data once validated
# - u can render a template after success -- with name 
# HttpResponseRedirect
# from django.http import HttpResponseRedirect
# redirect to new function


# cleaning and validating specific field
# clean_fieldname
# validations


# example email shud be @cohin.com



class StudReg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    # name shud be not be more than 4 characters

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            raise forms.ValidationError("Name length shud be more than 4 characters..")
        return name

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        email = self.cleaned_data['email']
        
        if len(valname) < 4:
            raise forms.ValidationError("Name length shud be more than 4 characters..")
        if len(email) < 10:
            raise forms.ValidationError("Email shud be more than 10")



# Vlaidation of Complete Django Form at once
# clean()
    # - run to_python(), validate(), run_Validators() in correct order

# - search clean in django -- implemented in above code


# ----------------

# Built in validators
from django.core import validators

class StudReg(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)


# create custom validators
def custom_validators(n):
    if n[0] != 's':
        raise forms.ValidationError("Name shud stat with s")



class StudReg(forms.Form):
    name = forms.CharField(validators=[custom_validators])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)




from django.shortcuts import redirect
from django import forms


class StudReg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valid_pass = self.cleaned_data['password']
        pass_2 = self.cleaned_data['rpassword']

        if valid_pass != pass_2:
            print("in clean")
            raise forms.ValidationError("Password does not match")



def stud_reg(request):
    if request.method == 'POST':
        sr = StudReg(request.POST)
        if sr.is_valid():
            print('in valid')
            return redirect('stud_reg')
        else:
            return render(request, template_name='password.html', context={'form': sr})
    else:
        sr = StudReg()
        return render(request, template_name='password.html', context={'form': sr})

# if i pass id while creating object in form -- then its update
# User(id=1).delete()   -- to delete