from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

   
def __str__(self):

        return f"{self.name} - {self.email} - {self.rating}"

from django.db import models
from django.contrib.auth.models import User

class VillageIssue(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    issue=models.TextField()

    media = models.FileField(
    upload_to='issues/',
    blank=True,
    null=True
    )

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

from django.db import models

class PanchayatGallery(models.Model):

    name = models.CharField(max_length=100)

    media = models.FileField(upload_to="panchayat_gallery/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FarmingGallery(models.Model):

    name = models.CharField(max_length=100)

    media = models.FileField(upload_to="farming_gallery/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TourismGallery(models.Model):

    name = models.CharField(max_length=100)

    media = models.FileField(upload_to="tourism_gallery/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SportsGallery(models.Model):

    name = models.CharField(max_length=100)

    media = models.FileField(upload_to="sports_gallery/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TempleGallery(models.Model):

    name = models.CharField(max_length=100)

    media = models.FileField(upload_to="temples_gallery/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        return f"{self.name} - {self.email} - {self.rating}"
