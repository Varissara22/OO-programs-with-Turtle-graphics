# Turtle Polygon Art Generator

This project uses Python's `turtle` graphics module and object-oriented programming (OOP) to generate artistic polygon patterns.  
The user selects from 9 different art styles, and the program randomly generates colorful triangles, squares, or pentagons with optional recursive shrinking effects.

---

## Features

### **Polygon Base Class**
All polygon shapes inherit from the `Polygon` class, which includes:
- Random size (50–150)
- Random orientation
- Random screen location
- Random RGB color
- Random border thickness
- A `draw_polygon()` method to draw the shape
- A `reduction_ratio()` method that shrinks the polygon using a golden-ratio factor (0.618)

### **Derived Shape Classes**
- `Triangle` → 3 sides  
- `Square` → 4 sides  
- `Pentagon` → 5 sides  

### **Draw Class**
Handles user selection and generates the chosen art pattern.

The user is asked:

Each number (1–9) corresponds to a different drawing mode:
1. Draw 30 random triangles  
2. Draw 30 random squares  
3. Draw 30 random pentagons  
4. Mixed polygons (triangle/square/pentagon)  
5. Recursive shrinking triangles  
6. Recursive shrinking squares  
7. Recursive shrinking pentagons  
8. Mixed polygons with recursive shrinking  
9. Mixed polygons, randomly shrinking or not  

---

## How It Works

### Drawing Polygons
Each shape:
- Moves to a random position  
- Applies a random rotation  
- Draws its polygon  
- Uses random colors and border sizes  

### Shrinking (Optional)
If shrinking is triggered:
- The polygon is redrawn 3 times
- Each time it shrinks using the golden-ratio factor  
- The location is adjusted so the smaller polygon stays centered  

---

## Requirements
* Python 3.x

---

##  How to Use

To run the demonstration script, execute `data_processing.py` from your terminal:

```bash