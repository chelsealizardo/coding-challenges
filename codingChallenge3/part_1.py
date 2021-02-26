# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
# 1. Simple directory tree
# # Replicate this tree of directories and subdirectories in the coding challenge 3 readme.md file

import os

# Create the directory
main_dir = "C:\data\codingChallenge3\Main_dir"
os.mkdir(main_dir)

# Now make folders
first_level = ["draft_code", "includes", "layouts", "site"]

for folder in first_level:
    os.mkdir(os.path.join(main_dir, folder))

second_level = ["pending", "complete"]

for folder in second_level:
    os.mkdir(os.path.join(main_dir, "draft_code", folder))

third_level = ["default", "post"]

for folder in third_level:
    os.mkdir(os.path.join(main_dir, "layouts", folder))

posted = ["posted"]

for folder in posted:
    os.mkdir(os.path.join(main_dir, "layouts\post", folder))

# delete all folders
# import shutil
# shutil.rmtree("Main_dir")