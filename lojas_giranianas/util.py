from django.template.defaultfilters import slugify

def gerar_slug(model, instance, to_slug_attr='nome'):
    to_slug = getattr(instance, to_slug_attr)
    slug = slugify(to_slug)
    novo_slug = slug
    contador = 1
    while model.objects.filter(slug=novo_slug).exclude(pk=instance.pk).count() > 0:
        novo_slug = '%s-%d' %(slug, contador)
        contador += 1
    instance.slug = novo_slug
