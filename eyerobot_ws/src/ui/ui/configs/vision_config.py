import json
import os
from dataclasses import dataclass

@dataclass
class VisionConfig:
    vision_config_json_path = os.path.join ('home','alireza', 'eyerobot_ros2', 'eyerobot_ws', 'src', 'ui', 'ui', 'configs', 'vision_config.json')
    with open ('/home/alireza/projects/eyerobot-ros2/eyerobot_ws/src/ui/ui/configs/vision_config.json') as vision_file: 
        vc = json.load(vision_file)
        FRAMRATE: int = vc['FRAMERATE']
        CAMERA : int = vc ['CAMERA']
