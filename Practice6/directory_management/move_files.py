import shutil
import os

os.makedirs("test_dir", exist_ok=True)

shutil.move("sample.txt", "test_dir/sample.txt")

shutil.copy("test_dir/sample.txt", "sample_copy.txt")