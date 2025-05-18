from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the pretrained model (do this once)
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_top_matches(resume_text, job_descriptions, top_n=3):
    """
    Compare resume_text with a list of job_descriptions and return top N matches.

    Args:
        resume_text (str): The extracted resume content (skills + job title).
        job_descriptions (list of dict): List containing job postings (title + description).
        top_n (int): Number of top matches to return.

    Returns:
        list of dict: Top matching job descriptions with similarity scores.
    """
    
    # Convert job descriptions to strings
    job_texts = [f"{job['title']} {job['description']}" for job in job_descriptions]
    
    # Encode both the resume and job descriptions
    resume_embedding = model.encode([resume_text])
    job_embeddings = model.encode(job_texts)

    # Compute cosine similarity between resume and all jobs
    similarities = cosine_similarity(resume_embedding, job_embeddings)[0]

    # Sort the scores and pick top N
    top_indices = np.argsort(similarities)[::-1][:top_n]

    # Return matched jobs with scores
    top_matches = []
    for idx in top_indices:
        job = job_descriptions[idx]
        score = round(float(similarities[idx]), 3)
        top_matches.append({**job, "score": score})

    return top_matches
