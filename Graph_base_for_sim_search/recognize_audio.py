
from datasets import load_dataset, Dataset
import os
import pandas as pd
from tqdm.auto import tqdm
import time

import re



def reorder_text(df, time_step=120):
    new = []
    cur_start_time = 0
    cur_max_time = time_step
    cur_text = []
    for i in range(len(df)):
        end = df.loc[i, 'end']
        text = df.loc[i, 'text']
        if end < cur_max_time:
            cur_text.append(text.strip())
        else:
            new.append([cur_start_time, df.loc[i, 'start'], ' '.join(cur_text).replace('  ', ' ')])
            cur_start_time = df.loc[i, 'start']
            cur_max_time += time_step
            cur_text = [text.strip()]
    new.append([cur_start_time, end, ' '.join(cur_text).replace('  ', ' ')])
    return pd.DataFrame(new, columns=['start', 'end', 'text'])





if __name__ == '__main__':
     from argparse import ArgumentParser

     parser = ArgumentParser()
     parser.add_argument("--local_model", '-l', action='store_true', help="If passed uses downloads model and runs local recognition, otherwise sends data to API")
     parser.add_argument("--link", "-l", type=str, default='')
     parser.add_argument("--output_folder", "-o", type=str, required=True)
     parser.add_argument("--verbose", action='store_true')
     
     args = parser.parse_args()
     assert args.file != '' or args.link != '', "Need to pass or --file (-f) or --link (-l)"


     if args.local_model:





     else:
          from dotenv import load_dotenv
          load_dotenv()


