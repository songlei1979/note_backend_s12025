from rest_framework import viewsets

from note_app.models import Note
from note_app.serialzers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer