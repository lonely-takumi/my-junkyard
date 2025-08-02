import fitz
import os
import shutil

def cut_last_page_from_pdf(inputFilePath, outputPath, suffix):
  doc = fitz.open(inputFilePath)
  pages = len(doc)
  
  doc.delete_page(pages - 1)

  fileNameWithoutExt = get_file_name_without_extension(inputFilePath)
  #outputFilePath = outputPath + "/" + fileNameWithoutExt + f"_{suffix}.pdf"
  outputFilePath = os.path.join(outputPath, f"{fileNameWithoutExt}.pdf")

  doc.save(outputFilePath)
  doc.close()
  print(f"Last page removed from {inputFilePath} and saved to {outputFilePath}")

  # if suffix != 1:
  #   deleteFilePath = outputPath + "/" + fileNameWithoutExt + f"_{suffix - 1}.pdf"
  #   os.remove(deleteFilePath)

  return outputFilePath

def cut_selected_page_from_pdf(inputFilePath, outputPath, suffix, page_number):
  doc = fitz.open(inputFilePath)
  
  if page_number < 0 or page_number >= len(doc):
    print("Invalid page number")
    return
  
  doc.delete_page(page_number)
  
  fileNameWithoutExt = get_file_name_without_extension(inputFilePath)
  #outputFilePath = outputPath + "/" + fileNameWithoutExt + f"_{suffix}.pdf"
  outputFilePath = os.path.join(outputPath, f"{fileNameWithoutExt}.pdf")


  doc.save(outputFilePath)
  doc.close()
  print(f"Page {page_number + 1} removed from {inputFilePath} and saved to {outputFilePath}")

  # if suffix != 1:
  #   deleteFilePath = outputPath + "/" + fileNameWithoutExt + f"_{suffix - 1}.pdf"
  #   os.remove(deleteFilePath)

  return outputFilePath

def get_page_count(inputFilePath):
  doc = fitz.open(inputFilePath)
  page_count = len(doc)
  doc.close()
  return page_count

def get_file_name_without_extension(filePath):
  baseName = os.path.basename(filePath)
  fileNameWithoutExt = os.path.splitext(baseName)[0]
  return fileNameWithoutExt

def initialize_output_directory():
  outputDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
  if not os.path.exists(outputDir):
    os.makedirs(outputDir)
  else:
    shutil.rmtree(outputDir)
    os.makedirs(outputDir)
  return outputDir

if __name__ == "__main__":
  cnt = 1

  outputPath = initialize_output_directory()

  while True:
    if cnt == 1:
      inputFilePath = input("Enter the path to the PDF file: ")

    choice = input("Enter '1' to cut the last page, '2' to cut a specific page, or 'q' to quit: ")

    if choice == '1':
      outputFilePath = cut_last_page_from_pdf(inputFilePath, outputPath, cnt)
    elif choice == '2':
      page = input(f"Enter the page number to cut (1-{get_page_count(inputFilePath)}): ")
      if page.isdigit():
        page = int(page) - 1
        outputFilePath = cut_selected_page_from_pdf(inputFilePath, outputPath, cnt, page)
      else:
        print("Invalid input. Please enter a valid page number.")
    elif choice == 'q':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")
    
    cnt += 1
    print(f"Operation count: {cnt}")
    
      