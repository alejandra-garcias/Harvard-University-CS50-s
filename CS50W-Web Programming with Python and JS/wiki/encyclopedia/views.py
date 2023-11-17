import markdown
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from . import util
from django import forms
from django.urls import reverse
from .util import save_entry





class NewEntryForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(label = "Content", widget=forms.Textarea)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry_content = util.get_entry(name)

    if entry_content:
        entry_html =  markdown.markdown(entry_content)
        return render(request, "encyclopedia/entry.html", {
            "entry": entry_html
        })
    else:
        # La entrada no existe, redirige a una página de error 404
        return HttpResponseNotFound('<h1>Página no encontrada</h1>')


def search(request):
    query = request.GET.get('q', '')  # Get the search term from the URL
    entries = util.list_entries()

    # Filter entries based on the query
    filtered_entries = [entry for entry in entries if query.lower() in entry.lower()]

    if filtered_entries:
        # If there are matching entries, redirect to the first match
        return redirect('entry', name=filtered_entries[0])
    else:
        # If no matches found, render a search results page
        return render(request, "encyclopedia/search.html", {'entries': entries, 'query': query})
    


def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            title = form.cleaned_data['title']
            content =  form.cleaned_data['content']

            # Llamar a la función save_entry
            save_entry(title, content)
            # Obtener la URL de la vista entry para la entrada recién creada
            entry_url = reverse("entry", kwargs={"name": title})

            # Redirigir al usuario a la entrada recién creada
            return redirect(entry_url)
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/create.html", {
            "form": NewEntryForm()
        })

def edit(request, name):
    entry_content = util.get_entry(name)

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            edited_title = form.cleaned_data['title']
            edited_content = form.cleaned_data['content']
            save_entry(edited_title, edited_content)
            entry_url = reverse("entry", kwargs={"name": edited_title})
            return redirect(entry_url)
    else:
        initial_data = {'title': name, 'content': entry_content}
        form = NewEntryForm(initial=initial_data)

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "name": name, 
    })

def random_page(request):
    entries = util.list_entries()
    random_page = random.choice(entries)
    return redirect('entry', name=random_page)
