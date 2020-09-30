from django.db import models

# Create your models here.
class Article(models.Model):

    # 제목은 길이제한이 있는 문자열
    title = models.CharField(max_length=50)

    # 내용물은 길이제한이 없는 문자열
    content = models.TextField()

    # 처음 생성되는 순간 = 처음 add되는 순간
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정되는 순간 (save되는 모든 순간)
    updated_at = models.DateTimeField(auto_now=True)