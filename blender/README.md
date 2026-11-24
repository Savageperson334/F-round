# The blender

Real code from real repositories in the F-round catalogue, copied and fused into one program.

Not a simulation of their ideas: their functions, verbatim, with their names on them. The blender takes over a thousand repositories written by strangers for unrelated purposes, pulls out every function that can stand on its own, in Python, numpy, notebooks and JavaScript, and then finds out by trying which ones actually feed each other.

```
python blender/smoothie.py "moth"
python blender/smoothie.py 440 --steps 30
python blender/smoothie.py "[0, 0.38, 0.71, 0.92, 1, 0.92, 0.71, 0.38, 0]"
python blender/smoothie.py --recipe 0
python blender/smoothie.py --list
```

Give it a seed (text, a number, a list of numbers) and it passes the seed through one real function after another, each from a different repository where it can, for as long as real calls keep succeeding. It prints the trail and writes the trail, a drawing of it and the sound of it to `blender/out/`.

Python alone is enough to run it. With **numpy** installed (`pip install numpy`) the 604 numpy functions join in, and with **Node** installed the 1,038 JavaScript ones do. Without them those are skipped and it says so under `--list`.

## What is in it

From one real run on 2026-11-23:

| | |
| --- | --- |
| Repositories fetched (licence allows copying) | 1,268 |
| Functions read in them | 54,350 (44,289 Python, 10,061 JavaScript) |
| Functions that stand on their own, copied verbatim | 6,158, from 521 repositories |
| Of those, functions that ran on something when tried | 2,901 |
| Pairs of functions from different repositories tried against each other | 151,371 |
| Pairs that really run | 93,354 (62%) |
| Pairs that also fit by name | 1,146 |
| **Functions in the blend** | **2,828, from 409 repositories on 53 shelves** |
| of which plain Python / numpy / JavaScript | 1,186 / 604 / 1,038 |
| of which came out of notebooks | 82 |
| Longest chains kept | 16 real functions from 16 repositories |

The first version of this (Python only, 391 repositories) had 408 functions from 132 repositories and 35 links by name.

Read the two pair numbers together. Six in ten pairs "work" because a number is a number and text is text: fitting by shape is cheap, and on its own it means nothing. 1,146 pairs also match by name, and those are a mixed bag: some are genuine (`to_polar` in one repository feeding `cartesian_from_polar` in another, `b24_to_rad` feeding `rad2deg`, `intToHex` feeding `rgbToHex`), many are loose (a function that says it makes a `byte` feeding one that merely has an argument called `b`). The program marks which kind of link it used on every line it prints.

An example, `--recipe 0`, starts from the number 1987. An origami library in JavaScript turns it into a direction; a fossil-shape model in Python reads that as polar coordinates, by name; a telescope toolkit in numpy turns those back into Cartesian ones, by name; a seismology package turns a pair of numbers into a latitude and longitude, which a transport simulator reads, by name, as a map zone; then rock physics, sonification, a graph library, a telemetry decoder. Sixteen functions, sixteen repositories, fifteen shelves, three languages.

See [CONNECTIONS.md](CONNECTIONS.md) for what connected and the longest chains, and [CREDITS.md](CREDITS.md) for every repository whose code is here.

## How it is made

Five steps, each a script, each re-runnable:

| Step | Script | What it does |
| --- | --- | --- |
| Fetch | `fetch.py` | Downloads the source of every catalogue repository whose licence allows copying and keeps only its `.py` files, the code cells of its notebooks, its `.js` files and its licence files, in `_berries/` (not committed). Nothing fetched is ever run, imported or installed. |
| Harvest | `harvest.py`, `harvest_js.js` | Reads every file as text and keeps the functions that are pure calculation: only their own arguments, harmless built-ins, a few maths and text modules (and the calculating part of numpy), and constants and helpers from their own file. Copies each one verbatim with its repository, file, line and licence. |
| Probe | `probe.py` | Calls each kept function with batteries of plain values to learn what it really accepts and returns. About half run on nothing and are dropped. |
| Blend | `blend.py` | Feeds each function's real output to functions from *different* repositories whose input it might fit: every one that fits by name, and a random sample of 60 that fit only by shape. Keeps the pair only if it really runs and its answer changes with its input. Then searches for long chains. |
| Pour | `make_smoothie.py` | Writes `berries/` (the functions that connected, verbatim), `blend_map.json`, `CONNECTIONS.md`, `CREDITS.md` and `licenses/`. |

