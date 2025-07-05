# Fast Approximate Anti-Aliasing (FXAA)

## What is FXAA?

FXAA, or Fast Approximate Anti-Aliasing, is an anti-aliasing technique invented by Timothy Lottes.\
FXAA managed to make anti-aliasing a feature of every computer, for it doesn't cost much performance in comparison to the visual results.

> [!NOTE]
> Many users claim that FXAA blurs more than it actually imporoves image quality. It is thus suggested to also offer alternative forms of Anti-Aliasing to the users.

## Usage in code

To use FXAA in your code, you need to import FastApproximate from the PGAA package.

```python
from PGAA import FastApproximate as FXAA
```

## Functions

### FXAA

`fxaa(surf, threshold, diagonal_blur, f4)`, where `surf` is a Pygame-CE surface, `threshold` is a float or an int with a value strictly above `0`, `diagonal_blur` is a bool, and `f4` is a bool, is a function that returns a Pygame-CE surface with FXAA applied to it.

With `fxaa`, the default `threshold` value is `20` *(the lower the better quality, with too low causing blurring)*, the default `diagonal_blur` value is `False` *(diagonal_blur cause better results on jagged_edges especially diagonals with the cost of a slight performance decrease)*, the default `f4` value is `False` *(Increases floating point precision at the cost of higher memory usage)*.

> [!NOTE]
> Added in **2.0.1**.\
> The kwarg `diagonal_blur` was added in **3.0.0**.

> [!NOTE]
> While it is recommended to avoid changing the default values, fine-tuning might yield the highest performance-to-image-quality ratio.

### FXAA HQ

`fxaa_hq(surf, threshold, diagonal_blur, f4)`, where `surf` is a Pygame-CE surface, `threshold` is a float or an int with a value strictly above `0`, `diagonal_blur` is a bool, and `f4` is a bool, is a function that returns a Pygame-CE surface with High Quality FXAA applied to it.

With `fxaa_hq`, the default `threshold` value is `10` *(the lower the better quality, with too low causing blurring)*, the default `diagonal_blur` value is `True` *(diagonal_blur cause better results on jagged_edges especially diagonals with the cost of a slight performance decrease)*, the default `f4` value is `True` *(Increases floating point precision at the cost of higher memory usage)*.

> [!NOTE]
> Added in **2.0.1**.\
> The kwarg `diagonal_blur` was added in **3.0.0**.

> [!IMPORTANT]
> From **3.0.1** onwards, FXAA_HQ is a simply a modified version of `fxaa()` instead of its own function.

> [!NOTE]
> While it is recommended to avoid changing the default values, fine-tuning might yield the highest performance-to-image-quality ratio.

### FXAA 3.11

`fxaa311(surf, threshold, diagonal_blur, f4)` where `surf` is a Pygame-CE surface, `threshold` is a float with a value strictly above `0`, `diagonal_blur` is a bool, and `f4` is a bool, is a function that returns a Pygame-CE surface with FXAA_311 applied to it.

Unlike the other FXAA functions, `fxaa311` is based on the more recent verison of FXAA — FXAA 3.11 — and thus has more advanced features, like adaptive thresholding and overall better quality.

> [!NOTE]
> Added in **2.0.1**.\
> The kwarg `diagonal_blur` was added in **3.0.0**.

> [!NOTE]
> While it is recommended to avoid changing the default values, fine-tuning might yield the highest performance-to-image-quality ratio.

## Aliases

> [!NOTE]
> Added in **2.0.1**:

+ `fxaa`:
  + `fxaa_default`
  + `legacy_fxaa`
  + `fxaa_legacy`
+ `fxaa_hq`: 
  + `fxaa_high_quality`
  + `fxaa_highquality`
+ `fxaa311`:
  + `fxaa_3_11`
  + `modern_fxaa`
  + `fxaa_modern`

> [!NOTE]
> Added in **3.0.1**:

+ `fxaa311`:
  + `fxaa_3_11`