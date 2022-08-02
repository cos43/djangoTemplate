from django.db import models
from DjangoUeditor.models import UEditorField
from django_jsonform.models.fields import JSONField


class Editor(models.Model):
    description = UEditorField(
        verbose_name='描述', height=700, width="100%",
        default="",
        toolbars='full'
    )


class ShoppingList(models.Model):
    ITEMS_SCHEMA = {
        'type': 'array',  # a list which will contain the items
        'items': {
            'type': 'string'  # items in the array are strings
        }
    }
    DICT_SCHEMA = {
        'type': 'dict',
        'keys': {
            'name': {'type': 'string'},
        },
        'addtionalProperties': True,
        'additionalProperties': {'type': 'string'}
    }

    items = JSONField(schema=ITEMS_SCHEMA)
    data = JSONField(schema=DICT_SCHEMA, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



