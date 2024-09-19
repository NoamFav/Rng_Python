# Define the functions to calculate the center and translate the vertices

def calculate_center_x(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    x_coords = [float(line.split()[1]) for line in lines if line.startswith('v ')]
    center_x = sum(x_coords) / len(x_coords)

    return center_x


def translate_obj_to_center_x(filename, target_x):
    with open(filename, 'r') as file:
        lines = file.readlines()

    x_coords = [float(line.split()[1]) for line in lines if line.startswith('v ')]
    center_x = sum(x_coords) / len(x_coords)
    translation_x = target_x - center_x

    with open('/mnt/data/translated_file.obj', 'w') as file:
        for line in lines:
            if line.startswith('v '):
                parts = line.split()
                x = float(parts[1]) + translation_x
                file.write(f'v {x} {parts[2]} {parts[3]}\n')
            else:
                file.write(line)


# Define the target X coordinate
target_x = 6

# Path to the provided OBJ file (assuming it's already uploaded)
filename = '/Users/noamfavier/Desktop/um_project_golf/src/main/resources/Models/Arrow/Arrow5.obj'

# Calculate the current center X-coordinate
center_x = calculate_center_x(filename)

# Translate the OBJ file vertices
translate_obj_to_center_x(filename, target_x)

# Path to the translated OBJ file
translated_filename = '/Users/noamfavier/Desktop/um_project_golf/src/main/resources/Models/Arrow/Arrow5.obj'

