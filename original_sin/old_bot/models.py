from django.db import models


class VkUser(models.Model):
    user_id = models.IntegerField(
        'id пользователя',
        blank=False, null=False,
        unique=True,
    )
    HOME = 0
    SPECIALIST = 1
    INCOMING = 2
    QUEST = 3
    CONTACTS = 4
    status = models.IntegerField(
        'текущей статус общения с ботом',
        blank=False, null=False,
        default=HOME
    )

    def set_default(self):
        self.status = self.HOME
        self.save()

    def __str__(self):
        return '{} <id:{}>'.format(self.__class__.__name__, self.user_id)

    def get_quest_data(self):
        quest_profile = self.quest_profile.all().first()
        return quest_profile and quest_profile.data

    def get_incoming_data(self):
        incoming_profile = self.incoming_profile.all().first()
        return incoming_profile and incoming_profile.status


class QuestProfile(models.Model):
    user = models.ForeignKey(
        VkUser,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
        related_name='quest_profile'
    )

    data = models.TextField(
        verbose_name='Json с прогрессом',
        null=True, blank=True,
    )


class IncomingProfile(models.Model):
    user = models.ForeignKey(
        to=VkUser,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
        related_name='incoming_profile'
    )
    HOME = 0
    ADMISSION = 1
    status = models.IntegerField(
        'Статус общения',
        blank=False, null=False,
        default=HOME
    )

    def set_default(self, full=False):
        self.status = self.HOME
        self.save()
        if full:
            self.user.set_default()


class GameProfile(models.Model):
    """ Игровой профиль """
    user = models.ForeignKey(
        VkUser,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )

    some_data = models.TextField('JSON фигня', default='{}')

    def __str__(self):
        return self.__doc__ + ':' + str(self.user)
