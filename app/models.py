from django.db import models
from django.core.validators import FileExtensionValidator

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'uz'), (1, 'ru'), (2, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)

class Question(models.Model):
    index = models.IntegerField(null=True, blank=True, verbose_name='Индекс')
    text_uz = models.CharField(null=True, blank=True, max_length=1024, verbose_name='Текст (UZ)')
    text_ru = models.CharField(null=True, blank=True, max_length=1024, verbose_name='Текст (RU)')
    photo_uz = models.ImageField(
        null=True, blank=True, upload_to="question/photo/", verbose_name='Фото (UZ)',
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','bmp','gif'])]
        )
    photo_ru = models.ImageField(
        null=True, blank=True, upload_to="question/photo/", verbose_name='Фото (RU)',
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','bmp','gif'])]
        )
    video_uz = models.FileField(
        null=True, blank=True, upload_to="question/video/", verbose_name='Видео (UZ)',
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
        )
    video_ru = models.FileField(
        null=True, blank=True, upload_to="question/video/", verbose_name='Видео (RU)',
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
        )
    answer_uz = models.CharField(null=True, blank=True, max_length=255, verbose_name='Ответ (UZ)')
    answer_ru = models.CharField(null=True, blank=True, max_length=255, verbose_name='Ответ (RU)')
    help_uz = models.CharField(null=True, blank=True, max_length=255, verbose_name='Подсказка (UZ)')
    help_ru = models.CharField(null=True, blank=True, max_length=255, verbose_name='Подсказка (RU)')
    answer_similarity = models.IntegerField(null=True, blank=False, default=70, verbose_name='Сходства ответов')
    datetime = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True, verbose_name='Дата')

    def save(self, *args, **kwargs):
        if not self.index:
            size = len(Question.objects.all())
            self.index = size + 1
        return super(Question, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'