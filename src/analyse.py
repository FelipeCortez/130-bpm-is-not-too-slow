import argparse
import librosa
import numpy as np
from collections import Counter

hop_length = 512

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    filepath = args.filepath
    print(filepath)

    y, sr = librosa.load(args.filepath)

    onset_env = librosa.onset.onset_strength(y, sr=sr)
    dtempo = librosa.beat.tempo(onset_envelope=onset_env,
                                sr=sr,
                                hop_length=hop_length,
                                aggregate=None)

    print(len(dtempo))
    print(set(dtempo))
    print(Counter(dtempo).most_common())
    print(f"{np.mean(dtempo)}, {np.std(dtempo)}")
