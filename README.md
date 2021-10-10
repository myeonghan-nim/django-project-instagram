# Project: instagram

## media root

```bash
$ pip install pillow django-imagekit
```

```python
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Image processing

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Feed(models.Model):
    image = ProcessedImageField(
                processors=[ResizeToFill(300, 300)],
                format='PNG',
                options={'quality': 100},
                upload_to='feeds'
            )
```
