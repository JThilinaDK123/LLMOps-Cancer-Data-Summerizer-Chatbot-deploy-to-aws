from pypdf import PdfReader

try:
    reader = PdfReader("./data/data.pdf")
    ESG_Indicators = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            ESG_Indicators += text
except FileNotFoundError:
    ESG_Indicators = "Data not available"

# # Read other data files
# with open("./data/summary.txt", "r", encoding="utf-8") as f:
#     summary = f.read()

# with open("./data/style.txt", "r", encoding="utf-8") as f:
#     style = f.read()

# with open("./data/facts.json", "r", encoding="utf-8") as f:
#     facts = json.load(f)