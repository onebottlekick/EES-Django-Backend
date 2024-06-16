from django.db import models

class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)
    imageUrl = models.URLField(max_length=200, null=True)  # 이미지 URL 추가
    category = models.CharField(max_length=32, null=True)  # 카테고리 추가
    rating = models.FloatField(null=True)  # 평점 추가
    reviewCount = models.IntegerField(null=True)  # 리뷰 수 추가

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'review'