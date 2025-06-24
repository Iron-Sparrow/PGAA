# Morphological Anti-Aliasing (MLAA)

## What is MLAA?

MLAA, or Morphological Anti-Aliasing, is a technique that uses the morphological properties of pixels to smooth out edges in an frame. It works by analyzing the pixel structure and applying filters to reduce jagged edges without significantly blurring the frame. This method is particularly effective for frames with high contrast edges.

## Usage in code

To use MLAA in your code, you need to import Morphological from the PGAA package.

```
from PGAA import Morphological as MLAA
```

## Functions

### MLAA_LOW

`...`

> [!NOTE]
> Added in **1.0.0**.

### MLAA_MEDIUM

`...`

> [!NOTE]
> Added in **1.0.0**.

### MLAA_HIGH

`...`

> [!NOTE]
> Added in **1.0.0**.

### MLAA_VERY_HIGH

`...`

> [!NOTE]
> Added in **1.0.0**.

### MLAA

`...`

> [!NOTE]
> Added in **1.0.0**.

### MLAA_CUSTOM

`...`

> [!NOTE]
> Added in **1.0.0**.

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