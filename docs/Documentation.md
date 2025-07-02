# Documentation

> [!IMPORTANT]
> Documentation is a work in progress and may not be complete nor fully accurate.
> It is very likely that there are more features than documented, so if you want to go beyond the documentation, you can check out the source code in the [GitHub repository](https://github.com/Iron-Sparrow/PGAA/tree/main/src/PGAA).

## What is PGAA?

PGAA is a Python Package that provides multiple forms of anti-aliasing for [Pygame-CE surfaces](https://pyga.me/docs/ref/surface.html).

## Available Anti-Aliasing Methods

### FXAA (Fast Approximate Anti-Aliasing)

> [!NOTE]
> It was added in **2.0.0**.

> [!WARNING]
> FXAA requires Numpy to run.

To check out the documentation for FXAA, see [FastApproximate.md](../docs/FastApproximate.md)

### Jimenez's MLAA (Jimenez Morphological Anti-Aliasing)

> [!NOTE]
> It was added in **3.0.0**.

> [!WARNING]
> Jimenez's MLAA requires Numpy to run.

> [!CAUTION]
> It is not recommended to use Jimenez's MLAA in projects for it's simply the predecessor of SMAA, an thus is worse than SMAA. We recommend using SMAA instead for better results.

To check out the documentation for Jimenez's MLAA, see [Jimenez.md](../docs/Jimenez.md).

### MLAA (Morphological Anti-Aliasing)

> [!NOTE]
> It was added in **1.0.0**.

> [!WARNING]
> MLAA requires Numpy to run.

To check out the documentation for MLAA, see [Morphological.md](../docs/Morphological.md).

### ScharrNFAA (Scharr Normal Filter Anti-Aliasing)

> [!NOTE]
> It was added in **3.0.0**.

> [!WARNING]
> ScharrNFAA requires Numpy to run.

### SMAA (Subpixel Morphological Anti-Aliasing)

> [!NOTE]
> It was added in **3.0.0**.

> [!WARNING]
> SMAA requires Numpy to run.

### SSAA (Super Sample Anti-Aliasing)

> [!TIP]
> SSAA was implemented as the first algorith and doesn't require Numpy to run.

> [!NOTE]
> It was added in **0.1.0**.

> [!NOTE]
> The implementation of SSAA in PGAA isn't necessarily proper SSAA, as SuperSampling is quite a broad term, but for PGAA, it is rather a Fullscreen upscaling Anti-Aliasing.

To check out the documentation for SSAA, see [SuperSampling.md](../docs/SuperSampling.md).
