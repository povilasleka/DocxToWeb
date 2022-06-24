class ConvertService:
    def __init__(self, docx_input_path, html_output_path):
        self.docx_input_path = docx_input_path
        self.html_output_path = html_output_path
    
    def run(self):
        return self.docx_input_path