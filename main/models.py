from django.db import models

from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cars(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='cars')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, default=996)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    description = models.TextField()

    def __str__(self):
        return self.title

class CarsImage(models.Model):
    image = models.ImageField(upload_to='cars', blank=True, null=True)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='images')


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('created',)


class Like(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes')
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='likes')
    likes = models.BooleanField(default=False)

    def __str__(self):
        return self.likes

class Rating(models.Model):
        author = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE, related_name='rating')
        cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='rating')
        rating = models.SmallIntegerField()


class Favorite(models.Model):
    author = models.ForeignKey(MyUser, default='', on_delete=models.CASCADE, related_name='favorite')
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='favorite')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.favorite