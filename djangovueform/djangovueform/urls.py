from django.contrib import admin
from django.urls import path
from .views import submit_form, NoteListView, NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-form', submit_form, name='submitform'),
    #path('send_note', send_note, name='note'),
    path('notes', NoteListView.as_view(), name='note_list'),
    path('note-create', NoteCreateView.as_view(), name='note_form'),
    path('detail/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note-update/<int:pk>', NoteUpdateView.as_view(), name='note_update_form'),
    path('note-delete/<int:pk>', NoteDeleteView.as_view(), name='note_confirm_delete')

]
