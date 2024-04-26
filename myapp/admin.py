from django.contrib import admin
from .models import CATEGORY , ARTIST , MUSIC , REGISTER , PLAYLIST
# Register your models here.

class showcat(admin.ModelAdmin):
    list_display = ["CAT_NAME","cat_photo"]

admin.site.register(CATEGORY,showcat)


class showart(admin.ModelAdmin):
    list_display = ["ARTIST_NAME", "ARTIST_TYPE", "artist_photo", "ARTIST_DOB"]


admin.site.register(ARTIST , showart)


class showmusic(admin.ModelAdmin):
    list_display = ["CAT_ID", "SONG_TITLE", "DURATION", "ARTIST_ID", "TIMESTAMP", "SONG_YEAR", "song_photo","SONG_FILE"]


admin.site.register(MUSIC, showmusic)


class showuser(admin.ModelAdmin):
    list_display = ["NAME", "EMAIL", "PASSWORD", "PHONE", "DOB", "GENDER", "DP"]


admin.site.register(REGISTER, showuser)


class showplaylist(admin.ModelAdmin):
    list_display = ["USER_ID", "SONG_ID", "STATUS"]


admin.site.register(PLAYLIST, showplaylist)
