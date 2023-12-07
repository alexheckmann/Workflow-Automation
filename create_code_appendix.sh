#!/bin/bash

export LC_ALL=C.UTF-8

# Check if folder location is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <folder_location>"
    exit 1
fi

FOLDER_LOCATION=$1
OUTPUT_TXT="output.txt"
OUTPUT_PDF="output.pdf"

# Check if the folder exists
if [ ! -d "$FOLDER_LOCATION" ]; then
    echo "Folder does not exist: $FOLDER_LOCATION"
    exit 1
fi

# Empty the output text file if it already exists
> $OUTPUT_TXT

# Iterate through each file in the folder recursively
# Excluding specific folders and files
find $FOLDER_LOCATION -type d \( -name ".next" -o -name "node_modules" -o -name ".git" -o -name ".idea" -o -name "components" -o -name ".swc" \) -prune -o -type f -print | egrep -v '(\.env\.local$|create_code_appendix\.sh$|plot_evaluation_results\.ipynb$|output\.txt$|favicon\.ico|package-lock\.json|package\.json|\.eslintrc\.json|postcss\.config\.js|README\.md|tailwind\.config\.ts|tailwind\.config\.js|utils\.ts|vector_search\.json|\.gitignore|next-env\.d\.ts|jest\.setup\.js|jest\.config\.js|next\.config\.js|tsconfig\.json|components\.json|globals\.css|layout\.tsx)' | while read file; do
    echo "Processing $file"
    echo "File: $file" >> $OUTPUT_TXT
    cat "$file" >> $OUTPUT_TXT
    echo -e "\n\n\n\f" >> $OUTPUT_TXT
done

# Convert the text file to PDF
# Ensure you have pandoc installed or change this part to use a different tool
pandoc $OUTPUT_TXT -s -o $OUTPUT_PDF

# Optional: Remove the temporary text file
rm $OUTPUT_TXT

echo "PDF generated: $OUTPUT_PDF"
