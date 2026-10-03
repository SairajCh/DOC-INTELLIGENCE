import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)
page = doc[0]

data = page.get_text("dict")

print("Page width:", data["width"])
print("Page height:", data["height"])

print("Number of blocks:", len(data["blocks"]))

for block_number, block in enumerate(data["blocks"]):

    print("\n" + "=" * 60)
    print("BLOCK:", block_number)
    print("Block type:", block["type"])

    if "lines" not in block:
        continue

    print("Number of lines:", len(block["lines"]))

    for line_number, line in enumerate(block["lines"]):

        print("  LINE:", line_number)

        for span in line["spans"]:

            print("    TEXT:", span["text"])
            print("    FONT:", span["font"])
            print("    SIZE:", span["size"])
            print("    BBOX:", span["bbox"])

doc.close()