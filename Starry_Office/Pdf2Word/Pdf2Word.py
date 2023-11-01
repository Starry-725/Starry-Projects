import PyPDF2
import os
from pdf2docx import Converter


# 获取指定文件夹下所有pdf文件的名称
def get_pdf_files(dir_path):
    pdf_files = []
    for file in os.listdir(dir_path):
        if file.endswith('.pdf'):
            pdf_files.append(os.path.join(dir_path, file))
    return pdf_files


#
def pdf_to_word(pdf_path):
    docx_path = './result_word/'+pdf_path.split('/')[-1].split('.')[0]+'.docx'
    p2w = Converter(pdf_path)
    p2w.convert(docx_path,start=0,end=None)
    p2w.close()
    return docx_path


# main函数
if __name__ == '__main__':
    files = get_pdf_files('./source_pdf')
    for file in files:
        docx_path = pdf_to_word(file)
        