A link **fits by name** when what one function says it produces is what the next says it takes (`deg`, `polar`, `color`). Otherwise it only **fits by shape**: a number is a number. Both are real, in that the call really ran; only the first can be meaningful, and the outputs mark which is which.

Values cross between functions, and between languages, as plain JSON: numbers, text, lists, dictionaries. A numpy function is handed its lists as arrays and its arrays come back as lists.

A chain prefers links by name, fields and repositories it has not visited, a change of language, and numpy code. It avoids "wrappers": 202 functions (mostly JavaScript) that only put whatever they are given into a labelled box, which accept anything and change nothing.

To rebuild from scratch you need the GitHub CLI, numpy, Node, and `npm install acorn` in `blender/_work/node`:

```
python blender/fetch.py
python blender/harvest.py
python blender/probe.py
python blender/blend.py --fresh
python blender/make_smoothie.py
```

## Safety

Other people's code is treated as untrusted. Three locks:

1. **Nothing fetched is executed as fetched.** No installs, no imports, no setup scripts, no build steps. Files are read as text and parsed.
2. **Only pure functions are kept.** A harvested function contains no imports, no file, network or process access, no `eval` or `exec`, no classes, no globals, and no attribute name beginning with an underscore. From numpy it may use calculation only: nothing that loads, saves or reads a file. A JavaScript function may not use `this`, `new` on anything but plain containers, `constructor`, `prototype`, `async`, or any name from outside itself but `Math`, `JSON` and the like. Everything else in the repository is left behind.
3. **Calls are contained.** Probing and blending run each function in a separate process. Python functions get only a short list of harmless built-ins and a cut-down numpy. JavaScript functions run inside an empty Node context with code-from-strings switched off, a time limit on every call, and a Node process that is not permitted to write files or start programs. A watchdog sets aside anything that hangs (18 functions in this run).

After the run, every one of the 2,828 functions in `berries/` was compared with the file it came from (all identical) and scanned again, independently, for anything that touches files, processes, the network or the interpreter (nothing found).

`smoothie.py` imports the kept Python functions directly, since by then they have passed all three; JavaScript ones still run inside the locked-down Node context.

## Licences

Only repositories whose licence allows copying go in: MIT, Apache-2.0, BSD, ISC, Unlicense, CC0, Zlib, BSL-1.0, MPL-2.0, GPL-3.0 and LGPL. Because GPL-3.0 code is included, **the blend as a whole is released under the GNU GPL version 3 or later** (`COPYING`). Each function stays under its own repository's licence, and each repository's licence file is kept in `licenses/` (three repositories have none at their top level; `CREDITS.md` names them).

Left out on purpose: the roughly 2,200 catalogue repositories with no licence (their code may not be copied), GPL-2.0 and AGPL-3.0 repositories (which may not combine with GPL-3.0), and JavaScript files that look like somebody else's library dropped into a repository (`lib/` and `vendor/` folders, well-known library names, a licence banner at the top), since those are not under the repository's own licence.

Licences are as GitHub reported them on 2026-11-22. That is a signal, not a legal audit. In particular, a Python file copied into a repository from elsewhere is not detected.

## Limits

- Python and JavaScript only. C, C++, TypeScript, MATLAB and R are untouched.
- Only functions that stand alone. Anything needing a class, a file, a network, scipy, pandas or a browser page is left behind, which is still most of what makes these repositories what they are. numpy brought the calculating core of the scientific ones in; it is more of the fruit than before, not the whole fruit.
- "Fits by shape" links are real calls but usually nonsense: a temperature fed to something expecting a frequency. That is deliberate, and labelled. Long chains still tend to decay from numbers into text.
- A function is called with its other arguments fixed at whatever values worked when it was probed, which is why test values such as `f-round` and `Hello World 42` turn up inside some results.
- Name matching is crude: a short word list and the function's name. It has not been taught what the values mean.
