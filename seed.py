from models import *
from faker import Faker
fake = Faker()

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
