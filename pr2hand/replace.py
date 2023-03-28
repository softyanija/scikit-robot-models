import sys
import re

if len(sys.argv) != 2:
    print("Usage: python3 replace.py <input_file>")
    sys.exit(1)

file_name = sys.argv[1]
string_to_replace = "pr2_description"
replacement_string = "pr2hand"
delete_start = "<transmission"
delete_end = "</transmission>"
delete_del = delete_start + ".*?" + delete_end

# openhand
with open(file_name, "r") as f_in:
    # read file
    file_content = f_in.read()

# replace
new_content = file_content.replace(string_to_replace, replacement_string)

# delete between "<transmission" and "</transmission>"
new_content = re.sub(delete_del, "", new_content, flags=re.DOTALL)

# write to new file
with open(file_name, "w") as f_out:
    f_out.write(new_content)
