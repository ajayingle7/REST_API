from django.db import models

# Create your models here.


class Order(models.Model):
    oid = models.IntegerField()
    oname = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    mfg = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.oid}--{self.oname}--{self.status}--{self.mfg}"