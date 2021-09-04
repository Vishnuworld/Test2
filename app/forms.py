from django import forms
# exec(open(r'F:\Class\B3-B4\Django\Form_Project\app\forms.py').read())
from app.models import Person


class SimpleForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=False)
    lastname = forms.CharField(max_length=100)
    age = forms.IntegerField()


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('name', 'email', 'job_title', 'bio', 'age')




# f = SimpleForm()
# print(f.as_ul())
# print(f.as_table())
# print(f.as_p())

# f = SimpleForm({"firstname":"abc", "lastname":"xyz", "age": 25})
# print(f.is_valid())
# print(f.errors)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )


    def clean(self):
        print("In clean method")
        cleaned_data = super(ContactForm, self).clean()
        # print(cleaned_data, "cleaned data")
        cd = self.cleaned_data
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            print("@@@@@@@@")
            raise forms.ValidationError('You have to write something!')
        return cleaned_data

# f = ContactForm()
# print(f)

