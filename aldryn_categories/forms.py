from treebeard.forms import movenodeform_factory, MoveNodeForm

from parler.forms import TranslatableModelForm
from django.utils.translation import get_language
from cms.forms.fields import PageSmartLinkField

from .models import Category

class PageSmartLinkFieldWithLang(PageSmartLinkField):

    def __init__(self, max_length=None, min_length=None, placeholder_text=None,
                 ajax_view=None, *args, **kwargs):
        self.placeholder_text = placeholder_text
        self.language = get_language()
        widget = self.widget(ajax_view=ajax_view)
        widget.language=self.language
        super(PageSmartLinkField, self).__init__(max_length, min_length,
                                                 widget=widget, *args, **kwargs)



class CategoryAdminForm(TranslatableModelForm, MoveNodeForm):
    landing_page = PageSmartLinkFieldWithLang(
        required=False,
        ajax_view='admin:cms_page_get_published_pagelist')


CategoryAdminForm = movenodeform_factory(Category, form=CategoryAdminForm)
