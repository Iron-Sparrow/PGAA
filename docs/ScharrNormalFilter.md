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

`...`

## Aliases

`...`
