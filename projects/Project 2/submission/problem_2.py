import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Handle edge case where path is a file, not a dir
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    path = os.path.abspath(path)  # Turn relative paths into absolute ones

    try:
        cwd_list = (os.listdir(path))  # Files in the dir currently being examined
    except(FileNotFoundError):
        return 'File not found'

    found_files = []  # List of files that match suffix

    for file in cwd_list:
        if os.path.isdir(os.path.join(path, file)):  # This file is really a dir, so recurse into it.
            subdir_files = find_files(suffix, path + '/' + file)
            for file in subdir_files:  # We'll get a list back, so iterate over it.
                if file.endswith(suffix):
                    found_files.append(file)
        elif file.endswith(suffix):  # This file is really a file, so check the suffix.
            found_files.append(file)

    return found_files


# Test cases
# Positive test cases
assert find_files('.c', './testdir/') == ['b.c', 't1.c', 'a.c', 'a.c']
assert find_files('.h', './testdir/') == ['b.h', 'a.h', 't1.h', 'a.h']

# No files found
assert find_files('.sh', './testdir/') == []

# Bad path
assert find_files('.c', './foo/') == 'File not found'

# Path is a file, not a dir. File suffix matches.
assert find_files('.py', './testdir/solution/solution2/solution2.py') == ['./testdir/solution/solution2/solution2.py']

# Path is a file, not a dir. File suffix does not match.
assert find_files('.html', './testdir/solution/solution2/solution2.py') == []

# Path is a file, not a dir. Invalid path.
assert find_files('.py', './testdir/solution/solution2/solution3.py') == 'File not found'

print('Tests passed')
