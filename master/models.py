# models.py

from django.db import models

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_no = models.IntegerField(unique=True)
    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=5)

    def __str__(self):
        return self.state_name
    


## masters of customer

from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_type = models.CharField(max_length=100)
    preference_string = models.TextField()

    def __str__(self):
        return f"{self.customer_id} - {self.customer_type}"
