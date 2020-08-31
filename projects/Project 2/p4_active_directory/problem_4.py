class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # Check for presence of user at this level
    if user in group.get_users():
        return True

    # Recurse into child groups to check if the user exists there
    for child_group in group.get_groups():
        return is_user_in_group(user, child_group)

    return False


# Test setup - Create groups
parent = Group('parent')
child_1 = Group('child_1')
child_2 = Group('child_2')
sub_child_1_1 = Group('subchild_1_1')
sub_child_2_1 = Group('subchild_2_1')
sub_child_2_2 = Group('subchild_2_2')

# Test setup - Add users to groups
for group in [parent, child_1, child_2, sub_child_1_1, sub_child_2_1, sub_child_2_2]:
    for i in range(4):
        group.add_user(group.name + '_user_' + str(i))

# Test setup - Add groups to parent groups
child_1.add_group(sub_child_1_1)
child_2.add_group(sub_child_2_1)
child_2.add_group(sub_child_2_2)
parent.add_group(child_1)
parent.add_group(child_2)

# Test 1 - Find a user in this group
assert is_user_in_group('parent_user_3', parent)
assert is_user_in_group('child_1_user_1', child_1)
assert is_user_in_group('subchild_2_2_user_3', sub_child_2_2)

# Test 2 - Find user that doesn't exist anywhere
assert not is_user_in_group('not_found_user', parent)
assert not is_user_in_group('not_found_user', child_1)
assert not is_user_in_group('not_found_user', sub_child_1_1)

# Test 3 - Find a user in a child group
assert is_user_in_group('subchild_1_1_user_3', parent)
assert is_user_in_group('subchild_1_1_user_3', child_1)
assert is_user_in_group('subchild_1_1_user_3', sub_child_1_1)

# Test 4 - Find a user that exists, but in a different group
assert not is_user_in_group('subchild_1_1_user_3', child_2)
assert not is_user_in_group('subchild_1_1_user_3', sub_child_2_1)

print('Tests passed.')
