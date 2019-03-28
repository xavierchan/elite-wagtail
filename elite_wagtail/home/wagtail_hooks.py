from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from taggit.models import Tag
from home.models import ArticlePage


class TagAdmin(ModelAdmin):
    model = Tag
    menu_label = 'Tag'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 201  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', )
    list_filter = ('name',)
    search_fields = ('name', )


class ArticlePageAdmin(ModelAdmin):
    model = ArticlePage
    list_display = ('title', )
    list_filter = ('title',)


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(TagAdmin)
modeladmin_register(ArticlePageAdmin)
