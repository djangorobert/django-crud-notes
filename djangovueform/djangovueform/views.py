from django.shortcuts import render
from django.http import JsonResponse
import json
from django.urls import reverse_lazy
from notes.forms import NoteModelForm
from notes.models import Note
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404


def submit_form(request):
    if request.method == "POST":

        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        if username and password:
            response = f"Welcome {username} - {password}"
            return JsonResponse({"msg": response}, status=201)


        else:
            response = "username or password is empty"
            return JsonResponse({"err":response}, status=400)

    return render(request, 'submit-form.html')


def send_note(request):
    all_notes = Note.objects.all()
    if request.method == 'POST':
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NoteModelForm()
    context = {
        'form': form,
        'all_notes': all_notes
    }
    return render(request, 'note.html', context)

#create view
class NoteCreateView(CreateView):
    model = Note
    fields = ['description']
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')


#detailView
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'


#Listview
class NoteListView(ListView):
    template_name = 'note_list.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        return Note.objects.all()


#edit view
class NoteUpdateView(UpdateView):
    model = Note
    fields = ['description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('note_list')


#delete view
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')
  