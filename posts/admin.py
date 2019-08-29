from django.contrib import admin
from .models import Post, Answer, Questions

# Register your models here.
from django.db.models import Sum
from .models import Answer


admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Questions)





class AnswerAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        total = Answer.objects.aggregate(total=Sum('answer'))['total']
        context = {
            'total': total,
        }
        return super(AnswerAdmin, self).changelist_view(request, extra_context=context)


