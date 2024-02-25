from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    # photos = models.ImageField(max_length=1000)

    def __str__(self):
        return self.title
    