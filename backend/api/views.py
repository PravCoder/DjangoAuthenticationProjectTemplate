from django.shortcuts import render
from django.contrib.auth.models import User  # import built-in user model change this to custom in models.py
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# inherit from built-in ciew that represents a collection of model instances, this view will list all of the notes user has created
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer  
    permission_classes = [IsAuthenticated]  # cannot call this route unless you are authenticated and pass a valid jwt-toekn
    
    def get_queryset(self):
        user = self.request.user  # get current authenticated-user-obj
        return Note.objects.filter(author=user)  # use that user to filter notes and get notes written by user

    def perform_create(self, serializer):
        if serializer.is_valid(): # if the data that was passed to serializer passed all checks, to create new note
            serializer.save(author=self.request.user)  # save serializer makes a new version of the note pass additional field author because it is read-only in serializer
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # get current authenticated-user-obj
        return Note.objects.filter(author=user)  # use that user to filter notes and get notes written by user
        

# inheri from built-in create-view which automaticall handels creating a new object
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # providing list exisitng users to view, so it doesn't create duplicate
 
    serializer_class = UserSerializer   # serializer-class tells view what kind of data we need to accept to create a new user

    permission_classes = [AllowAny]  # who can call this, anyone

