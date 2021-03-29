from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    """
    table in a database;
    each variable models a column in the table
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    # time when note is added to database
    created_at = models.DateTimeField(auto_now_add=True)
    # time when last modified
    last_modified = models.DateTimeField(auto_now=True)

# create subclass of Note
class PersonalNote(Note):
    # link two tables and delete all notes of user when deteling a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
