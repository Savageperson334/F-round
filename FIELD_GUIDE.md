# F-round — Field Guide

This project does **not** begin with a product. It begins with strange parts and a disciplined way of deciding which ideas deserve an experiment.

## Four states of a repository

1. **Spotted** — GitHub search exposed its name; do not assume the description, demo, license or code quality.
2. **Scouted** — repository exists and its stated purpose / metadata have been inspected, but not its implementation. Most of [ATLAS.md](ATLAS.md) is here.
3. **Tested** — a repeatable small local smoke test works; actual inputs and outputs captured.
4. **Reused** — source or assets have been imported into F-round **with license and attribution checked**. Being public or on GitHub is not a license.

An archived project can still be creatively useful; distinguish *a working dependency* from *a technical reference* or *pure aesthetic inspiration*.

## Pick by surprise, filter by usefulness

For any proposed collage, ask:
- **Artifact:** What can a person see, hear, print, compare, measure, learn, or do after an hour?
- **Bridge:** What travels between the parts: JSON events, images, paths, samples, graph edges, time series, shapes, instructions, or physical signals?
- **Provenance:** Can every factual output be traced to inputs and source code? Can simulation and measured reality be distinguished?
- **Constraint:** What is the smallest version that makes the connection real, without new hardware, cloud accounts, paid APIs, or privileged device access?
- **Failure:** If one part is unavailable, can the other part still do something meaningful?

A combination is genuinely useful when the new output reveals, makes tangible, validates, compares or documents something that the individual source projects cannot easily do alone.

## Practical design rule: adapters before mergers

Do not begin by copying multiple codebases into one mega-repo. Start by defining a tiny intermediate format:

```json
{
  "id": "sample:001",
  "kind": "observation",
  "source": {
    "project": "example/repo",
    "url": "https://example.invalid/dataset",
    "license": "CHECK_BEFORE_USE"
  },
  "observed_at": "2026-11-22T00:00:00Z",
  "location": null,
  "measurements": {},
  "confidence": null,
  "synthetic": true
}
```

Keep time zones, units, coordinate systems and uncertainty explicit. Simulators should always tag their events as synthetic. Artists and data-science tools can consume the same records without modifying the underlying evidence.

Possible bridges:
- **CSV/JSON** for instruments and timeseries
- **SVG/GeoJSON** for cartography, ornament, textiles and plotting
- **WAV/MIDI** for sonification and unusual voices
- **PNG/JPEG** for scanned media and print
- **GraphML/JSON** for ancestry, relationships and code history
- **MQTT/WebSocket** for local sensors and event streams

## The F-round experiment folder convention (proposed)

```
experiments/
  <collision-name>/
    README.md          # Why these pieces, what it proves
    SOURCES.md         # Direct links, versions, licenses
    examples/          # Synthetic or properly licensed demo input
    src/               # Original adapters / glue
    expected/          # Known-good outputs
```

Keep the core experiment independent of unfinished upstream software. A thin adapter, small synthetic sample, and reproducible output are a successful first step.

## Licensing, attribution, security

- MIT/Apache/BSD/MPL/GPL/AGPL are different legal regimes; check project and model/data licenses individually. Never assume GPL, AGPL, assets and training models all have the same requirements.
- Repository descriptions and ideas are not copyrighted source code; link, describe, and independently implement when a code license is absent.
- Public data can still implicate sensitive locations, individual people, copyrighted images, private telemetry or ecological conservation concerns.
- Do not connect arbitrary GitHub repositories to your computer, credentials or personal accounts without sandboxing and source inspection.
- Archived science tools need validation before scientific or medical use; an evocative graph is not proof.

## Where to start

- For a **weird but useful artifact**: [The Universal Receipt](COLLISIONS.md#14-the-universal-receipt).
- For **history and research**: [The Accidental Time Machine](COLLISIONS.md#1-the-accidental-time-machine).
- For **hardware-free artificial life**: [The Artificial Ecology That Writes Poetry](COLLISIONS.md#8-the-artificial-ecology-that-writes-poetry).
- For **physical fabrication**: [The Fossil That Can Knit](COLLISIONS.md#3-the-fossil-that-can-knit).
- For the **meta-tool that produces new ideas**: [F-round: The Collision Engine](COLLISIONS.md#15-f-round-the-collision-engine).

Each starts with a one-evening proof; none requires choosing a product direction immediately.
