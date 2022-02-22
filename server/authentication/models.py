from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

## contains all the attributes of the sales dept employees persona

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    user_type = (
        ('s_admin', 'sales_admin'),
        ('s_representative', 'sales_representative'),
        ('none', 'None')
    )

    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=200, null=True, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_no = models.IntegerField(unique=True, null=True, blank=True)
    password = models.CharField(unique=True, blank=False, editable=True, max_length=100)
    user_type = models.CharField(blank=False, choices=user_type, default="None", max_length=100)
    user_bio = models.CharField(blank=True, max_length=300, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(blank=True, null=True)
    manager_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    # class Meta:
    #     permissions = (
    #         ("can_drive", "Can drive"),
    #         ("can_vote", "Can vote in elections"),
    #         ("can_drink", "Can drink alcohol"),
    #     )

    def __str__(self):
        return self.first_name


class Lead(models.Model):
    # Here we are defining the quality of the lead
    not_assigned = 'na'
    state = (
        ('hot', 'hot'),
        ('cold', 'cold'),
        ('med', 'med'),
        ('sold', 'sold'),
        ('na', 'na')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_no = models.IntegerField(unique=True, null=True, blank=True)
    state = models.CharField(default=not_assigned, choices=state, max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
