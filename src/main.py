import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    inpath = os.path.join("in", "scottish_hills.csv")

    # load and plot
    df = pd.read_csv(inpath)

    fig, ax = plt.subplots(figsize=(8, 10))
    scatter = ax.scatter(
        df["Longitude"],
        df["Latitude"],
        c=df["Height"],
        cmap="terrain",
        edgecolors="k",
        linewidths=0.3,
        s=30,
        alpha=0.8,
    )
    fig.colorbar(scatter, ax=ax, label="Height (m)", shrink=0.6)

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Scottish Munros")

    mean_lat = np.radians(df["Latitude"].mean())
    ax.set_aspect(1 / np.cos(mean_lat))

    # save output
    plt.tight_layout()
    outpath = os.path.join("out", "scottish_hills.png")
    plt.savefig(outpath, dpi=150)
    print(f"Saved to {outpath}")


if __name__ == "__main__":
    main()
