import os


def create_gallery_dirs(parent_dir):
    for root, dirs, files in os.walk(parent_dir):
        gallery_path = os.path.join(root, ".gallery")
        if not os.path.exists(gallery_path):
            os.mkdir(gallery_path)
            print(f"Created .gallery directory in: {root}")


# Example usage: B:\dolphin\photos\DarkRoomVR
create_gallery_dirs("B:/dolphin/photos/DarkRoomVR")
