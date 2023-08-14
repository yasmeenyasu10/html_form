from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.topic_name
    
class Web_page(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    urls=models.URLField()
    def __str__(self):
       return self.name
   
class Acess_record(models.Model):
    name=models.ForeignKey(Web_page,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self) -> str:
        return self.author
   
   
    