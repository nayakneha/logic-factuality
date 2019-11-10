import collections
import sys
import numpy as np
import pandas as pd
import re


COLUMNS = ["Party", "First", "Last", "Full name", "File name"]

def main():
  book_list_file, data_path = sys.argv[1:3]

  records = []
  books_df = pd.DataFrame(columns=COLUMNS)
  with open(book_list_file, 'r') as f:
    for line in f:
      filename, party, _, first, last, full_name = line.strip().split("\t")
      value_dict = dict(zip(COLUMNS, [party, first, last, full_name,
        filename]))
      books_df = books_df.append(value_dict, ignore_index=True)


  counts = {}

  for idx, row in books_df.iterrows():
    author = row["Full name"]
    with open(data_path + "/" + row["File name"], 'r') as f:
      text = f.read()
    for _, entity_row in books_df.iterrows():
      entity_name = entity_row["Full name"]
      mention_count = sum(
          1 for match in re.finditer(r"\b" + entity_name + r"\b", text))
      if mention_count:
        counts[(row["Party"] + "_" + author,
          entity_row["Party"] + "_" + entity_name)] = mention_count


    with open("output.txt" ,'w') as f:
      for (author, entity), value in counts.iteritems():
        f.write("\t".join([author, entity, str(value)]) + "\n")

if __name__ == "__main__":
  main()
