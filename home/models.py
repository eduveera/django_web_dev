from django.db import models

# Create your models here.

class Enquiry(models.Model):
    # Using tuples of (actual_value, human_readable_name) for choices
    LEAD_STAGE_CHOICES = [
        ('DROP_NOT_INTERESTED', 'Drop - Not Interested'),
        ('BLANK', 'Blank'),
        ('BUSY', 'Busy'),
        ('SWITCH_OFF', 'Switch Off'),
        ('PROSPECT', 'Prospect'),
    ]

    LEAD_SOURCE_CHOICES = [
        ('WEBSITE', 'Website'),
        ('LINKEDIN', 'LinkedIn'), # Corrected "Linkdin" to "LinkedIn"
        ('INSTAGRAM', 'Instagram'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    
    # Using the defined choices and providing a default
    lead_source = models.CharField(
        max_length=50, # A shorter max_length is usually sufficient for choices
        choices=LEAD_SOURCE_CHOICES,
        default='WEBSITE',
        null=True, 
        blank=True
    )
    
    # Using the defined choices
    lead_stage = models.CharField(
        max_length=50, # A shorter max_length is usually sufficient for choices
        choices=LEAD_STAGE_CHOICES,
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        # You might want to add ordering, e.g., ordering = ['-date_of_creation']
        # if you add a DateTimeField for creation date.

    def __str__(self):
        # Always good to have a string representation for Django Admin
        return self.name if self.name else f"Enquiry {self.pk}"