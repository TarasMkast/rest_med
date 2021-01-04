from django.contrib import admin


class CustomModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False