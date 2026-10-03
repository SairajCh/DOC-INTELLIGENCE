import pdfplumber

pdf_path = "experiments/pdf_extraction/sample.pdf"

with pdfplumber.open(pdf_path) as pdf:

    print("Number of pages:", len(pdf.pages))

    for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()

        print("=" * 50)
        print(f"PAGE {page_number}")
        print("=" * 50)
        print(text)


    print("-" * 50)
    print("LAYOUT ANALYSIS")
    print("-" * 50)

    for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(layout=True)
    
            print("=" * 50)
            print(f"PAGE {page_number}")
            print("=" * 50)
            print(text)