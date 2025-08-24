# Working with Data: A Practical Guide to Data Science Workflows

A comprehensive guide to the essential steps in any data science project - from collecting raw data to preparing it for machine learning models. Each subdirectory contains practical code examples that you can run, modify, and learn from.

## What You'll Learn

This chapter breaks down the data science workflow into four key phases:

1. **Data Collection & Preprocessing** - Getting your data ready
2. **Exploratory Data Analysis (EDA)** - Understanding your data
3. **Feature Engineering & Scaling** - Creating and transforming features
4. **Handling Imbalanced Data** - Dealing with real-world data challenges

## Directory Structure

```
working-with-data/
├── data-collection-preprocessing/     # Data loading and cleaning
├── exploratory-data-analysis/         # EDA tools and techniques
├── feature-engineering-scaling/       # Feature creation and transformation
├── handling-imbalanced-data/          # Balancing techniques and methods
└── README.md                          # This file
```

## 1. Data Collection & Preprocessing

**Location**: `data-collection-preprocessing/`

**What it does**: This section shows you how to load raw datasets and clean them up for analysis.

**Key Features**:
- Load datasets from various sources
- Handle missing values and outliers
- Clean and standardize data formats
- Prepare data for downstream analysis

**Files**:
- `main.py` - Main execution script
- `utils/data_loader.py` - Functions to load different data formats
- `utils/preprocessing.py` - Data cleaning and preparation functions
- `requirements.txt` - Required Python packages

**Quick Start**:
```bash
cd data-collection-preprocessing
pip install -r requirements.txt
python main.py
```

**What you'll see**: The script loads a credit card dataset, cleans it up, and shows you the before/after results.

## 2. Exploratory Data Analysis (EDA)

**Location**: `exploratory-data-analysis/`

**What it does**: EDA is like being a detective with your data. You'll learn to understand patterns, spot issues, and discover insights.

**Key Features**:
- Generate comprehensive data summaries
- Visualize data distributions
- Analyze missing values
- Create correlation heatmaps
- Identify data quality issues

**Files**:
- `main.py` - Orchestrates all EDA steps
- `eda/summary.py` - Statistical summaries and basic info
- `eda/distributions.py` - Distribution plots and histograms
- `eda/missing_values.py` - Missing data analysis
- `eda/correlation.py` - Correlation analysis and heatmaps

**Quick Start**:
```bash
cd exploratory-data-analysis
python main.py
```

**What you'll see**: Beautiful visualizations of the Iris dataset, including distributions, correlations, and data quality insights.

## 3. Feature Engineering & Scaling

**Location**: `feature-engineering-scaling/`

**What it does**: Transform raw data into features that machine learning models can actually use effectively.

**Key Features**:
- Create interaction features (e.g., area from length × width)
- Extract time-based features (year, month, day)
- Encode categorical variables
- Scale numerical features to similar ranges

**Files**:
- `feature_engineering.py` - Create new features from existing data
- `feature_scaling.py` - Normalize and standardize numerical features

**Quick Start**:
```bash
cd feature-engineering-scaling
python feature_engineering.py
python feature_scaling.py
```

**What you'll see**: Examples of how to transform raw data into meaningful features that improve model performance.

## 4. Handling Imbalanced Data

**Location**: `handling-imbalanced-data/`

**What it does**: Real-world datasets are rarely perfectly balanced. This section teaches you techniques to handle imbalanced classes (like fraud detection where 99% of transactions are legitimate).

**Key Features**:
- Analyze class distribution imbalances
- Apply oversampling techniques (SMOTE)
- Use undersampling methods
- Train models with class weights
- Evaluate performance on imbalanced data

**Files**:
- `main.py` - Complete workflow demonstration
- `imbalance_analysis.py` - Analyze class distribution
- `resampling_methods.py` - Oversampling and undersampling
- `smote_handler.py` - SMOTE implementation
- `weighted_model.py` - Class-weighted model training
- `evaluation.py` - Performance metrics for imbalanced data

**Quick Start**:
```bash
cd handling-imbalanced-data
python main.py
```

**What you'll see**: A comparison between baseline models and balanced models, showing how handling imbalanced data improves performance.

## How to Use This Chapter

### For Beginners
1. Start with **Data Collection & Preprocessing** - it's the foundation
2. Move to **Exploratory Data Analysis** to understand your data
3. Learn **Feature Engineering** to create better inputs
4. Tackle **Imbalanced Data** when you're comfortable with the basics

### For Intermediate Users
- Use these examples as templates for your own projects
- Modify the code to work with your datasets
- Experiment with different preprocessing techniques
- Combine multiple approaches for better results

### For Advanced Users
- Extend the functionality with additional algorithms
- Implement custom preprocessing pipelines
- Add more sophisticated balancing techniques
- Integrate with your existing ML workflows

## Prerequisites

- **Python 3.7+** (recommended: 3.8+)
- **Basic Python knowledge** (variables, functions, imports)
- **Familiarity with pandas and numpy** (helpful but not required)
- **Understanding of machine learning concepts** (for the later sections)

## Installation

Each subdirectory has its own `requirements.txt` file. Install dependencies as needed:

```bash
pip install -r requirements.txt
```

**Common packages you'll need**:
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `matplotlib` - Basic plotting
- `seaborn` - Statistical visualizations
- `scikit-learn` - Machine learning tools

## Pro Tips

1. **Start Small**: Don't try to implement everything at once. Master one concept before moving to the next.

2. **Experiment**: Modify the code examples. Change parameters, try different datasets, see what happens.

3. **Document Your Process**: Keep notes on what works and what doesn't. Data science is iterative!

4. **Validate Assumptions**: Always check your data quality before building models.

5. **Think About Business Context**: The best technical solution isn't always the right business solution.

## Troubleshooting

**Common Issues**:
- **Import errors**: Make sure you're in the right directory and have installed requirements
- **Data not found**: Check that data files exist in the expected locations
- **Memory issues**: Large datasets might need chunking or sampling
- **Plotting problems**: Some systems need additional display configurations

**Getting Help**:
- Check the error messages carefully - they often contain the solution
- Verify your Python environment and package versions
- Look at the example data files to understand expected formats

## Next Steps

After mastering this chapter, you'll be ready to:
- Build complete machine learning pipelines
- Handle real-world data challenges
- Implement advanced preprocessing techniques
- Work with production data systems

## Additional Resources

- **Pandas Documentation**: https://pandas.pydata.org/
- **Scikit-learn User Guide**: https://scikit-learn.org/stable/user_guide.html
- **Matplotlib Tutorials**: https://matplotlib.org/stable/tutorials/
- **Data Science Handbook**: https://jakevdp.github.io/PythonDataScienceHandbook/

---

*Happy data wrangling!*

*Remember: The best data scientist is the one who spends the most time understanding their data before building models.*
