# NEON COAST · 霓虹海岸

Preserved original browser game, mirrored to GitHub Pages.

- Main entrance: **1.3.5**
- Optional preview at `preview-1-5/`: **1.5.1-preview**
- Original source snapshot: `7ea0b217fba1f40464b6f31bec3a236753c2f32d`

Only three preview navigation files have been adjusted for GitHub Pages project subpaths. Gameplay, physics, models and visuals are preserved from the original published bundle. This release does not include new aircraft autopilot, a selectable Gemini ADAS strategy, or a claimed fix for reported acceleration shake.

## Saves

Each website origin stores its own saves. To transfer progress from the original website, open the in-game phone save menu, export JSON, then explicitly import that file in the same formal/preview edition on this mirror. The two domains do not automatically synchronize saves. Importing writes to the selected edition/slot. Keep the exported file as a backup.

## Deployment

The two ZIP files contain only public runtime assets and license notices. `release-manifest.json` records every file's size and SHA-256. `verify_release.py` checks the archives and extracts an exact `_site/` tree; the pinned GitHub Actions workflow deploys that tree. Project source history, credentials and hosting configuration are not included.

The preview uses Godot 4.6.3 WebAssembly, WebGL 2 and gzip `DecompressionStream`, with a single-threaded loader. Use a current browser; older iPhones/browsers may not support all required features.

## Attribution

The runtime retains the Godot MIT license and third-party notices, Three.js licenses, and the LUCENT VISION model's CC BY 4.0 attribution. See `ASSET_CREDITS.txt` and the relevant `assets/`, `vendor/` and preview `physics/` license files in the deployed site or archives.
