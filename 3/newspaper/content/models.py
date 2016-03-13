from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()


class Image(Content):
    path = models.CharField(max_length=500)

    def get_info(self):
    	return "Title: " + self.title + ", Caption: " + self.subtitle + ", Path: " + str(self.pub_date)
    	
class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def die(self):
    	self.delete()