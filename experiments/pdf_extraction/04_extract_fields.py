import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)

page = doc[0]

matches = page.search_for("Claim Number")

for match in matches:

    print("Found:", page.get_textbox(match))

doc.close()