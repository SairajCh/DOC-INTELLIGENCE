import pymupdf


def extract_value(words, key):
    key_words = key.split()

    for i in range(len(words) - len(key_words)):
        
        # Check whether the current words match our key
        current_words = [
            words[i + j][4]
            for j in range(len(key_words))
        ]

        if current_words == key_words:

            key_line = words[i][6]

            value_words = []

            for word in words[i + len(key_words):]:

                # Stop when we reach another line
                if word[6] != key_line:
                    break

                value_words.append(word[4])

            return " ".join(value_words)

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