# Super Sampling Anti-Aliasing (SSAA)

## What is SSAA?

SSAA, or Super Sampling Anti-Aliasing, is a technique that consists of rendering a frame at a higher resolution (usually except for SSAA0.5x) and then downscaling it to the screen resolution. Thi process helps to smooth out the edges of objects visible on screen and allows to keep details visible even when resolution is low.\
The downside to SSAA is that it is very resource-intensive, as it requires either to upscale and then downscale a frame, or to render the frame at a higher resolution from the start and then to downscale it.

## Usage in code

To use SSAA in your code, you need to import Supersampling from the PGAA package.

```python
from PGAA import SuperSampling as SSAA
```

## Functions

### SSAA0.5x

`ssaa05(surf)` where `surf`is a Pygame-CE surface and where the function returns a new surface with the anti-aliasing applied.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa05` to `ssaa05` in **0.3.1**.

SSAA0.5x does not render the frame at a lower resolution. Instead, it first downscales the frame by 50% (0.5x). Then, it upscales the frame back to the original resolution.\
Thanks to the optimised algorith found in [pygame-ce](https://pyga.me/docs/ref/transform.html#pygame.transform.scale2x), it allows better upscaling to the original resolution of the frame.

> [!CAUTION]
> Unlike other SSAA methods, SSAA0.5x and its variants require the surface size to be even. If the surface size is odd, it will raise an error.

### SSAA0.5x HQ

`ssaa05_hq(surf)` where `surf` is a Pygame-CE surface and where the function returns a new surface with the smooth anti-aliasing applied.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa05_hq` to `ssaa05_hq` in **0.3.1**.

### SSAA0.5x LQ

