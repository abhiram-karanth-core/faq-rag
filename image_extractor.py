# image_extractor.py
import os
import uuid
import base64
from unstructured.partition.pdf import partition_pdf

IMAGE_DIR = "extracted_images"
os.makedirs(IMAGE_DIR, exist_ok=True)


def extract_images_from_pdf(pdf_path):
    """
    Automatically extracts and crops images from a PDF.
    Returns metadata only (no indexing).
    """
    elements = partition_pdf(
        filename=pdf_path,
        extract_images_in_pdf=True,
        infer_table_structure=True
    )

    images = []

    for el in elements:
        if el.category == "Image" and el.metadata.image_base64:
            img_id = str(uuid.uuid4())
            img_path = os.path.join(IMAGE_DIR, f"{img_id}.png")

            with open(img_path, "wb") as f:
                f.write(base64.b64decode(el.metadata.image_base64))

            images.append({
                "image_path": img_path,
                "page": el.metadata.page_number
            })

    return images
