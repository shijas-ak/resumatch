# parser.py

import re
import io
from pdfminer.high_level import extract_text
from typing import Dict, List


# Predefined skills to match (you can expand this later or make it dynamic)
SKILL_KEYWORDS = [
    'python', 'java', 'c++', 'c#', 'javascript', 'typescript', 'html', 'css',
    'react', 'node.js', 'express', 'django', 'flask', 'sql', 'mysql',
    'postgresql', 'mongodb', 'git', 'docker', 'aws', 'linux'
]


def extract_text_from_pdf(pdf_file: bytes) -> str:
    """Extract raw text from PDF file bytes."""
    try:
        return extract_text(io.BytesIO(pdf_file))
    except Exception as e:
        print(f"[ERROR] PDF parsing failed: {e}")
        return ""


def extract_email(text: str) -> str:
    match = re.search(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    return match.group(0) if match else ""


def extract_phone(text: str) -> str:
    match = re.search(r'\+?\d[\d\s\-]{7,15}', text)
    return match.group(0) if match else ""


def extract_name(text: str) -> str:
    """Assumes first line or first few words is the name (basic assumption)."""
    lines = text.strip().split('\n')
    for line in lines:
        clean_line = line.strip()
        if len(clean_line.split()) <= 4:  # Likely a name
            return clean_line
    return "N/A"


def extract_skills(text: str) -> List[str]:
    """Returns matched skills from predefined list."""
    text_lower = text.lower()
    found_skills = [skill for skill in SKILL_KEYWORDS if skill in text_lower]
    return found_skills


def parse_resume(pdf_bytes: bytes) -> Dict:
    """Main function to extract structured data from a resume PDF."""
    text = extract_text_from_pdf(pdf_bytes)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }
