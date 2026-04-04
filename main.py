import os , shutil

file_path = r"C:\Users\ASUS\OneDrive\Desktop\org"

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

def get_new_name(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name

listfiles = os.listdir(file_path)

for file in listfiles:
    current_file_path = os.path.join(file_path,file)
    if os.path.isdir(current_file_path):      #if current path is folder it skips.
        continue
    _, extracted_file_name = os.path.splitext(file)
    moved = False

    for folder, extensions in file_types.items():
        if extracted_file_name.lower() in extensions:
            target_folder = os.path.join(file_path, folder)
            os.makedirs(target_folder, exist_ok=True)

            new_file = get_new_name(target_folder, file)
            shutil.move(current_file_path, os.path.join(target_folder, new_file))
            moved = True
            break

    if not moved:
        other_folder = os.path.join(file_path, "Others")
        os.makedirs(other_folder, exist_ok=True)
        new_file = get_new_name(other_folder, file)
        shutil.move(current_file_path, os.path.join(other_folder, new_file))
print("Files Organized Successfully")

