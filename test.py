
import os
import shutil
import argparse

GAME_ID = '287450'
WORKSHOP_ID = '2287791153'

def build_dir():
    # Make the workshop dir path
    os.makedirs(f'./steamapps/workshop/content/{GAME_ID}/{WORKSHOP_ID}',
                exist_ok=True)

    # Make the game dir path
    os.makedirs('./steamapps/common/Rise of Nations', exist_ok=True)

def clean():
    shutil.rmtree('./steamapps')

parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['build', 'clean'])
args = parser.parse_args()

if args.action == 'build':
    build_dir()
elif args.action == 'clean':
    clean()




