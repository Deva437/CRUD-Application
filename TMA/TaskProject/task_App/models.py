from django.db import models

class Mainclass(models.Model):
    priority =[ 
        ('','none'),
        ("high","high"),
        ("medium","medium"),
        ("low","low"),

    ]
    status = [
        ('','none'),
        ("inproces","inproces"),
        ("pending"," pending"),
        ("complete","complete"),
    ]

    task_title =models.CharField(max_length=500,null=True)
    task_description = models.TextField(max_length=200)
    task_priority = models.CharField(max_length=106, choices=priority, default='none')
    task_status = models.CharField(max_length=106, choices=status, default='none')
    task_image=models.ImageField(upload_to='img/')
    
    
    def _str_(self):
        return self.task_title