from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=200)
    enable = models.BooleanField()
    description = models.CharField(max_length=1000)
    position = models.IntegerField()

    class Meta:
        db_table = 'roles'
        ordering = ['id']

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    roles = models.ForeignKey(Role, db_column = "role_id", to_field = "id", on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'
        ordering = ['id']

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)
    parent = models.IntegerField(name='parent_id')
    permission = models.CharField(max_length=200)
    enable = models.BooleanField()
    type = models.BooleanField()

    class Meta:
        db_table = 'resource'
        ordering = ['id']

    def __str__(self):              # __unicode__ on Python 2
        return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline