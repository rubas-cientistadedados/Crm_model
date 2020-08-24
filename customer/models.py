from django.db import models
from django.urls import reverse

class Customer(models.Model):
    firt_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.firt_name} {self.last_name}"
    
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"({self.firt_name}) {self.last_name}"

    def get_full_city(self):
        return f"({self.city}) - {self.state}"
    
    def get_absolute_url(self):
        return reverse("customer:customer_update", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("customer:customer_delete", kwargs={"id":self.id})

    class Meta:
        db_table = "customer"