import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def average_results(results_list):
    """
    Calculate average metrics from a list of cross-validation results.
    
    Parameters:
    -----------
    results_list : list
        List of dictionaries containing metric results
        
    Returns:
    --------
    avg_metrics : dict
        Dictionary with average values for each metric
    """
    if not results_list:
        return {}
    
    # Get all metric names from the first result
    metric_names = list(results_list[0].keys())
    
    avg_metrics = {}
    for metric in metric_names:
        values = [result[metric] for result in results_list if metric in result]
        if values:
            avg_metrics[metric] = {
                'mean': np.mean(values),
                'std': np.std(values),
                'min': np.min(values),
                'max': np.max(values)
            }
    
    return avg_metrics

def calculate_classification_metrics(y_true, y_pred):
    """
    Calculate comprehensive classification metrics.
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
        
    Returns:
    --------
    metrics : dict
        Dictionary containing all calculated metrics
    """
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
        'f1': f1_score(y_true, y_pred, average='weighted', zero_division=0)
    }
    
    return metrics

def print_metrics_summary(metrics, title="Metrics Summary"):
    """
    Print a formatted summary of metrics.
    
    Parameters:
    -----------
    metrics : dict
        Dictionary containing metrics
    title : str, default="Metrics Summary"
        Title for the summary
    """
    print(f"\n{title}")
    print("=" * len(title))
    
    for metric_name, value in metrics.items():
        if isinstance(value, dict):
            print(f"{metric_name}:")
            for sub_metric, sub_value in value.items():
                print(f"  {sub_metric}: {sub_value:.4f}")
        else:
            print(f"{metric_name}: {value:.4f}")
    
    print()

def compare_metric_lists(metrics_list, metric_names, title="Metric Comparison"):
    """
    Compare metrics across different models or configurations.
    
    Parameters:
    -----------
    metrics_list : list
        List of metric dictionaries
    metric_names : list
        List of names for each metric set
    title : str, default="Metric Comparison"
        Title for the comparison
    """
    print(f"\n{title}")
    print("=" * len(title))
    
    # Get all unique metric keys
    all_metrics = set()
    for metrics in metrics_list:
        all_metrics.update(metrics.keys())
    
    # Print header
    header = f"{'Metric':<15}"
    for name in metric_names:
        header += f"{name:>12}"
    print(header)
    print("-" * len(header))
    
    # Print each metric
    for metric in sorted(all_metrics):
        row = f"{metric:<15}"
        for metrics in metrics_list:
            value = metrics.get(metric, 'N/A')
            if isinstance(value, (int, float)):
                row += f"{value:>12.4f}"
            else:
                row += f"{value:>12}"
        print(row)
    
    print()
