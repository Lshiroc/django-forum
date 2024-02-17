from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    views = models.IntegerField(default=0)
    upvote = models.ManyToManyField('accounts.CustomUser', symmetrical=False, related_name='upvoted_posts')
    downvote = models.ManyToManyField('accounts.CustomUser', symmetrical=False, related_name='downvoted_posts')
    posted_by = models.ForeignKey('accounts.CustomUser', related_name='all_posts', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('posted_at', 'title', 'views',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    context = models.TextField()
    upvotes = models.ManyToManyField('accounts.CustomUser', symmetrical=False, related_name='upvoted_comments')
    downvotes = models.ManyToManyField('accounts.CustomUser', symmetrical=False, related_name='downvoted_comments')
    score = models.IntegerField(default=0)
    posted_by = models.ForeignKey('accounts.CustomUser', related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='all_comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('context',)
    
    def __str__(self):
        return self.context
    
    def save(self, *args, **kwargs):
        self.score = self.upvotes.count() - self.downvotes.count()
        super().save(*args, **kwargs)
