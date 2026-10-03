import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)
page = doc[0]

words = page.get_text("words")

for i, word in enumerate(words):
    text = word[4]

    if text == "Number:":
        print("Found:", text)

        next_word = words[i + 1]

        print("Next word:", next_word[4])

doc.close()