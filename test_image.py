from app.services.image_generator import (
    generate_image
)

path = generate_image(
    "futuristic AI city"
)

print("Image saved at:", path)