from PIL import Image
from backend.core.image_moderation import moderate_image
import cloudinary
import cloudinary.uploader
import uuid
import os


cloudinary.config(
    cloud_name="YOUR_CLOUD_NAME",
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)


def process_profile_image(image_path):

    img = Image.open(image_path)

    img = img.convert("RGB")

    img.thumbnail((1200, 1200))

    processed_path = f"temp/{uuid.uuid4()}.jpg"

    img.save(
        processed_path,
        "JPEG",
        quality=82,
        optimize=True
    )
    
    is_safe = moderate_image(processed_path)

    if not is_safe:
        os.remove(processed_path)
        raise Exception("Unsafe image")

    result = cloudinary.uploader.upload(
        processed_path,
        folder="prizor_profiles"
    )

    os.remove(processed_path)

    return result["secure_url"]