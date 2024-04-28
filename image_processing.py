from PIL import Image
import os

def scale_and_add_border(image_path, target_size=(255, 255), border_color=(0, 0, 0)):
    original_image = Image.open(image_path)
    scaled_image = original_image.resize(target_size)
    bordered_image = Image.new('RGB', (target_size[0] + 2, target_size[1] + 2), border_color)
    bordered_image.paste(scaled_image, (1, 1))
    return bordered_image

def combine_images(image1, image2, output_file):
    canvas = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
    canvas.paste(image1, (0, 0))
    canvas.paste(image2, (0, 256))
    canvas.save(os.path.join('results', output_file))

def create_input_image(image1_path, image2_path):
    bordered_image1 = scale_and_add_border(image1_path)
    bordered_image2 = scale_and_add_border(image2_path)
    combine_images(bordered_image1, bordered_image2, 'input-image.png')
