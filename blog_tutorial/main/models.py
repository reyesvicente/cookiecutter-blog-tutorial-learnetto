from django.db import models
from django.utils.translation import ugettext_lazy as _


STATUS_CHOICES = [
    ("d", "draft"),
    ("p", "published"),
    ("w", "withdrawn"),
]


class Project(models.Model):
    """ This model defines our Project class which will
        handles the portfolio of the user.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=140, default=title)
    image = models.ImageField(upload_to="projects/", blank=True)
    live_site = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title


class Category(models.Model):
    """ This model defines the categories field in the Post model
        with a ManyToManyField.
    """
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default=title)

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title


class Post(models.Model):
    """ The main model that defines the Post class which
        has a relationship with the Category class
    """
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default=title)
    overview = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title


class Contact(models.Model):
    """ The Contact model that accepts the name, email, and message
        on the contact page.
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, help_text="hi@example.com")
    message = models.TextField()

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.name