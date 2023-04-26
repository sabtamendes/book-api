from .base import BaseSettings
from .db import TortoiseSettings
# .base e .db são os arquivos

config = BaseSettings()
tortoise_config = TortoiseSettings.generate()
