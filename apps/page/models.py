from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class CMSModel(models.Model):
    page_name = models.CharField(_("page_name"), max_length=50)
    page_slug = models.CharField(_("page_slug"), max_length=50, null=True, blank=True)
    section_name = models.CharField(_("section_name"), max_length=50)
    section_slug = models.CharField(_("section_slug"), max_length=50, null=True, blank=True)       
    header_title = models.CharField(_("Header Title"), max_length=100)
    title = models.CharField(_("Title"), max_length=150)
    sub_title = models.CharField(_("Sub Title"), max_length=200)

    # Regular text fields
    short_description = models.TextField(_("Short Description"), max_length=200)
    short_description_2 = models.TextField(_("Short Description"), max_length=200, null=True, blank=True)

    # Rich text fields
    description = RichTextField(_("Description"))
    content_block_1 = RichTextField(_("Primary Content Block"), blank=True, null=True)
    content_block_2 = RichTextField(_("Secondary Content Block"), blank=True, null=True)
    content_block_3 = RichTextField(_("Tertiary Content Block"), blank=True, null=True)

    # Buttons
    button_text_1 = models.CharField(_("Primary Button Text"), max_length=50, blank=True)
    button_url_1 = models.URLField(_("Primary Button URL"), max_length=200, blank=True)
    button_text_2 = models.CharField(_("Secondary Button Text"), max_length=50, blank=True)
    button_url_2 = models.URLField(_("Secondary Button URL"), max_length=200, blank=True)
    button_text_3 = models.CharField(_("Tertiary Button Text"), max_length=50, blank=True)
    button_url_3 = models.URLField(_("Tertiary Button URL"), max_length=200, blank=True)

    # Media
    media_1 = models.FileField(_("media_1"), upload_to='page/media/', max_length=100, blank=True)
    media_2 = models.FileField(_("media_2"), upload_to='page/media/', max_length=100, blank=True)
    media_3 = models.FileField(_("media_3"), upload_to='page/media/', max_length=100, blank=True)

    # Icons (e.g., FontAwesome or class names)
    icon_1 = models.CharField(_("icon_1 (FontAwesome class)"), max_length=100, blank=True)
    icon_2 = models.CharField(_("icon_2 (FontAwesome class)"), max_length=100, blank=True)
    icon_3 = models.CharField(_("icon_3 (FontAwesome class)"), max_length=100, blank=True)

    # Card 1
    card_1_title = models.CharField(_("card_1_title"), max_length=100, blank=True)
    card_1_description = models.TextField(_("card_1_description"), max_length=300, blank=True)
    card_1_icon = models.CharField(_("card_1_icon (FontAwesome class)"), max_length=100, blank=True)

    # Card 2
    card_2_title = models.CharField(_("card_2_title"), max_length=100, blank=True)
    card_2_description = models.TextField(_("card_2_description"), max_length=300, blank=True)
    card_2_icon = models.CharField(_("card_2_icon (FontAwesome class)"), max_length=100, blank=True)

    # Card 3
    card_3_title = models.CharField(_("card_3_title"), max_length=100, blank=True)
    card_3_description = models.TextField(_("card_3_description"), max_length=300, blank=True)
    card_3_icon = models.CharField(_("card_3_icon (FontAwesome class)"), max_length=100, blank=True)

# Additional fields for better organization
    is_active = models.BooleanField(_("is_active"), default=True)
    order = models.PositiveIntegerField(_("order"), default=0)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    class Meta:
        verbose_name = _("CMS Page")
        verbose_name_plural = _("CMS Pages")
        ordering = ['order', 'page_name']

    def save(self, *args, **kwargs):
        if not self.page_slug:
            self.page_slug = slugify(self.page_name)
        if not self.section_slug:
            self.section_slug = slugify(self.section_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.page_name} - {self.section_name}"