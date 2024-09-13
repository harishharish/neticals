from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mol_list", views.mol_list, name="mol_list"),
    path("add_mol", views.add_mol, name="add_mol"),
    path("<int:mol_id>/edit_mol", views.edit_mol, name="mol_edit"),
    path("<int:mol_id>/delete_mol", views.delete_mol, name="mol_delete"),
]