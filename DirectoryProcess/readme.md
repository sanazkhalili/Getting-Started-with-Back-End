This code is for intelligent document processing. We pass a directory address to the program (DirectoryProcess/projects/directory_info_elk.py) as a command-line argument. The program reads all the files in the directory.

If a file is a text file, the program saves the directory address, creation time, file name, file type, language detection, and class information for that text file in Elasticsearch.

If a file is an image, the program handles it in two different states. If the image contains text, the program performs OCR (Optical Character Recognition) to extract the text and saves the extracted text, language detection, label, and class score.

If the image file does not contain text, the program performs classification and saves the directory address, creation time, file name, and file type for both states.