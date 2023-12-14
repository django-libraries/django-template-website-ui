from django.db import models
from django.utils.translation import gettext_lazy as _


class WebsiteBase(models.Model):
    """
    Base model for Django Template Website UI.
    """
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_("Designates whether this data is active."),
    )
    create_time = models.DateTimeField(
        _("Create Time"),
        auto_now_add=True,
        help_text=_("Designates when this data was created."),
    )
    update_time = models.DateTimeField(
        _("Update Time"),
        auto_now=True,
        help_text=_("Designates when this data was last updated."),
    )

    class Meta:
        abstract = True
# Create your models here.
