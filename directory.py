import os

def get_directory_hierarchy(directory):
    hierarchy = []
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, "", 1).count(os.sep)
        indent = "  " * level
        for name in dirs:
            hierarchy.append(f"{indent}|- {name}")
        for name in files:
            hierarchy.append(f"{indent}|- {name}")
    return "\n".join(hierarchy)

# Replace "your_directory_path" with the actual path to your folder
directory_path = r"C:\Users\LENOVO\Desktop\Spectro Mobile\SpectroMobile"  # Use raw string literal
hierarchy_text = get_directory_hierarchy(directory_path)

# Get the current working directory (where directory.py is present)
current_dir = os.getcwd()

# Construct the full path to the output file
output_file = os.path.join(current_dir, "hierarchy.txt")

# Write the hierarchy text to the file
with open(output_file, "w") as f:
    f.write(hierarchy_text)

print("Hierarchy text written to:", output_file)