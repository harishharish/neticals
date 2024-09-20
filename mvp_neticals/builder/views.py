from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import PDBFiles
from .forms import MolBuilderForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "builder/index.html")


def mol_list(request) -> HttpResponse:
    """
    Render html page that list molecule from PDBFiles model
    """
    mols = PDBFiles.objects.all().order_by('-entry_date')
    return render(request, 'builder/mol_list.html', {'mols':mols})


@login_required
def add_mol(request) -> HttpResponse:
    if request.method  == 'POST':
        form = MolBuilderForm(request.POST, request.FILES)
        if form.is_valid():
            mol_form = form.save(commit=False)
            mol_form.user = request.user
            mol_form.save()
            return redirect('mol_list')
    else:
        form = MolBuilderForm()
    return render(request, 'builder/mol_form.html', {'form':form})


@login_required
def edit_mol(request, mol_id) -> HttpResponse:
    mol = get_object_or_404(PDBFiles, pk=mol_id, user = request.user )
    if request.method == 'POST':
        form  = MolBuilderForm(request.POST, request.FILES, instance=mol)
        if form.is_valid():
            mol_form = form.save(commit=False)
            mol_form.user = request.user
            mol_form.save()
            return redirect('mol_list')
    else:
        form =  MolBuilderForm(instance=mol)
    return render(request, 'builder/mol_form.html', {'form':form})

@login_required
def delete_mol(request, mol_id) -> HttpResponse:
    mol = get_object_or_404(PDBFiles, pk=mol_id, user=request.user)
    if request.method == 'POST':
        mol.delete()
        return redirect('mol_list')
    return render(request, 'builder/mol_delete.html', {'mol':mol})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('mol_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
