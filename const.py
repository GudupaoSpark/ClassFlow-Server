"""
常量存储
"""

import os
import uuid
import hashlib
from encrypt.dh import DH

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

computer_id = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

dh = DH()