import random
import string


def test_delete_group(app):
    group_name = random_name("group", 3)
    check_empty_group_list(app, group_name)
    old_list = app.groups.get_group_list()
    app.groups.delete_group(group_name)
    new_list = app.groups.get_group_list()
    old_list.remove(group_name)
    assert sorted(old_list) == sorted(new_list)
    

def check_empty_group_list(app, group_name):
    if len(app.groups.get_group_list()) <= 1:
        app.groups.add_group(group_name)


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])