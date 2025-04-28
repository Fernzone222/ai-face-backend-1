import os

def save_file(file_content, filename):
    path = os.path.join('uploads', filename)
    with open(path, 'wb') as f:
        f.write(file_content)
    return path
