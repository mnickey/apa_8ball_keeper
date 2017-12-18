import os
import shutil

class seasons:

    def archive_check():
        archives = os.path.dirname('Archives')
        if not os.path.exists('Archives'):
            os.makedirs('Archives')

    def season_start():
        current_season = input("What season are you starting? i.e.'Fall2017' > ")
        season_dir = os.path.dirname(current_season)
        if not os.path.exists(current_season):
            os.makedirs(current_season)

    def archive_season():
        season_to_archive = input("What season should we archive? i.e.'Fall2017' > ")
        shutil.copytree(season_to_archive, Archives)
        print("Moving ", season_to_archive, "to Archvies")
