# Jimenez's Morphological Anti-Aliasing (Jimenez-MLAA)

## What is Jimenez's MLAA?

Jimenez's MLAA is a variant of Reshetov's MLAA. Nowadays, we consider MLAA to be Reshetov's version while Jimenez's variant has been abandoned in favor of its continuation: SMAA.\
Jimenez's MLAA is a modification and upgrade of the original MLAA algorithm and can nowadays be found in the [SMAA Github Repository](https://github.com/iryoku/smaa/tree/master) for the version [1.3](https://github.com/iryoku/smaa/tree/v1.3), [1.4](https://github.com/iryoku/smaa/tree/v1.4), [1.5](https://github.com/iryoku/smaa/tree/v1.5).

If you want more information, check out [MLAA on iryoku.com](https://www.iryoku.com/mlaa/) and [SMAA on iryoku.com](https://www.iryoku.com/smaa/).

## Usage in code

> [!IMPORTANT]
> We do not recommend using Jimenez's MLAA in projects. Instead, we recomment using SMAA, which is the continuation of Jimenez's MLAA[^1].

To use Jimenez's MLAA in your code, you need to import Jimenez from the PGAA package.

```
from PGAA import Jimenez as Jimenez_MLAA
```

[^1]: To quote [The important information section of the Jimenez's MLAA webpage](https://www.iryoku.com/mlaa/#:~:text=Note%20that%20the%20repository%20name%20changed%20from%20%27jimenez%2Dmlaa%27%20to%20%27smaa%27%2C%20as%20SMAA%20builds%20on%20top%20of%20Jimenez%27s%20MLAA%2C%20and%20we%20preferred%20to%20use%20the%20same%20repository%20for%20both.%20It%20is%20strictly%20superior%20in%20quality%20and%20performance%2C%20so%20there%20is%20no%20reason%20for%20using%20Jimenez%27s%20MLAA%20anymore.): *"Note that the repository name changed from 'jimenez-mlaa' to 'smaa', as [SMAA](https://www.iryoku.com/smaa/) builds on top of Jimenez's MLAA, and we preferred to use the same repository for both. It is strictly superior in quality and performance, so there is no reason for using Jimenez's MLAA anymore."*

## Link to SMAA
To check out the documentation for SMAA, see [SMAA.md](../docs/SubpixelMorphological.md).