from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

gender_list = [("male","male"),
               ("female","female")]

status_list = [("active","active"),
               ("inactive","inactive")]

class CATEGORY(models.Model):
    CAT_NAME = models.CharField(max_length=50)
    CAT_IMAGE = models.ImageField(upload_to="catphotos")

    def cat_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.CAT_IMAGE.url))
    cat_photo.allow_tags = True

    def __str__(self):
        return self.CAT_NAME

class ARTIST(models.Model):

    ARTIST_NAME = models.CharField(max_length=255)
    ARTIST_TYPE = models.CharField(max_length=255)
    ARTIST_IMAGE = models.ImageField(upload_to="artistimg")
    ARTIST_DOB = models.DateField()

    def artist_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.ARTIST_IMAGE.url))
    artist_photo.allow_tags = True

    def __str__(self):
        return self.ARTIST_NAME

class MUSIC(models.Model):
    CAT_ID = models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    SONG_TITLE = models.CharField(max_length=255)
    DURATION = models.CharField(max_length=255)
    ARTIST_ID = models.ForeignKey(ARTIST,on_delete=models.CASCADE)
    TIMESTAMP = models.DateTimeField(auto_now=True)
    SONG_YEAR = models.CharField(max_length=4)
    SONG_FILE = models.FileField(upload_to="songs",null=True)
    SONG_IMAGE = models.ImageField(upload_to="songimage")

    def song_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.SONG_IMAGE.url))
    song_photo.allow_tags = True

    def __str__(self):
        return self.SONG_TITLE

class REGISTER(models.Model):

    NAME = models.CharField(max_length=255)
    EMAIL = models.EmailField()
    PASSWORD = models.CharField(max_length=255)
    repassword = models.CharField(max_length=255, null=True)
    PHONE = models.BigIntegerField()
    DOB = models.DateField()
    DP = models.ImageField(upload_to="userimg")
    GENDER = models.CharField(choices=gender_list,max_length=255)

    def dp_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.DP.url))
    dp_photo.allow_tags = True

    def __str__(self):
        return self.NAME


class PLAYLIST(models.Model):

    PLAYLIST_NAME = models.CharField(max_length=255 ,null=True)
    USER_ID = models.ForeignKey(REGISTER,on_delete=models.CASCADE,null = True)
    SONG_ID = models.ForeignKey(MUSIC,on_delete=models.CASCADE , null=True)
    STATUS = models.CharField(choices=status_list,max_length=255, null=True)




