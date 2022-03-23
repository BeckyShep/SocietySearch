import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocietySearchProject.settings')

import django
import datetime

django.setup()
# from societysearch.models import User, GeneralUserProfile, SocietyAdminUserProfile, SocietyPage, Reviews
from societysearch.models import SocietyPage, Reviews


def populate():
    reviews = [
        {'review': 'This Society was great', 'likes': 5},
        {'review': 'This Society was ok', 'likes': 3},
        {'review': 'This Society was bad', 'likes': 1},
        {'review': 'This Society was amazing', 'likes': 10},
        {'review': 'This Society was very entertaining', 'likes': 7},
    ]

    Socities = [
        {'name': 'Judo',
         'availability': 'Every Thursdays',
         'nextEvent': 'Thursdays',
         'description': 'bla bla bla'},
        {'name': 'Computing',
         'availability': 'Every Thursdays',
         'nextEvent': 'Thursdays',
         'description': 'bla bla bla'},
        {'name': 'BasketBall',
         'availability': 'Every Thursdays',
         'nextEvent': 'Thursdays',
         'description': 'bla bla bla'},
        {'name': 'Football',
         'availability': 'Every Thursdays',
         'nextEvent': 'Thursdays',
         'description': 'bla bla bla'},
        {'name': 'Engineering',
         'availability': 'Every Thursdays',
         'nextEvent': 'Thursdays',
         'description': 'bla bla bla'}
    ]

    # user = add_user()
    # admin = add_society_admin(user)
    x = 0
    for soc in Socities:
        s = add_society(soc['name'], soc['availability'], soc['nextEvent'], soc['description'])
        for rev in reviews:
            add_review(rev['review'], s, rev['likes'])


# def add_user():
#     user = User.objects.get_or_create(is_societyAdmin=True)[0]
#     user.save()
#     return user
#
#
# def add_society_admin(user):
#     admin = SocietyAdminUserProfile.get_or_create(societyAdminUser=user, university='Glasgow')
#     admin.save()
#     return admin


def add_society(name, availability, nextEvent, description):
    society = SocietyPage.objects.get_or_create(name=name, availability=availability, nextEvent=nextEvent,
                                                description=description, facebook='facebook.com', twitter='twitter.com',
                                                discord='https://discord.com/', slug=name)[0]
    society.save()
    return society


def add_review(review, society, likes):
    review = Reviews.objects.get_or_create(review=review, society=society, likes=likes, date=datetime.date.today())[0]
    review.save()


if __name__ == '__main__':
    print('Starting Society population script...')
    populate()
