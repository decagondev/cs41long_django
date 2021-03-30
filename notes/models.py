from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model): # Table in a database
    # each of the variables are columns in the table
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

