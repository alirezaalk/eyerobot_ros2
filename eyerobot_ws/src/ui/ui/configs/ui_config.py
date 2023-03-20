import json
import logging
import os
from dataclasses import dataclass
# /home/alireza/projects/eyerobot-ros2/eyerobot_ws/src/ui/ui/configs/device_configs.json
@dataclass
class UiConfig:
    device_configs_json_path = os.path.join(
        os.environ['HOME'], 'projects', 'eyerobot-ros2', 'eyerobot_ws', 'src', 'ui' , 'ui', 'configs', 'device_configs.json')
    with open(device_configs_json_path) as device_file:
        dc = json.load(device_file)

    HOME_DIR: str = os.environ['HOME']

    # Device Specific Configurations
    PROJECT_DIR: str = HOME_DIR + '/projects' + '/eyerobot-ros2/' 
    UI_DIR : str = HOME_DIR + '/projects' + '/eyerobot-ros2' + '/eyerobot_ws' + '/src' + '/ui' + '/ui/'

    TIMEZONE: str = 'Europe/Berlin'
 
    CANVAS: int = dc['CANVAS']
    PARSE_OCT_VOL = dc['PARSE_OCT_VOLUME']
    # Directories
    
    CONFIGS_DIR: str = PROJECT_DIR + 'configs/'
    DATA_DIR: str = PROJECT_DIR + 'data/'
    TEST_DIR: str = PROJECT_DIR + 'test/'
    TEST_DATA_DIR: str = TEST_DIR + 'resources/'
    TEST_IMAGES_DIR: str = TEST_DATA_DIR + 'images/'
    # UI_DIR: str = PROJECT_DIR + 'eyerobot_ws/src/ui/ui/'
    TRANSLATE_DIR: str = UI_DIR + 'translations/'
    ICONS_DIR: str = UI_DIR + 'icons/'
    
    # TUBES_DIR: str = DATA_DIR + 'tubes/'
    # CAPS_DIR: str = DATA_DIR + 'caps/'
    TEMPLATE_DIR: str = DATA_DIR + 'templates/'
    # TUBE_IMAGE_DIR: str = PROJECT_DIR + 'tmp/'
    # os.makedirs(TUBE_IMAGE_DIR, exist_ok=True)
    # DEBUG_DIR: str = TUBE_IMAGE_DIR + 'debug/'
    # os.makedirs(DEBUG_DIR, exist_ok=True)
    LOG_DIR: str = PROJECT_DIR + 'logs/'
    os.makedirs(LOG_DIR, exist_ok=True)
    LOG_ARCHIVE_DIR: str = LOG_DIR + 'archive/'
    os.makedirs(LOG_ARCHIVE_DIR, exist_ok=True)



