from PIL import Image, ImageDraw
import os


def generate_image(prompt):

    # Create folder
    os.makedirs("generated_images", exist_ok=True)

    # Create image
    image = Image.new(
        "RGB",
        (512, 512),
        color=(73, 109, 137)
    )

    # Draw text
    draw = ImageDraw.Draw(image)

    draw.text(
        (20, 250),
        prompt,
        fill=(255, 255, 255)
    )

    # Image path
    image_path = (
        f"generated_images/{prompt[:20]}.png"
    )

    # Save image
    image.save(image_path)

    return image_path