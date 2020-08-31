## File recursion 

Listing regular files is easy. The tricky part is following nested directories to explore an entire filesystem.

I used a for loop to iterate over the regular files and recursion to dive into each nested layer of folders.

The time complexity is O(n) where n is the number of files (in the Unix sense where regular files and directories are all files). The space complexity is also O(n) in the edge case where every file in the directory structure matches our search pattern.