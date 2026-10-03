import pymupdf

pdf_path = "experiments/pdf_extraction/sample.pdf"

doc = pymupdf.open(pdf_path)

page = doc[0]

blocks = page.get_text("blocks")

print("Number of blocks:", len(blocks))

for i, block in enumerate(blocks):
    print("\n" + "=" * 60)
    print("BLOCK:", i)
    print("=" * 60)

    print("X0:", block[0])
    print("Y0:", block[1])
    print("X1:", block[2])
    print("Y1:", block[3])
    print("TEXT:", block[4])

doc.close()