# fix_project.py
import os
import re


def normalize_imports():
    """标准化项目中的所有导入"""
    project_root = r"C:\Users\Administer\Desktop\PromptIR-main\PromptIR-main"

    # 1. 先把所有 image_utilss 改回 image_utils
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 修复导入语句
                content = re.sub(r'from .image_utils import', 'from .image_utils import', content)
                content = re.sub(r'from . import image_utils', 'from . import image_utils', content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    # 2. 重命名文件
    utils_dir = os.path.join(project_root, 'utils')
    if os.path.exists(os.path.join(utils_dir, 'image_utilss.py')):
        os.rename(
            os.path.join(utils_dir, 'image_utilss.py'),
            os.path.join(utils_dir, 'image_utils.py')
        )
        print("✅ 已重命名 image_utilss.py -> image_utils.py")

    if os.path.exists(os.path.join(utils_dir, 'dataset_utilss.py')):
        os.rename(
            os.path.join(utils_dir, 'dataset_utilss.py'),
            os.path.join(utils_dir, 'dataset_utils.py')
        )
        print("✅ 已重命名 dataset_utilss.py -> dataset_utils.py")

    print("✅ 修复完成！")


if __name__ == "__main__":
    normalize_imports()