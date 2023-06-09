from django.db import models
from django.utils import timezone
from django.core import validators

# Create your models here.


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,
                            validators=[
                                validators.MinLengthValidator(3, "최소 3글자 이상은 입력해주셔야합니다.")
                            ])
    content = models.TextField("내용", validators=[
        validators.MinLengthValidator(10, "최소 10글자 이상은 입력해주셔야 합니다."),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} - {self.title}"
    
class Comment(models.Model):
    #id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255,
                                validators=[
                                    validators.MinLengthValidator(3, "최소 3글자 이상은 입력해주셔야합니다.")
                            ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
