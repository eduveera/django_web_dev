from django.db import models

class Enquiry(models.Model):
    LEAD_STAGE_CHOICES = [
        ('DROP NOT INTERESTED', 'DROP NOT INTERESTED'),
        ('BLANK', 'BLANK'),
        ('BUSY', 'BUSY'),
        ('SWITCH OFF', 'SWITCH OFF'),
        ('PROSPECT', 'PROSPECT'),
    ]

    LEAD_SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('LinkedIn', 'LinkedIn'),
        ('Instagram', 'Instagram'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    lead_source = models.CharField(
        max_length=100,
        choices=LEAD_SOURCE_CHOICES,
        default='Website',
        null=True,
        blank=True
    )
    lead_stage = models.CharField(
        max_length=100,
        choices=LEAD_STAGE_CHOICES,
        default='BLANK',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name if self.name else "Unnamed Enquiry"