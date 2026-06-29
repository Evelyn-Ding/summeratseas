import os
import subprocess
import pandas as pd
import glob

SMILEXTRACT = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/bin/SMILExtract"
CONFIG = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/config/egemaps/v02/eGeMAPSv02.conf"
WAV_DIR = "/Users/evelyn/Documents/claudecode/speechlab/TORGO/torgo-processed-wav/"
OUTPUT_DIR = "/Users/evelyn/Documents/claudecode/speechlab/week-04/torgo_csvs/"

# Step 1: get all wav files
wav_files = glob.glob(os.path.join(WAV_DIR, "*.wav"))

# Step 2: run SMILExtract on each file
for wav_file in wav_files:
    filename = os.path.basename(wav_file)
    output_csv = os.path.join(OUTPUT_DIR, filename.replace(".wav", ".csv"))
    subprocess.run([SMILEXTRACT, "-C", CONFIG, "-I", wav_file, "-csvoutput", output_csv])

# Step 3: load and concatenate all CSVs
all_dfs = []
for csv_file in glob.glob(os.path.join(OUTPUT_DIR, "*.csv")):
    df = pd.read_csv(csv_file, sep=";")
    all_dfs.append(df)

combined_df = pd.concat(all_dfs, ignore_index=True)

# Step 4: add label column
def get_label(filename):
    speaker_id = filename.split("-")[0]
    if "C" in speaker_id:
        return 0
    else:
        return 1

combined_df["label"] = combined_df["name"].apply(get_label)

combined_df.to_csv(os.path.join(OUTPUT_DIR, "torgo_egemaps.csv"), index=False)
