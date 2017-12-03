from django.db import models

# topic and response are almost identical, refactor later?


class Text(models.Model):
    topic_field = models.CharField(max_length=30)
    text_field = models.CharField(max_length=500)
    score = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.user', related_name='texts', on_delete=models.CASCADE)
    text_response = models.ForeignKey('Text', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
