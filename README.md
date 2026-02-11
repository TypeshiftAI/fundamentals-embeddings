# Galaxy Generator: Embedding Visualizer

A utility to generate custom 3D word embedding "galaxies" for use in the TensorFlow Projector. This package creates two specific files—`embeddings.tsv` and `metadata.tsv`—engineered to show semantic clusters like "Space," "Fruit," and "Technology."

🚀 Quick Start

1. Prerequisites

- macOS (Optimized for your MacBook Pro setup)

- Python 3.9+

- Virtual Environment (recommended)

Install Python & pip

macOS (Homebrew)

```bash
# Install Homebrew if you don't have it: https://brew.sh
brew install python
# Verify
python3 --version
python3 -m pip install --upgrade pip
```

Windows

```powershell
# Using winget (Windows 10+)
winget install --id Python.Python.3
# Or download the installer from https://python.org and ensure "Add Python to PATH" is checked
python --version
python -m pip install --upgrade pip
```

2. Installation

Clone this repository and set up your local environment:

```bash
# Clone the repository (HTTPS)
git clone https://github.com/TypeshiftAI/fundamentals-embeddings.git
# Or via SSH:
# git clone git@github.com:TypeshiftAI/fundamentals-embeddings.git
cd fundamentals-embeddings

# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

🛠 Usage

To generate your 1,000-point galaxy, run the generator script:

```bash
python scripts/vector_creator.py
```

This will output into the `data/` folder:

- `data/embeddings.tsv`: 999 rows of 50-dimensional vectors.

- `data/metadata.tsv`: 1,000 lines (1 header + 999 labels), categorized for visual coloring.

🌌 Loading into TensorFlow Projector

Follow these steps for your live presentation:

1. Navigate to projector.tensorflow.org.
2. Click the Load button on the left-hand sidebar.
3. Upload Vectors: Select `embeddings.tsv`.
4. Upload Metadata: Select `metadata.tsv`.

Configure Visuals:

- Color by: Change from "None" to Category.

- Label by: Change to Word.

- Projection: Select T-SNE (Bottom left).

- Perplexity: Set to 30.

Click Run and wait for the "stars" to cluster into their respective nebulas.

📁 Project Structure

```
.
├── scripts/
│   ├── vector_creator.py     # The main generator script
│   └── test_embeddings.py    # small test/demo script
├── fundamentals_embeddings/
│   ├── __init__.py
│   └── example.py
├── requirements.txt          # Python dependencies
├── pyproject.toml
├── .gitignore
├── LICENSE
├── README.md                 # You are here
└── data/                     # Generated outputs (created by the script)
```

🧭 Context Switching Examples

- Fruit context: Search for "apple" — pause to show nearby labels (pear, banana, mango). Use slow rotation to reveal the Fruit nebula and note how cluster coloring groups similar words.

- Space context: Search for "mars" or "astronaut" — highlight the Space cluster and trace neighbor lines to orbit/satellite words to demonstrate spatial coherence.

- Technology context: Search for "computer" or "google" — observe the Technology cloud and how words like `software`, `server`, and `linux` form a tech neighborhood.

- Switching to Justice: Search for "justice" (an `Other` word). Notice how it sits outside the scripted clusters; then switch `Color by` to Category to compare distance from `justice` to `law`, `court`, or `government`. This shows how an outlier concept relates to nearby topical clusters and can help illustrate semantic drift or policy-related contexts.

📝 Scripted Interaction Tips

- Rotation: Use a slow drag to show the "Galaxy" before searching.

- The Warp: Use the search bar for "Space" to trigger the neighborhood lines.

- The Bridge: Search "Apple" to show its position between the "Fruit" and "Technology" clusters.
