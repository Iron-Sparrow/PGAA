# Subpixel Morphological Anti-Aliasing (SMAA)

## What is SMAA?

SMAA, or Subpixel Morphological Anti-Aliasing, is an advanced anti-aliasing technique developed as an evolution of Jimenez's MLAA. It was created by Jorge Jimenez, Jose I. Echevarria, Tiago Sousa, and Diego Gutierrez. SMAA improves upon MLAA by incorporating subpixel features detection and diagonal pattern handling, resulting in higher quality anti-aliasing with less performance impact.

SMAA is widely considered one of the most effective post-processing anti-aliasing techniques, offering a good balance between quality and performance. It's particularly effective at handling both geometric aliasing and shader aliasing.

> [!IMPORTANT]
> The implementation of SMAA in this context is not fully up to specs with SMAA v2.8. Results may vary.

## Usage in code

```python
from PGAA import SubpixelMorphological as SMAA
```

## Functions

### smaa

`smaa(surf, quality, luma)` where `surf` is a Pygame-CE surface, `quality` is a string representing the quality level, and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with SMAA applied to it.

With `smaa`, the default `quality` value is `'medium'` (options include 'low', 'medium', 'high', 'ultra'), and the default `luma` value depends on the quality setting.

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### smaa_low

`smaa_low(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with SMAA applied at low quality.

With `smaa_low`, the default `luma` value is `'mean'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### smaa_medium

`smaa_medium(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with SMAA applied at medium quality.

With `smaa_medium`, the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### smaa_high

`smaa_high(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with SMAA applied at high quality.

With `smaa_high`, the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### smaa_ultra

`smaa_ultra(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with SMAA applied at ultra quality.

With `smaa_ultra`, the default `luma` value is `'rec2100'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### smaa_custom

`smaa_custom(surf, threshold, max_search_steps, diagonal_detection, corner_detection, luma)` where `surf` is a Pygame-CE surface, and the other parameters control the SMAA algorithm's behavior. Returns a Pygame-CE surface with custom SMAA settings applied to it.

With `smaa_custom`, you can fine-tune the SMAA algorithm to achieve the desired balance between quality and performance.

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

## Aliases

PGAA provides aliases for the SMAA functions to make them easier to use. The aliases are as follows:

 `...`