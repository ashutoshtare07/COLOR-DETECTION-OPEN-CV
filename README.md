# Real-Time Color Detection with OpenCV

## Overview

A Python-based real-time color detection system that uses your webcam to detect and highlight **green**, **blue**, and **red** objects simultaneously using HSV color space masking.

---

## Architecture

* **OpenCV** → webcam capture, HSV conversion, bounding box rendering
* **Pillow (PIL)** → bounding box extraction from binary masks
* **NumPy** → efficient array operations for color range computation

### Why HSV?

* BGR color space mixes brightness and color, making detection unreliable under changing lighting
* HSV separates **Hue** (color), **Saturation** (intensity), and **Value** (brightness)
* Thresholding on Hue alone gives robust, lighting-independent detection

---

## How It Works

* Each BGR color is converted to HSV to extract its hue
* A ±10 hue tolerance range is computed around the target color
* **Red wrap-around handling** → red spans both ends of the HSV hue circle (0° and 180°), so the code checks both bounds and adjusts limits accordingly
* Binary masks isolate pixels matching each color
* Bounding boxes are drawn around detected regions in real-time

---

## Color Detection Logic

| Color | BGR Value | HSV Hue Range | Special Handling |
|-------|-----------|---------------|-----------------|
| Green | `[0, 255, 0]` | ~55° ± 10° | None |
| Blue | `[255, 0, 0]` | ~120° ± 10° | None |
| Red | `[0, 0, 255]` | ~0° / ~180° | Wrap-around logic |

---

## Files

* `color.py` → `get_limits()` helper — converts a BGR color to HSV hue bounds with red wrap-around support
* `Color_detection.py` → main script — captures webcam feed, applies masks for all three colors, and draws bounding boxes

---

## Requirements

```
opencv-python
Pillow
numpy
```

Install with:

```bash
pip install opencv-python Pillow numpy
```

---

## Usage

```bash
python Color_detection.py
```

* Point your camera at colored objects
* Bounding boxes will appear around detected green, blue, and red regions
* Press **`q`** to quit

---

## 👨‍💻 Author

**Ashutosh Tare** | Aspiring ML Engineer | Data Science Enthusiast
