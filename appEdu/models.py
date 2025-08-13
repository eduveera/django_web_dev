from django.db import models

class LeadSource(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class LeadStage(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)

    lead_source = models.ForeignKey(
        LeadSource,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.lead_source:
            try:
                self.lead_source = LeadSource.objects.get(name="Website")
            except LeadSource.DoesNotExist:
                self.lead_source = LeadSource.objects.create(name="Website")
        super().save(*args, **kwargs)

    lead_stage = models.ForeignKey(
        LeadStage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    consulted_by = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name if self.name else "Unnamed Enquiry"
