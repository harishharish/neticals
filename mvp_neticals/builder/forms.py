from django import forms
from .models import PDBFiles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MolBuilderForm(forms.ModelForm):
    class Meta:
        model = PDBFiles
        fields =  ['pdb_id', 'entry_date', 'description']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')



# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

# from .forms import UploadFileForm

# def upload_file(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#             return HttpResponseRedirect("/success/url/")
#     else:
#         form = UploadFileForm()
#     return render(request, "upload.html", {"form": form})