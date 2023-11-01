import os
from PyPDF2 import PdfReader, PdfWriter

# 返回指定文件夹下的文件名列表
def get_file_list(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list



def split_pdf(input_file_path, output_dir_path, chunk_size):
    # Open the PDF file
    input_pdf = PdfReader(open(input_file_path, "rb"))

    # Get the total number of pages in the PDF file
    num_pages = len(input_pdf.pages)

    # Calculate the number of chunks required
    num_chunks = num_pages // chunk_size + (1 if num_pages % chunk_size != 0 else 0)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Split the PDF file into chunks
    for i in range(num_chunks):
        # Calculate the start and end pages of the chunk
        start_page = i * chunk_size
        end_page = min(start_page + chunk_size, num_pages)

        # Create a new PDF file for the chunk
        output_pdf = PdfWriter()

        # Add the pages from the input PDF file to the output PDF file
        for j in range(start_page, end_page):
            output_pdf.add_page(input_pdf.pages[j])

        # Save the output PDF file
        output_file_path = os.path.join(output_dir_path, f"chunk_{i+1}.pdf")
        with open(output_file_path, "wb") as output_file:
            output_pdf.write(output_file)
        output_file.close()



if __name__ == "__main__":
    input_path = "./source_pdf/"
    source_pdf = get_file_list(input_path)

    for pdf in source_pdf:
        split_pdf(pdf, "./result_pdf", 100)

