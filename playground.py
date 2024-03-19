# import gdown

# url = 'https://drive.google.com/uc?id=1s3UeBftDhTPWzpNHIrhEKEN2tC5PzvRL'
# output_path = 'data/test.rar'
# url = gdown.download(url, output_path, quiet=False, fuzzy=True, use_cookies=True)

# print('driveeeee', url)

import patoolib

# Define the path to your RAR file
rar_file_path = "data/1. Tuplah Aceh 2019.rar"

# Extract all files from the RAR archive
patoolib.extract_archive(rar_file_path, outdir="data")

# Print a success message
print(f"Files extracted from {rar_file_path}")