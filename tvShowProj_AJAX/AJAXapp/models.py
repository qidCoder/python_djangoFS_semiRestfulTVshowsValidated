from django.db import models
from datetime import date, datetime#to use the current date

# Create your models here.
#validator
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # ADDING A NEW SHOW:
        # all fields are required
        # title should be at least 2 characters
        if (len(postData['title']) < 2):
            errors['title'] = "Title should be at least 2 characters"

        # Network should be at least 3 characters
        if (len(postData['network']) < 3):
            errors['network'] = "Network should be at least 3 characters"

        # Description should be at least 10 characters
        # if (len(postData['desc']) < 10):
        #     errors['desc'] = "Description should be at least 10 characters"

        # a date is required
        if (postData['date'] == ''):
            errors['date'] = "Please enter a date"

        # Bonus: Release date should be in the past
        # need to import datetime and date
        else:
            convert_date = datetime.strptime(str(postData['date']), '%Y-%m-%d').date()
            if (convert_date > date.today()):
                errors['date'] = "Please enter a date in the past"        

        # Bonus: Description is optional, but if present must be at least 10 characters
        if (postData['desc'] != ''):   
            if (len(postData['desc']) < 10):
                errors['desc'] = "Description should be at least 10 characters"
                        
        # Bonus: Title should be unique
        if Show.objects.filter(title=postData['title']):
            errors['title'] = "duplicate title"

        return errors

        # SENSEI BONUS: Do uniqueness validations (including displaying errors) for creating and updating using AJAX! -----see duplicate project for implementation

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255, default='')
    release_date = models.DateField(blank=True, null=True)#these attributes ensure that a date must be entered
    desc = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #adding validations
    objects = ShowManager()
