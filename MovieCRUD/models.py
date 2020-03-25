from djongo  import models
from django import forms

#embeded actors
class actor(models.Model):
    fullname=models.CharField('Full name:', max_length=100  )
    
    class Meta:
        abstract=True
    def __str__(self):
        return self.name

class actorForm(forms.ModelForm):
    class Meta:
        model=actor
        fields=('fullname',)

#embeded genres
class genre(models.Model):
    genreFilm=models.CharField('Genre film:',max_length=100)
    class Meta:
        abstract=True
    def __str__(self):
        return self.name

class genreForm(forms.ModelForm):
    class Meta:
        model=genre
        fields=('genreFilm',)

#embeded rating
class Rating(models.Model):
    ratingValue = models.IntegerField('Rating value:')

    class Meta:
        abstract = True

rate=[('1',1),
      ('2',2),
      ('3',3),
      ('4',4),
      ('5',5),
      ('6',6),
      ('7',7),
      ('8',8),
      ('9',9),
      ('10',10)]


class ratingForm(forms.ModelForm):
    #Rating=forms.ChoiceField(label='Rate:',choices=rate, required=False, widget=forms.RadioSelect())
    class Meta:
        model=Rating
        fields=('ratingValue',)

#Content rating
class contentRate(models.Model):
    content=models.TextField('Rating content:')
    class Meta:
        abstract=True

class contentRateForm(forms.ModelForm):
    class Meta:
        model = contentRate
        fields = (
            'content',
        )

#movies class
class moviesintheaters(models.Model):
#    id              =models.CharField(max_length=120)
    title           =models.CharField(max_length=120)
    year            =models.CharField(max_length=4)

    genres          =models.ArrayField(model_container=genre)
    ratings         =models.ArrayField(model_container=Rating)
   
    poster          =models.CharField(max_length=120)
    contentRating   =models.ArrayField( model_container=contentRate)

    duration        =models.CharField(max_length=120)
    releaseDate     =models.CharField(max_length=120)
    averageRating   =models.FloatField(null=True, blank=True, default=None)

    storyline       =models.TextField()
    actors          =models.ArrayField(model_container=actor)

    imdbRating      =models.FloatField()
    posterurl       =models.CharField(max_length=200)
    
    objects         = models.DjongoManager()
    #pdobjects=DataFrameManager()
    def __str__(self):
        return self.title
   
# Create your models here.
