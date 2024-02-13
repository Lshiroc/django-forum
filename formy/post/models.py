from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField('Post', symmetrical=False, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    views = models.IntegerField(default=0)
    posted_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # using comma separated list of tags might a better approach
    tags = models.ManyToManyField(Tag, symmetrical=False, blank=True)

    class Meta:
        ordering = ('posted_at', 'title', 'views',)

    def __str__(self):
        return self.title

