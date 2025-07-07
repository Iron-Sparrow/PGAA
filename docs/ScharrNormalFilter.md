# Scharr Normal Filter Anti-Aliasing (ScharrNFAA)

## What is ScharrNFAA?

ScharrNFAA, or Scharr Normal Filter Anti-Aliasing, is a combination of two different procedures to produce an anti-aliased image.\
It first applies the Scharr algorith that turns a normal image into a normal map, and then applies Anti-Aliasing based on the normal map. Using the Normal Map to apply Anti-Aliasing is commonly called Normal Filter Anti-Aliasing (NFAA). By generating the normal map from the Pygame-CE surface, we are using the lack of Normal Map to our advantage, and thus we apply NFAA to a surface/image that doesn't have an external normal map.\
This method is very experimental and can cause some unexpected results. It is best to test out whether this anti-aliasing method suits your needs.

## Usage in Code

```python
from PGAA import ScharrNormalFilter as ScharrNFAA
```

## Functions

### scharr_nfaa

`scharr_nfaa(surf, quality, luma)` where `surf` is a Pygame-CE surface, `quality` is a string representing the quality level, and `luma` is a string representing the luma calculation method. Returns a Pygame-CE surface with ScharrNFAA applied to it.

With `scharr_nfaa`, the default `quality` value is `'medium'` (options include 'low', 'medium', 'high'), and the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### scharr_nfaa_low

`scharr_nfaa_low(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with ScharrNFAA applied at low quality.

With `scharr_nfaa_low`, the default `luma` value is `'mean'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### scharr_nfaa_medium

`scharr_nfaa_medium(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with ScharrNFAA applied at medium quality.

With `scharr_nfaa_medium`, the default `luma` value is `'rec709'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

### scharr_nfaa_high

`scharr_nfaa_high(surf, luma)` where `surf` is a Pygame-CE surface and `luma` is a string. Returns a Pygame-CE surface with ScharrNFAA applied at high quality.

With `scharr_nfaa_high`, the default `luma` value is `'rec2100'` (options include 'rec709', 'rec601', 'rec2100', 'mean').

> [!NOTE]
> Added in **3.0.0**.
> The kwarg `luma` was added in **3.1.0**.

## Aliases

PGAA provides aliases for the ScharrNFAA functions to make them easier to use. The aliases are as follows:

 `...`