import os
import subprocess
import pandas as pd
import glob

SMILEXTRACT = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/bin/SMILExtract"
CONFIG = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/config/egemaps/v02/eGeMAPSv02.conf"
WAV_DIR = "/Users/evelyn/Documents/claudecode/speechlab/Parkinsons/Spanish neurovoz_v3/audios/"
OUTPUT_DIR = "/Users/evelyn/Documents/claudecode/speechlab/week-07/neurovoz_free_csvs/"
SUMMARY_CSV = "/Users/evelyn/Documents/claudecode/speechlab/week-07/neurovoz_free_egemaps_summary.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# speaker IDs are prefixed PD_FREE_#### (Parkinson's, label 1) or HC_FREE_#### (healthy control, label 0)
# SMILExtract wraps -instname in single quotes in the csv output, so strip those first
def get_label(name):
    if name.strip("'").startswith("PD_"):
        return 1
    else:
        return 0

# Step 1: get all FREE (spontaneous monologue) wav files
wav_files = glob.glob(os.path.join(WAV_DIR, "*FREE*.wav"))

# Step 2: run SMILExtract on each file and save individual CSVs
for wav_file in wav_files:
    filename = os.path.basename(wav_file)
    output_csv = os.path.join(OUTPUT_DIR, filename.replace(".wav", ".csv"))
    subprocess.run(
        [SMILEXTRACT, "-C", CONFIG, "-I", wav_file,
         "-csvoutput", output_csv,
         "-instname", filename,   # pass filename so name column is not 'unknown'
         "-appendcsv", "0"],      # overwrite instead of append to avoid duplicate rows
    )

# Step 3: load and concatenate all CSVs into one dataframe
all_dfs = []
for csv_file in glob.glob(os.path.join(OUTPUT_DIR, "*.csv")):
    df = pd.read_csv(csv_file, sep=";")
    all_dfs.append(df)

combined_df = pd.concat(all_dfs, ignore_index=True)

# Step 4: add label column
combined_df["label"] = combined_df["name"].apply(get_label)

combined_df.to_csv(SUMMARY_CSV, index=False)
print(f"Done! {len(combined_df)} rows saved to {SUMMARY_CSV}")
