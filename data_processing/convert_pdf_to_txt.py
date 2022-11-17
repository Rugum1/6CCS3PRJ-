import fitz

class PDFConverter() :

    in_file = None
    out_file = None


    def __init__(self,in_file,out_file):
        self.in_file = in_file
        self.out_file = out_file

    def convert_pdf_to_txt_file(self):
        doc = fitz.open(self.in_file)

        with open(self.out_file, 'w' ) as f:
            for page in doc:
                f.writelines(page.get_text("text"))
                f.write('\n')
