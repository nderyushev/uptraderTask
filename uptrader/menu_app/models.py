from django.db import models
from django.urls import reverse_lazy
from django.http import Http404


class MenuItem(models.Model):
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True,
        blank=True
    )
    name =  models.CharField(max_length=255)
    explicit_url = models.CharField(max_length=255, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []

    def save(self, *args, **kwargs):
        if self.named_url:
            url_chunks = self.named_url.split()
            url_name = self.named_url.split()[0]
            params = url_chunks[1:]
            reversed_named_url = reverse_lazy(url_name, args=params)
            if self.explicit_url:
                if self.explicit_url != reversed_named_url:
                    raise Http404('explicit_url does not match named_url')
            else:
                self.explicit_url = reversed_named_url
        else:
            self.named_url = f'item {self.id}' 
        super(MenuItem, self).save(*args, **kwargs)