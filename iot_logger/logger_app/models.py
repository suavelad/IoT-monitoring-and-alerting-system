from django.db import models
import uuid

# Create your models here.

class Log(models.Model):
    LEVEL_TYPE =(
        ('debug','debug'),
        ('info','info'),
        ('warning','warning'),
        ('error','error'),
        ('critical','critical')
    )
    id = models.AutoField(primary_key=True)
    device_id = models.UUIDField(default=uuid.uuid4,editable =False,blank=True,null=True)
    location_id = models.UUIDField(default=uuid.uuid4,editable =False,blank=True,null=True)
    message_id = models.UUIDField(default=uuid.uuid4,editable =False,blank=True,null=True)
    message =models.TextField(blank=True,null=True)  
    level = models.CharField(max_length=20, choices=LEVEL_TYPE,blank=True,null=True)
    timestamp = models.TextField(blank=True,null=True)
    mqtt_topic = models.CharField(max_length=255,blank=True,null=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> int:
        return self.id
