from django.db import models


# Create your models here.
class Musician(models.Model):
    # id = models.AutoField(primary_key=True) ## this is added by default even when it is not written
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
## the above code will creata atable as following
# CREATE TABLE appName_className (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );
##

class Album (models.Model):
    # id = models.AutoField(primary_key=True) ## this is added by default even when it is not written
    artist = models.ForeignKey(Musician, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    ## choices
    rating = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Not bad'),
        (4, 'Good'),
        (5, 'Excelent')
    )
    # <select>
    # <option value='1'>Worst</options>
    num_stars= models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ", Rating: " + self.get_num_stars_display()+ " " + str(self.num_stars)
