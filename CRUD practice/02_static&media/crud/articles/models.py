from django.db import models

# image resizing
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# delete media file
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Article(models.Model):

    # 제목은 길이제한이 있는 문자열
    title = models.CharField(max_length=50)

    # 내용물은 길이제한이 없는 문자열
    content = models.TextField()

    # 처음 생성되는 순간 = 처음 add되는 순간
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정되는 순간 (save되는 모든 순간)
    updated_at = models.DateTimeField(auto_now=True)

    # 이미지
    # blank=True : permit empty values in forms()
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality':90},
        upload_to='%Y/%m/%d/'
    )


# 글 삭제할 때 media폴더에 저장된 이미지도 삭제하기
@receiver(post_delete, sender=Article)
def on_delete(sender, instance, **kwargs):
    instance.image.delete(False)


# 수정하고 난 후 그 전에 media 폴더에 있던 이미지도 삭제하기
@receiver(pre_save, sender=Article)
def on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_img = sender.objects.get(pk=instance.pk).image
    
    except sender.DoesNotExist:
        return False

    new_img = instance.image
    if not old_img == new_img:
        old_img.delete(False)