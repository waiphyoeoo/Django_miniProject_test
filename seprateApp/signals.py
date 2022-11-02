from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from seprateApp.models import Customer

def create_customer_profile(sender,instance,created,**kwargs):
    if created:
        gp=Group.objects.get(name='customer')
        instance.groups.add(gp)
        #create customerprofile foe each a user
        Customer.objects.create(user=instance,email=instance.email)

post_save.connect(create_customer_profile,sender=User)