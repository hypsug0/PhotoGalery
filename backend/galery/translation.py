from modeltranslation.translator import TranslationOptions, translator

from .models import Photo, Tags


class TagsTranslationOptions(TranslationOptions):
    fields = ("label",)


class PhotoTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Tags, TagsTranslationOptions)
translator.register(Photo, PhotoTranslationOptions)
