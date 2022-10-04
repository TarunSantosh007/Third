from django.core.management.base import BaseCommand
import pandas as pd


from app.models import movies 
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        df = pd.read_csv('new.csv')

        for NAME,YEAR,HERO,VILLIAN in zip(df.name,df.year,df.hero,df.villian):
            field = movies(name = NAME,year = YEAR, hero = HERO, villian = VILLIAN) 
            field.save()