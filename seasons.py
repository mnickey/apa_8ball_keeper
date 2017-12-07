import os
import shutil

class seasons:
## CHECK FOR ARCHIVES FOLDER
    def archive_check():
        archives = os.path.dirname('Archives')
        if not os.path.exists('Archives'):
            os.makedirs('Archives')
## CREATE A SEASON FOLDER
    def season_start():
        season = input("What season are you starting? i.e.'Fall2017' > ")
        season_dir = os.path.dirname(season)
        if not os.path.exists(season):
            os.makedirs(season)
## ABILITY TO ARCHIVE A SEASON.JSON FILE
    def archive_season():
        season_to_archive = input("What season should we archive? i.e.'Fall2017' > ")
        shutil.copytree(season_to_archive, Archives)
        print("Moving ", season_to_archive, "to Archvies")
