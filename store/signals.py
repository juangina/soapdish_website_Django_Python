from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Customer

from django.core.mail import send_mail
from django.conf import settings

#sender-Model used that sent the post signal
#instance-Instance of the Model that sent the post signal
#created-Boolean to indicate whether this was get_or_create()
#**kwargs-miscellaneous keyword (key:value pair) arguments
#print('inside signal file') #debug file statement

@receiver(post_save, sender=Customer)
def createCustomer(sender, instance, created, **kwargs):
    #print('Instance: ', instance)
    if created:
        customer = instance

        subject = 'Welcome to Soapdish, ' + customer.name 
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            "soapdish@theaccidentallifestyle.net",
            ["ericrenee21@gmail.com"],
            fail_silently=False,
        )
        # print("Email Sent to Administrator.")


# def updateCustomer(sender, instance, created, **kwargs):
#     customer = instance
#     user = customer.user

#     if created == False:
#         user.first_name = customer.name
#         user.email = customer.email
#         user.save()


# def deleteCustomer(sender, instance, **kwargs):
#     try:
#         user = instance.user
#         user.delete()
#     except:
#         pass


# post_save.connect(createCustomer, sender=Customer)
# post_save.connect(updateCustomer, sender=Customer)
# post_delete.connect(deleteCustomer, sender=Customer)