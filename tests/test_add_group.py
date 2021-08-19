#import random
#import string


def test_add_group(app, xlsx_groups):
    group_list = xlsx_groups
    #group_name = random_name("group", 3)
    old_list = app.groups.get_group_list()
    app.groups.add_group(group_list)
    new_list = app.groups.get_group_list()
    old_list.append(group_list)
    assert sorted(old_list) == sorted(new_list)


#def random_name(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits
#    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])