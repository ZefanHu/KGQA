import os

# 在Python中，当前脚本文件无法直接获取其父目录的路径。
# 因此，通过以下代码来定义文件所在目录的祖父级目录（上两级目录）和数据目录路径。
BASE_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
DATA_DIR = os.path.join(BASE_DIR, "data")