import pymupdf


def extract_value(words, key):
    key_words = key.split()

    for i in range(len(words) - len(key_words)):
        current_words = [words[i + j][4] for j in range(len(key_words))]

        if current_words == key_words:
            value_index = i + len(key_words)

            return words[value_index][4]

    return None


pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)
page = doc[0]

words = page.get_text("words")

fields = [
    "Claim Number:",
    "Policy Number:",
    "Patient Name:",
    "Member ID:",
    "Hospital:",
    "Physician:",
]

for field in fields:
    value = extract_value(words, field)
    print(field, "=>", value)

doc.close()