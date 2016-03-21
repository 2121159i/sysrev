import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sysRevu.settings')
django.setup()

from sysrev.models import *
from sysrev.query_pubmed import *


def populate():
    add_user('jim', 'jim@gmail.com', 'jim', 'Jim', 'Jimsom')
    add_user('jill', 'jill@gmail.com', 'jill', 'Jill', 'Jillson')
    add_user('joe', 'joe@gmail.com', 'joe', 'Joe', 'Joeson')
    add_user('bob', 'bob@gmail.com', 'bob', 'Bob', 'Bobson')
    add_user('jen', 'jen@gmail.com', 'jen', 'Jen', 'Jenson')

    # final_user = add_user('jay', 'didi', 'didi', 'jonah', 'jameson')
    # add_review(final_user, "egss", 'egss', 'egss')


def add_review(researcher, title, description, query_string):
    review = Review(user=researcher, title=title, description=description, query_string=query_string)
    review.save()
    id_list = get_id_list(query_string)

    for id in id_list['Id']:
        Paper(review=review, pubmed_id=id).save()

    return review


def add_user(username, email, password, first_name, last_name):
    new_user = User.objects.get_or_create(username=username, email=email)[0]
    new_user.set_password(password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()

    researcher = Researcher.objects.get_or_create(user=new_user)[0]
    researcher.save()
    return researcher

# Start execution here!
if __name__ == '__main__':
    print "Starting SysRev population script..."
    populate()
    print "Done!"