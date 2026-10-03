import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)
page = doc[0]

words = page.get_text("words")

for word in words[:5]:
    print("WORD:", word[4])
    print("X0:", word[0])
    print("Y0:", word[1])
    print("X1:", word[2])
    print("Y1:", word[3])
    print()

doc.close()