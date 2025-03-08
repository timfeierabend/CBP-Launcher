
import os
import shutil

GAME_ID = '287450'
PROD_WORKSHOP_ID = '2287791153'
BETA_WORKSHOP_ID = '2528425253'

# Make the workshop dir path
os.makedirs(f'./steamapps/workshop/content/{GAME_ID}/{PROD_WORKSHOP_ID}',
            exist_ok=True)

# Make the pre-release workshop dir path
os.makedirs(f'./steamapps/workshop/content/{GAME_ID}/{BETA_WORKSHOP_ID}',
            exist_ok=True)

# Make the game dir path
os.makedirs('./steamapps/common/Rise of Nations', exist_ok=True)
