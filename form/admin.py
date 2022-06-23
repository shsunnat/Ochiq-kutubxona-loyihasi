from django.contrib import admin
from .models import Bolim, Til, Form, KitobShakli, Comment


# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Bolim)
admin.site.register(Til)
admin.site.register(Form, PostAdmin)
admin.site.register(KitobShakli)
