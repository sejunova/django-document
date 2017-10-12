from django.db import models

__all__=(
    'Champion',
)

class Champion(models.Model):
    CHOICES_TYPE = (
        ('magician', '마법사'),
        ('supporter', '서포터'),
        ('ad carry', '원딜'),
    )
    champion_type = models.CharField(max_length=20, choices=CHOICES_TYPE)
    name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.get_champion_type_display()}'

