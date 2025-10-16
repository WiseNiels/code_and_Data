import fitz  # PyMuPDF

doc = fitz.open()
page = doc.new_page()
page.insert_text((50, 100), "Relatório de Vendas - Outubro", fontsize=14)
doc.save("relatorio.pdf")
