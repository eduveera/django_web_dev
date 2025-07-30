from django.db import models

# Create your models here.

class Enquiry(models.Model):
    lead_stage_type = [
        ('DROP NOT INTERESTED', 'DROP NOT INTERESTED'),
        ('BLANK', 'BLANK'),
        ('BUSY', 'BUSY'),
        ('SWITCH OFF', 'SWITCH OFF'),
        ('PROSPECT', 'PROSPECT'),
    ]

    lead_source_type = [
        ('Website', 'Website'),
        ('Linkdin', 'Linkdin'),
        ('Instagram', 'Instagram'),
    ]
    
    name = models.CharField(max_length=100, null=False),
    email = models.EmailField(null=False),
    phone = models.BigIntegerField(null=False),
    date_of_birth = models.DateField(null=False),
    university = models.CharField(max_length=100, null=False),
    course = models.CharField(max_length=100, null=False),
    lead_source = models.CharField(max_length=100, choices=lead_source_type, default='Website'),
    lead_stage = models.CharField(max_length=100, choices=lead_stage_type),


def __str__(self):
        return self.name

    
    

