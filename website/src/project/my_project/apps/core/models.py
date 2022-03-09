from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


RATING_CHOICES = (
 (1, "★☆☆☆☆"),
 (2, "★★☆☆☆"),
 (3, "★★★☆☆"),
 (4, "★★★★☆"),
 (5, "★★★★★"),
)

class MetaTagsBase(models.Model):
    meta_keywords = models.CharField(max_length=255, blank=True,help_text='"Separate keywords with commas')
    meta_description = models.CharField(max_length=255,blank=True)
    
    class Meta:
        abstract = True

    def get_meta_field(self, name, content):
        tag = ""
        if name and content:
            tag = render_to_string("core/includes/meta_field.html",{"name":name,"content":content})
        
        return mark_safe(tag)

    def get_meta_keywords(self):
        return self.get_meta_field("keywords", self.meta_keywords)

    def get_meta_description(self):
        return self.get_meta_field("description", self.meta_description)

    def get_meta_tags(self):
        return mark_safe("\n".join((
            self.get_meta_keywords(),
            self.get_meta_description(),
        )))

    '''
    for use enogh inheritance this class in your model
    and full fields then your html call back
    
    {% block meta_tags %}
    {{ block.super }}
    {{ your_context_object.get_meta_tags }}
    {% endblock %}
    '''