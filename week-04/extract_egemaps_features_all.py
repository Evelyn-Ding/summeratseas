import os
import subprocess
import pandas as pd
import glob
import tempfile

SMILEXTRACT = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/bin/SMILExtract"
CONFIG = "/Users/evelyn/Downloads/opensmile-3.0.2-macos-armv8/config/egemaps/v02/eGeMAPSv02.conf"
WAV_DIR = "/Users/evelyn/Documents/claudecode/speechlab/TORGO/torgo-processed-wav/"
SUMMARY_CSV = "/Users/evelyn/Documents/claudecode/speechlab/week-04/torgo_egemaps_summary.csv"

# Step 4: extract speaker ID from filename and add label
# speaker IDs with 'C' (e.g. FC01, MC02) are controls (0), others are dysarthric (1)
def get_label(name):
    speaker_id = name.strip("'").split("-")[0]
    if "C" in speaker_id:
        return 0
    else:
        return 1

# Step 1: get all wav files
wav_files = glob.glob(os.path.join(WAV_DIR, "*.wav"))

# Step 2: run SMILExtract on each file, collect results in memory (no individual CSVs saved)
all_dfs = []
for wav_file in wav_files:
    filename = os.path.basename(wav_file)
    # use a temp file so we don't clutter the output folder
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
        tmp_path = tmp.name
    subprocess.run(
        [SMILEXTRACT, "-C", CONFIG, "-I", wav_file,
         "-csvoutput", tmp_path,
         "-instname", filename,   # pass filename so name column is not 'unknown'
         "-appendcsv", "0"],      # overwrite instead of append to avoid duplicate rows
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if os.path.exists(tmp_path):
        df = pd.read_csv(tmp_path, sep=";")
        all_dfs.append(df)
        os.remove(tmp_path)

# Step 3: concatenate all results into one dataframe
combined_df = pd.concat(all_dfs, ignore_index=True)

# Step 4: add label column
combined_df["label"] = combined_df["name"].apply(get_label)

combined_df.to_csv(SUMMARY_CSV, index=False)
print(f"Done! {len(combined_df)} rows saved to {SUMMARY_CSV}")
