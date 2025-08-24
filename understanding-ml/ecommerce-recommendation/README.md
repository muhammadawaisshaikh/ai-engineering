# Simple Ecommerce Recommendation System

A clean, modular recommendation system that shows how to suggest products to customers based on what similar users liked.

## Project Structure

The system is now broken into small, focused modules:

### Core Modules

- **`data_utils.py`** - Data creation and utility functions (25 lines)
  - Creates sample data
  - Converts data to rating matrix
  - Helper functions for data access

- **`similarity.py`** - User similarity calculations (20 lines)
  - Calculates cosine similarity between users
  - Finds most similar users

- **`recommendations.py`** - Core recommendation logic (25 lines)
  - Generates product recommendations
  - Uses collaborative filtering

- **`display.py`** - Output formatting (25 lines)
  - Handles all display functions
  - Formats recommendations nicely

- **`main.py`** - Orchestrates everything (15 lines)
  - Imports and runs all modules
  - Clean, simple flow

## What it does

The system looks at how customers rate products and finds customers with similar tastes. Then it recommends products that similar customers liked but you haven't tried yet.

## How it works

1. **Get data**: Collect ratings from customers
2. **Find similar users**: Compare rating patterns between customers
3. **Make recommendations**: Suggest products that similar customers liked

## Quick start

1. Install packages: `pip install -r requirements.txt`
2. Run: `python main.py`

That's it! The system will show you sample data and recommendations.

## Example output

```
Simple Ecommerce Recommendation System
========================================
Sample data:
   user_id  product_id  rating product_name
0        1         101       5       Laptop
1        1         102       4         Mouse
2        2         101       4       Laptop
3        2         103       5     Keyboard
4        3         102       3         Mouse
5        3         103       4     Keyboard

User 1 recommendations:
  - Keyboard (similarity: 0.71)

User 2 recommendations:
  - Mouse (similarity: 0.71)

User 3 recommendations:
  - Laptop (similarity: 0.71)
```

## How recommendations work

- User 1 likes Laptop and Mouse
- User 2 likes Laptop and Keyboard  
- User 3 likes Mouse and Keyboard
- The system finds that User 1 and User 2 are similar (both like Laptop)
- So it recommends Keyboard to User 1 (since User 2 likes it)
- And recommends Mouse to User 2 (since User 1 likes it)

## Why this structure is better

- **Small files**: Each file has a single, clear purpose
- **Easy to understand**: Focus on one concept per file
- **Easy to modify**: Change one part without affecting others
- **Easy to test**: Test individual functions separately
- **Easy to extend**: Add new features to specific modules

## Real-world use

This is how Netflix, Amazon, and other sites suggest things to you:
- They look at what you've watched/bought
- Find other people with similar tastes
- Recommend things those people liked

## Learning value

This modular version teaches you:
- How to break code into logical pieces
- How recommendation systems work
- Basic collaborative filtering
- Data manipulation with pandas
- Similarity calculations
- Clean code organization

Perfect for learning both the basics and good coding practices!
