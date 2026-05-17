from app.services.file_generator import (
    generate_pdf,
    generate_docx
)

pdf_path = generate_pdf(
    "Artificial Intelligence Notes",
    "ai_notes"
)

docx_path = generate_docx(
    "Machine Learning Report",
    "ml_report"
)

print("PDF:", pdf_path)
print("DOCX:", docx_path)