from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership'
)


class Idol(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=30)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        # through_fields의 첫번째는 이게 정의된 모델의 field, 두번째는 target 모델의 field
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    ##idol_id로 Membership 테이블에 표현
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set')
    ##group_id로 Membership 테이블에 표현
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}의 ' \
               f'{self.idol.name}' \
               f'({self.is_active})'
