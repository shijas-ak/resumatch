

from app.core.matcher import get_top_matches
import json

# Load job descriptions
with open("data/jobs_data.json", "r", encoding="utf-8") as f:
    jobs_data = json.load(f)

# Simulated resume input
resume_text = """
Experienced software engineer skilled in Python, Java, React, Node.js, and SQL. Passionate about backend development, cloud technologies like AWS, and building scalable systems.
"""

# Get top matches
top_matches = get_top_matches(resume_text, jobs_data)

# Show results
print("\nTop job matches based on similarity:\n")
for job in top_matches:
    print(f"Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Similarity Score: {job['score']:.2f}")
    print("-" * 40)
