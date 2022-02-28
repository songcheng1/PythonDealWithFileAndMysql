# -*- coding: utf-8 -*-
import fitz
import uuid
import time
import pandas as pd
from tqdm import tqdm
from pydocx import PyDocX

class File2Html:
    def docx_to_html(self, docx_path):
        # docx
        docx_html_data = PyDocX.to_html(docx_path)
        return docx_html_data

    def excel_to_html(self, excel_path):
        # xls xlsx
        excel_html_data = ''
        if '红醴消防' not in str(excel_path):
            xd = pd.ExcelFile(excel_path)
            sheet_names = xd.sheet_names
            df = ''
            for i, sheet_name in enumerate(sheet_names):
                df = xd.parse(sheet_name=sheet_names[i])
            excel_html_data = df.to_html(header=True, index=False)
        return excel_html_data

    def pdf2html(self, pdf_path):
        # pdf
        doc = fitz.open(pdf_path)
        html_text = ''
        for page in tqdm(doc):
            html_content = page.getText('html')
            html_text += html_content
        return html_text
