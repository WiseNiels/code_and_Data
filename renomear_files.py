import os

folder = "caminho/para/pasta"
for i, filename in enumerate(os.listdir(folder)):
    new_name = f"arquivo_{i}.txt"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))