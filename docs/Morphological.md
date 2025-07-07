# Morphological Anti-Aliasing (MLAA)

## What is MLAA?

MLAA, or Morphological Anti-Aliasing, is a technique that uses the morphological properties of pixels to smooth out edges in an frame. It works by analyzing the pixel structure and applying filters to reduce jagged edges without significantly blurring the frame. This method is particularly effective for frames with high contrast edges.

## Usage in code

To use MLAA in your code, you need to import Morphological from the PGAA package.

```python
from PGAA import Morphological as MLAA
```

## Functions

### MLAA_LOW

`mlaa_low(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with low quality MLAA applied to it.

With `mlaa_low`, the default `luma` value is `'mean'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### MLAA_MEDIUM

`mlaa_medium(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with medium quality MLAA applied to it.

With `mlaa_medium`, the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### MLAA_HIGH

`mlaa_high(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with high quality MLAA applied to it.

With `mlaa_high`, the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### MLAA_VERY_HIGH

`mlaa_very_high(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with very high quality MLAA applied to it.

With `mlaa_very_high`, the default `luma` value is `'rec2100'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### MLAA

`mlaa(surf, quality, luma)` where `surf` is a Pygame-CE surface, `quality` is a string representing the quality level, and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with MLAA applied to it.

With `mlaa`, the default `quality` value is `'medium'` (options include 'low', 'medium', 'high', 'very_high'), and the default `luma` value depends on the quality setting.

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### MLAA_CUSTOM

`mlaa_custom(surf, threshold, search_steps, diagonal_search_steps, corner_rounding, luma)` where `surf` is a Pygame-CE surface, and the other parameters control the MLAA algorithm's behavior. Returns a Pygame-CE surface with custom MLAA settings applied to it.

With `mlaa_custom`, you can fine-tune the MLAA algorithm to achieve the desired balance between quality and performance.

> [!NOTE]
> Added in **1.0.0**.
> The kwarg `luma` was added in **3.1.0**.

> [!WARNING]
> Changed from `custom_mlaa` to `mlaa_custom` in **1.0.3**.

## Aliases

PGAA provides aliases for the MLAA functions to make them easier to use. The aliases are as follows:

> [!NOTE]
> Added in **1.0.0**.

+ `mlaa_low`:
  + `mlaa_lq`
+ `mlaa_medium`:
  + `mlaa_med`
  + `mlaa_default`
+ `mlaa_high`:
  + `mlaa_hq`
+ `mlaa_very_high`:
  + `mlaa_vhq`
  + `mlaa_very_hq`

> [!NOTE]
> Added in **1.0.3**.

+ `mlaa_low`:
  + `mlaa_low_quality`
+ `mlaa_medium`:
  + `mlaa_medium_quality`
  + `mlaa_mq`
+ `mlaa_high`:
  + `mlaa_high_quality`
+ `mlaa_very_high`:
  + `mlaa_veryhigh`
  + `mlaa_very_high_quality`
  + `mlaa_veryhighquality`
+ `mlaa_custom`:
  + `mlaa_custom_quality`
  + `custom_mlaa_quality`
  + `custom_mlaa`
