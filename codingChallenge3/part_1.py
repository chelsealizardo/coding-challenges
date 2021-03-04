# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
# 1. Simple directory tree
# # Replicate this tree of directories and subdirectories in the coding challenge 3 readme.md file

import os

# Create the directory
main_dir = "C:\Main_dir"
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
import shutil
shutil.rmtree(main_dir)

# Had a little issue with the fact that your main_dir was so deep, that I had to just create a single folder.
# your rmtree works for you if Main_dir is in the same folder as the script, not for me, so I merely used your
# main_dir variable to delete it.