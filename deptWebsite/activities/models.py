from django.db import models

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=600)
    domain = models.CharField(max_length=800)
    details = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField(blank=True,null=True)
    cover_Image = models.ImageField(upload_to='activities')
    def __str__(self):
        return f"{self.title} : {self.id}"


class ActivityImage(models.Model):
    image = models.ImageField(upload_to='activities')
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE,related_name="images")