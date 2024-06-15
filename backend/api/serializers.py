from django.contrib.auth.models import User  # import built-in user-model
from rest_framework import serializers
from .models import Note

# serializer converts python-data into json-data vice versa

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "password"]  # fields we want to serialize
        extra_kwargs = {"password": {"write_only":True}}  # we want to accept password when creating a new user, do not want to return password when getting info about user. No one can read what the password is

    # handles creating user-obj, takes in dict of valid-data checked by serializer, makes sures fields-speciifed are valid
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # pass all of the data
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content","created_at","author"]
        extra_kwargs = {"author":{"read_only":True}} # we should be able to read who author is but not write it. Mannualy set who author is, someone cant just decide who the author is.
