from django.db import models

class course(models.Model):
    title = models.CharField(max_length=200)
    Link = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
