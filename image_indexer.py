# image_indexer.py
import uuid


def summarize_image(llm, image_path):
    """
    Uses multimodal LLM to describe image.
    """
    response = llm.invoke([
        {"type": "text", "text": "Describe this image clearly and concisely."},
        {"type": "image_url", "image_url": image_path}
    ])
    return response.content


def build_image_vectors(images, embeddings_model, llm):
    """
    Converts images to Pinecone-ready vectors.
    """
    vectors = []

    for img in images:
        summary = summarize_image(llm, img["image_path"])
        emb = embeddings_model.embed_query(summary)

        vectors.append((
            str(uuid.uuid4()),
            emb,
            {
                "type": "image",
                "summary": summary,
                "image_path": img["image_path"],
                "page": img["page"]
            }
        ))

    return vectors
    