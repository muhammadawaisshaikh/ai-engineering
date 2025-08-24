# AI Lab with Python

A comprehensive Python-based AI laboratory designed for hands-on learning and experimentation with artificial intelligence and machine learning concepts.

## Overview

This directory serves as your primary AI laboratory environment, providing a structured approach to learning AI concepts through practical implementation. It includes Jupyter notebooks, utility functions, and sample datasets to help you understand and experiment with various AI algorithms.

## Directory Structure

```
ai-lab-python/
├── main.py                 # Main execution script
├── notebooks/              # Jupyter notebooks for experiments
│   └── intro_experiments.ipynb
├── utils/                  # Utility functions and helpers
│   ├── __init__.py
│   ├── data_loader.py      # Data loading utilities
│   └── visualizer.py       # Visualization functions
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Features

- **Interactive Learning**: Jupyter notebooks for step-by-step experimentation
- **Utility Functions**: Reusable data loading and visualization tools
- **Sample Datasets**: Built-in datasets for immediate experimentation
- **Modular Design**: Clean separation of concerns for easy understanding

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Basic understanding of Python programming
- Interest in AI and machine learning

## Installation

1. **Navigate to the directory**
   ```bash
   cd ai-lab-python
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python --version
   pip list | grep -E "(numpy|pandas|matplotlib|scikit-learn)"
   ```

## Quick Start

### Running the Main Script

Execute the main script to see a basic AI workflow in action:

```bash
python main.py
```

This will:
- Load a sample dataset (Iris dataset)
- Display basic data information
- Create a visualization of the target distribution

### Using Jupyter Notebooks

For interactive learning, launch Jupyter:

```bash
jupyter notebook notebooks/intro_experiments.ipynb
```

The notebook covers:
- Data loading and exploration
- Basic data visualization
- Simple machine learning workflow
- Feature importance analysis

## Core Components

### Data Loader (`utils/data_loader.py`)

Provides functions to load and prepare datasets:
- `load_sample_data()`: Loads the Iris dataset as a pandas DataFrame
- Easy to extend for other datasets

### Visualizer (`utils/visualizer.py`)

Creates informative plots and charts:
- `plot_distribution()`: Visualizes target variable distributions
- Customizable plotting functions for different data types

### Main Script (`main.py`)

Demonstrates the complete workflow:
- Data loading
- Basic preprocessing
- Visualization
- Ready for model training

## Learning Objectives

After working with this lab, you should understand:

1. **Data Loading**: How to import and prepare datasets for AI applications
2. **Data Exploration**: Basic techniques for understanding your data
3. **Visualization**: Creating informative plots to analyze data patterns
4. **Workflow Structure**: How to organize AI projects systematically
5. **Python Best Practices**: Writing clean, maintainable AI code

## Customization

### Adding New Datasets

1. Place your dataset file in the directory
2. Modify `utils/data_loader.py` to include a new loading function
3. Update the main script to use your new data

### Extending Visualizations

1. Add new plotting functions to `utils/visualizer.py`
2. Import and use them in your notebooks or main script
3. Share useful visualizations with the community

## Troubleshooting

### Common Issues

- **Import Errors**: Ensure you're in the correct directory and have installed requirements
- **Display Issues**: Some systems may need additional configuration for matplotlib
- **Memory Problems**: Large datasets might require chunking or sampling

### Getting Help

- Check the error messages carefully
- Verify your Python environment and package versions
- Ensure all required files are present in the directory

## Next Steps

After mastering this lab:

1. Explore the `foundations-ai-ml/` directory for symbolic AI concepts
2. Move to `understanding-ml/` for core machine learning principles
3. Practice with real datasets from sources like Kaggle or UCI
4. Experiment with different visualization libraries (seaborn, plotly)

## Contributing

We welcome improvements to this lab:
- Better utility functions
- Additional sample datasets
- Enhanced visualizations
- More comprehensive notebooks

## Resources

- **Python Documentation**: https://docs.python.org/
- **Pandas User Guide**: https://pandas.pydata.org/docs/
- **Matplotlib Tutorials**: https://matplotlib.org/stable/tutorials/
- **Jupyter Documentation**: https://jupyter.org/documentation

---

*This lab is designed to be your starting point for AI experimentation. Take your time, experiment freely, and don't hesitate to modify the code to suit your learning needs.*
