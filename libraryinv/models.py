from django.db import models


# Create your models here.
class Location(models.Model):
    ASHEVILLE = 'ASH'
    ATLANTA = 'ATL'
    AUSTIN = 'AUS'
    BIRMINGHAM = 'BHM'
    BOSTON = 'BOS'
    COLUMBIA = 'COL'
    DALLAS = 'DAL'
    DENVER = 'DEN'
    ENCINO = 'ENC'
    FAIRFAX = 'FAR'
    GREENVILLE = 'GRE'
    JACKSONVILLE = 'JAC'
    KANSAS_CITY = 'KAS'
    MACON = 'MAC'
    MADISON = 'MAD'
    NASHVILLE = 'NAS'
    NEW_YORK = 'NYC'
    OPELIKA = 'OPE'
    PRINCETON = 'PRI'
    ST_LOUIS = 'STL'
    TAMPA = 'TAM'
    WINSTON_SALEM = 'WSA'

    LOCATION_CHOICES = (
        (ASHEVILLE, 'Asheville'),
        (ATLANTA, 'Atlanta'),
        (AUSTIN, 'Austin'),
        (BIRMINGHAM, 'Birmingham'),
        (BOSTON, "Boston"),
        (COLUMBIA, "Columbia"),
        (DALLAS, 'Dallas'),
        (DENVER, 'Denver'),
        (ENCINO, 'Encino'),
        (FAIRFAX, 'Fairfax'),
        (GREENVILLE, 'Greenville'),
        (JACKSONVILLE, 'Jacksonville'),
        (KANSAS_CITY, 'Kansas City'),
        (MACON, 'Macon'),
        (MADISON, 'Madison'),
        (NASHVILLE, 'Nashville'),
        (NEW_YORK, 'New York'),
        (OPELIKA, 'Opelika'),
        (PRINCETON, 'Princeton'),
        (ST_LOUIS, 'St. Louis'),
        (TAMPA, 'Tampa'),
        (WINSTON_SALEM, 'Winston-Salem'),
    )
    location = models.CharField(max_length=3,
                                choices=LOCATION_CHOICES,
                                default=ATLANTA)

    def __unicode__(self):
        return self.location


class Publisher(models.Model):
    # How to access a reverse relationship on a foreign key:  publisher.publication_set.all()
    publisher = models.CharField(max_length=150, primary_key=True, unique=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    location = models.ForeignKey(Location, default= 'ATL')

    def __unicode__(self):
        return self.publisher


class Publication(models.Model):
    BOOK = 'B'
    SUBSCRIPTION = 'S'

    SUBSCRIPTION_CHOICES = (
        (BOOK, 'Book'),
        (SUBSCRIPTION, 'Subscription'),
    )

    # How to access a foreign key:  publication.publisher
    publication_title = models.CharField(max_length=200, null=True, blank=True)
    publication_number = models.CharField(max_length=50, null=True, blank=True)
    publication_type = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, default=SUBSCRIPTION)
    location = models.ForeignKey(Location)
    price = models.FloatField()

    def __unicode__(self):
        return self.publication_title

class Line(models.Model):
    title = models.ForeignKey(Publication)
    price = models.FloatField()
    version = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.FloatField()

    def __unicode__(self):
        return self.title


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=150)
    price = models.ForeignKey(Line)
    tax = models.FloatField()
    shipping = models.FloatField()
    total = models.FloatField()
    date_purchased = models.DateField()
    order_type = models.CharField(max_length=50)
    date_sent_acctg = models.DateField()

    def __unicode__(self):
        return self.invoice_number



# One way of organizing:
# Publisher
# Publication -> has a Publisher
# Line -> has a Publication, records quantity, price, etc.
# Invoice -> has Lines, records total price, shipping, date, etc.