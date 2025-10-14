from django.contrib import admin
from .models import Video, Question, Choice, UserProgress, Category, Testimonial, NewsletterSubscriber

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class VideoAdmin(admin.ModelAdmin):
    # Adicionamos 'category' ao list_display e list_filter
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category', 'uploaded_at')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

# --- REGISTRO FINAL DOS MODELOS ---
admin.site.register(Video, VideoAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProgress)
admin.site.register(Category)
admin.site.register(Testimonial) 
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
admin.site.register(Choice)