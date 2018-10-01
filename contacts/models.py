from django.db import models


class Contact(models.Model):
    GENDER_MAN = 0
    GENDER_FEMALE = 1
    CHOICES_GENDER = (
        (GENDER_MAN, 'man'),
        (GENDER_FEMALE, 'female')
    )

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.SmallIntegerField(choices=CHOICES_GENDER)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return 'contact', (), {'pk': self.pk}
