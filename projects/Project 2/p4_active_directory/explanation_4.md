## Active Directory

Since an AD group can contain both users and other groups, we need to recursively check each child group. When searching a group for a particular user, I first check the individual users that are direct members of the group. Then I get the list of groups in that group and recurse into each of those groups.

The time complexity of this search is O(n) where n is the total number of users in the entire Active Directory instance. This search doesn't require any additional storage.