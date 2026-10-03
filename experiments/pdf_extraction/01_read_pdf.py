import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)

print("Number of pages:", len(doc))

for page_number, page in enumerate(doc, start=1):
    text = page.get_text(sort=True)

    print("=" * 50)
    print(f"PAGE {page_number}")
    print("=" * 50)
    print(text)
    
    # blocks = page.get_text("blocks")

    # print("=" * 50)
    # print(f"PAGE {page_number}")
    # print("=" * 50)
    # print(type(blocks))
    # print(len(blocks))

    # for block in blocks[:4]:
    #     print(block)



doc.close()