# Instagram...?

### Add media root for save images

```bash
$ pip install django-imagekit
```

```python
# in settings.py
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# in insta/urls.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Image processing in python

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