`ssaa05_lq(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. It doesn't use the algorithm used in ssa05, but rather the default (faster but less good-looking one). More info in [the pygame-ce transform documentation.](https://pyga.me/docs/ref/transform.html#pygame.transform.scale)

> [!NOTE]
> Added in **0.2.2**.

> [!WARNING]
> Change from `aa05_lq` to `ssaa05_lq` in **0.3.1**.

### SSAA2x

`ssaa2(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. This functions uses the high quality [2x upscaling algorithm](https://pyga.me/docs/ref/transform.html#pygame.transform.scale2x) but uses the fast downscaling algorithm. It is suggested to use the High Quality version of this function for better results.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa2` to `ssaa2` in **0.3.1**.

### SSAA2x HQ

`ssaa2_hq(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with the anti-aliasing applied. This function uses the high quality [2x upscaling algorithm](https://pyga.me/docs/ref/transform.html#pygame.transform.scale2x) and the smoother higher quality downscaling algorithm. This is the recommended function to use for SSAA2x and thus is the default for SuperSampling.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa2_hq` to `ssaa2_hq` in **0.3.1**.

### SSAA2x LQ

`ssaa2_lq(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. It uses the faster but less accurate scaling algorithms for both upscaling and downscaling.

> [!NOTE]
> Added in **0.2.2**.

> [!WARNING]
> Change from `aa2_lq` to `ssaa2_lq` in **0.3.1**.

### SSAA4x

`ssaa4(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. This function upscales the image to 4x its original size and then downscales it back, using the standard scaling algorithms.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa4` to `ssaa4` in **0.3.1**.

### SSAA4x HQ

`ssaa4_hq(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with high-quality anti-aliasing applied. It uses the smoother scaling algorithms for both upscaling and downscaling, resulting in better image quality but at a higher performance cost.

> [!NOTE]
> Added in **0.1.0**.

> [!WARNING]
> Change from `aa4_hq` to `ssaa4_hq` in **0.3.1**.

### SSAA8x

`ssaa8(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. This function upscales the image to 8x its original size and then downscales it back, using the standard scaling algorithms.

> [!NOTE]
> Added in **0.2.1**.

> [!WARNING]
> Change from `aa8` to `ssaa8` in **0.3.1**.

### SSAA8x HQ

`ssaa8_hq(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with high-quality anti-aliasing applied. It upscales the image to 8x its original size using high-quality algorithms, then downscales it back with smooth scaling, resulting in very high image quality at a significant performance cost.

> [!NOTE]
> Added in **0.2.1**.

> [!WARNING]
> Change from `aa8_hq` to `ssaa8_hq` in **0.3.1**.

### SSAA32x

`ssaa32(surf)` where `surf` is a Pygame-CE surface and where it returns a new surface with anti-aliasing applied. This function is only meant to be used for Benchmarking purposes has no real use in production code. It uses [smoothscale](https://pyga.me/docs/ref/transform.html#pygame.transform.smoothscale) by default, as a means to get the best looking results.

> [!NOTE]
> Added in **0.2.2**.

> [!WARNING]
> Change from `aa32` to `ssaa32` in **0.3.1**.

### SSAA

`ssaa(surf, scale_factor, smooth)` where `surf` is a Pygame-CE surface, `scale_factor` is an integer representing the scaling factor (default is 2), and `smooth` is a boolean indicating whether to use smooth scaling (default is True). Returns a Pygame-CE surface with SSAA applied to it.

> [!NOTE]
> Added in **0.3.1**.

### SSAA LQ

`ssaa_lq(surf, scale_factor)` where `surf` is a Pygame-CE surface and `scale_factor` is an integer representing the scaling factor (default is 2). Returns a Pygame-CE surface with low-quality SSAA applied to it.

> [!NOTE]
> Added in **0.3.1**.

### SSAA HQ

`ssaa_hq(surf, scale_factor)` where `surf` is a Pygame-CE surface and `scale_factor` is an integer representing the scaling factor (default is 2). Returns a Pygame-CE surface with high-quality SSAA applied to it. This uses smooth scaling for both upscaling and downscaling.

> [!NOTE]
> Added in **0.3.1**.

## Aliases

PGAA provides aliases for the functions to make it easier to use them.\
Here are the aliases:
> [!NOTE]
> Added in **1.0.1**:

+ `ssaa05`:
  + `ssaa_05`
  + `ssaa_05x`
  + `ssaa05x`

+ `ssaa05_hq`:
  + `ssaa_05_hq`
  + `ssaa_05x_hq`
  + `ssaa05x_hq`

+ `ssaa05_lq`:
  + `ssaa_05_lq`
  + `ssaa_05x_lq`
  + `ssaa05x_lq`

+ `ssaa2`:
  + `ssaa_2`
  + `ssaa_2x`
  + `ssaa2x`

+ `ssaa2_hq`:
  + `ssaa_2_hq`
  + `ssaa_2x_hq`
  + `ssaa2x_hq`
  + `ssaa_default`

+ `ssaa2_lq`:
  + `ssaa_2_lq`
  + `ssaa_2x_lq`
  + `ssaa2x_lq`

+ `ssaa4`:
  + `ssaa_4`
  + `ssaa_4x`
  + `ssaa4x`

+ `ssaa4_hq`:
  + `ssaa_4_hq`
  + `ssaa_4x_hq`
  + `ssaa4x_hq`

+ `ssaa8`:
  + `ssaa_8`
  + `ssaa_8x`
  + `ssaa8x`

+ `ssaa8_hq`:
  + `ssaa_8_hq`
  + `ssaa_8x_hq`
  + `ssaa8x_hq`

+ `ssaa32`:
  + `ssaa_32`
  + `ssaa_32x`
  + `ssaa32x`

+ `ssaa_lq`:
  + `ssaa_low`

+ `ssaa_hq`:
  + `ssaa_high`

> [!NOTE]
> Added in **1.0.2**:

+ `ssaa_lq`:
  + `ssaa_low_quality`

+ `ssaa_hq`:
  + `ssaa_high_quality`

+ `ssaa32`:
  + `ssaa32_hq`
  + `ssaa_32_hq`
  + `ssaa32x_hq`
  + `ssaa_32x_hq`
