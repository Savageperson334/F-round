# F-round — Godot Exploration Plan for Claude

**Status:** Exploratory handoff, not a locked game design document  
**Starting reference:** `Savageperson334/F-round` `main` at `edcf493` (2026-11-22)  
**Target:** Godot 4.5.x, with 4.5.1 a sensible local baseline  
**Working premise:** One player. One room. A computer. An escalating number of profoundly incompatible ideas.

> **Build a room that can become anything. Do not build a game about reading a catalogue.**

## The brief

F-round currently contains a broad repository catalogue—**4,169 unique GitHub repository leads**, with GitHub metadata and an HTML collision browser—but no committed Godot project at this reference point.

The long-term scope is **intentionally enormous**. F-round has two parallel potential futures:

- **A. Game:** A strange but substantial interactive world made from real, disparate mechanisms, scientific ideas, obscure software, odd institutions, physical contraptions, systemic consequences, and surreal comedy. It can be thoughtful, beautiful, grotesque, funny, serious, uncanny, and mechanically deep. Not every moment must fit one genre or aesthetic.
- **B. Practical laboratory:** Independently useful experimental programs, interfaces, visualizations, instruments, conversions, educational simulations, and art-producing machines. Game modules may become real utilities and vice versa.

**This document does not choose between A and B.** Build a Godot environment that lets us *discover* which ideas become interesting once they are tangible. Keep the catalogue research and the playable experiments separate enough that either can thrive independently.

The first Godot environment is **a laboratory / workshop / office / cabinet of curiosities**, but that is a convenient test environment, not confirmed lore. We should be able to replace it with an impossible museum, city, cave, observatory, post-apocalyptic bunker, or a world that changes its architecture as the player connects things.

---

## 1. The experience we are after

A player enters a room. There is a computer because some tools genuinely require one. But the room must **not** be a computer interface wearing 3D wallpaper.

The player should be able to:

- Walk around a convincing 3D environment and look at things.
- Handle at least a few objects physically: pick up, place, insert, route, connect, carry, inspect, or activate.
- Use specialised devices in different ways. A keyboard, dial, microscope, printer, terrarium, map wall, physical scanner and machine tray should not all open the same generic menu.
- Produce an **artifact** that can outlive the interaction: a printout, signal, waveform, cassette, image, fluid pattern, diagram, specimen, coordinate, voice fragment, dataset, or something even stranger.
- Take an artifact made in one system and try it in another system, sometimes with surprising consequences.
- Find obscure real-world ideas organically, without being required to read long research pages.
- Experience moments that are funny or deeply odd **because something in the simulation happened**, not merely because a joke was written on the screen.

A key principle: **the source projects are inspiration and possible machinery, not an in-game shopping list.** A player should encounter what an algorithm *does*, not be forced to care that it is a GitHub repository.

## 2. What the first room might contain

Do not treat this as a fixed inventory. Treat each as a candidate *interaction family*. Art assets can remain simple placeholders until the behaviour is good.

| Family | Possible physical interaction | Underlying real-world ideas | Result |
| --- | --- | --- | --- |
| Archive computer | Search, inspect, load, compare, run | Repository metadata, parsing, data visualisation | Files, maps, graphs, instructions |
| Signal bench | Turn knobs, cable outputs, tune radio | Formant synthesis, oscillators, SSTV, sonification | WAV / signal artifacts |
| Living chamber | Add matter, expose light/sound, alter environment | Cellular automata, fungal networks, agent-based biology | Evolving organisms, branching paths |
| Optics bench | Focus, rotate, magnify, shine light | Microscopy, particle detection, texture/optics models | Images, contours, measurements |
| Plotter / printer | Feed paper, load a drawing, print | Generative geometry, SVG paths, thermal printing | Tangible diagrams, receipts |
| Map / evidence wall | Pin, overlay, arrange, connect | Historical maps, shipwrecks, timelines, provenance | A discovery, contradiction, route |
| Mechanical bench | Assemble, align, rotate, attach | Origami, mechanical linkages, robotics, physical synthesis | A working contraption |
| Experimental vessel | Feed signals to a visible phenomenon | Ferrofluids, flow fields, particles, reaction-diffusion | Dynamic physical patterns |
| Room itself | Observe wall/floor/ceiling effects | Geometry nodes, procedural architecture, topology, signals | Room mutation, hidden spaces |

Some experiments may eventually require a full-screen UI, a 3D visualization, custom audio, a simulation sandbox, an NPC, or an entirely new room. **The station format is not a constraint on ideas.**

### Model and art direction

- Start with greyboxes / simple CSG or primitive meshes plus readable lighting and silhouettes.
- Use **Blender** and the user's **BlenderKit subscription** for later distinctive props or hero equipment, but don't make the prototype depend on downloading paid assets.
- Potential quick CC0 sources: Kenney, Quaternius, Poly Haven. Verify the license for each selected model, material, or texture.
- Prefer `.glb` / glTF for practical Godot scene imports. Keep pivots, size, collision shapes and interaction points explicit.
- Avoid committing non-redistributable BlenderKit source models or paid materials into this public repo; document asset provenance and use placeholders if needed.
- An intentionally mismatched visual language may eventually be part of the design: pristine equipment next to obsolete industrial machinery, apparently ordinary furniture around impossible behaviour. It does **not** need a polished unified art style now.

---

## 3. The most important design problem: how ideas become transferable

Long term, the interesting unit is not a repository. It is a **capability** and a **thing that capability produces**.

Examples:

- Text → voice
- Sound → waveform or classification
- Waveform → vibration, motion or ferrofluid pattern
- Image → contours
- Contours → plotter motion, folded surface or biological branches
- Graph → path, narrative structure, electrical wiring or map
- Coordinates → map, route, room geometry
- Measurements → data visualization, sound or strange printed record
- Artificial-life state → ecological event, object behaviour or persistent mutation

We need a small **artifact-exchange layer**, but *not* a giant abstract universal framework before there is gameplay.

A reasonable first model could be:

```
Artifact:
  id
  kind              # signal, image, path, map, text, specimen, event, etc.
  payload           # small typed data for the prototype
  title / description
  origin_station
  source_reference  # optional real-source URL and version
  simulated         # distinguishes fictional/synthetic from actual measurements
```

Possible station behaviours:

```
can_accept(artifact) -> bool
accept(artifact) -> response / new artifact
interact(player) -> focus mode / physical action
```

These are **concepts, not mandatory class names or a required software architecture**. Use simple GDScript Resources, typed dictionaries or small objects where that is enough. Do not build a general dependency-injection system, plugin marketplace, or abstract adapter runtime before two stations actually exchange something.

The room should also support **physical identity** for artifacts: a paper sheet, vial, cassette, floppy, specimen slide, wooden block, or data card. A data artifact may have multiple physical representations. Not every transfer has to happen through a cable or computer.

### Keep the simulation distinct from presentation

A fluid experiment might first be a cheap shader. Later it might be replaced by a more accurate implementation, or an external program. If its input/output contract remains stable, the in-room object should not need wholesale replacement.

This is also how practical applications could share experimentation logic with the game without becoming dependent on Godot scenes.

---

## 4. First build: an intentionally small but flexible room

**Deliver a runnable Godot prototype**, not another huge catalogue or an architecture-only PR.

Suggested first slice:

1. **3D room and player.** First-person is the simplest initial test, not a permanent game-camera decision. Basic mouse look, walking, readable collision, inspect/interact input and a way to exit focused interfaces.
2. **A genuinely usable computer.** It can display a small searchable subset or imported index of real F-round entries, plus an obvious button to produce a test artifact. Keep the authoritative catalogue unchanged. The CSV already contains 4,169 entries and 21 columns at the starting reference; avoid putting all content into scene files by hand.
3. **One non-computer source device.** A dial-driven signal generator, radio receiver, image scanner, small growth chamber, or anything Claude finds quick to make *physically satisfying*. The player should interact with it in 3D, not just by clicking a UI menu.
4. **One transformation device.** An oscilloscope-like display, ferrofluid bowl, mechanical plotter, terrarium, or microscope that visibly responds to an artifact.
5. **One persistent output.** A printout, diagram, specimen, signal, path, or evidence card that can be carried, viewed, pinned, or reused.
6. **At least one cross-device chain.** Interact with device A → generate something → physically bring or route it to device B → see a different result → preserve the result as an object or persistent state.

A possible **test chain, not a binding creative direction**:

```
Computer or analog sound device
  -> synthesized signal
  -> experimental chamber turns signal into movement/contours
  -> printout or diagram
  -> evidence board displays the output
  -> room reacts subtly / new option appears
```

A completely different viable test chain:

```
Historical map snippet
  -> tracing desk converts region boundaries into paths
  -> procedural machine folds or grows the paths
  -> resulting object can be placed on a pedestal
  -> another device interprets its geometry as music
```

The first chain should be **genuinely playable and visibly interesting**. Not just four boxes with “Interact” prompts and no substantial behaviour.

### A sensible initial interaction vocabulary

- Walk / look / interact.
- Inspect an object by bringing it into a focused view.
- Pick up and place at least one small physical object.
- Operate one or two kinds of controls (toggle, knob, dial, button, lever, slider, slot).
- A clear way to enter and leave a computer or other focused view.
- Contextual feedback for incompatible artifacts (“this device doesn't understand that signal”), with room for surprising converters later.
- A minimal journal / evidence surface or persistent output; no giant inventory UI required.

Avoid exhaustive physics handling and arbitrary drag-and-drop for everything at first. Simple snap slots, stable held-object behaviour and explicit connection points are enough.

---

## 5. Make the space extensible without prematurely building a universe

This little room is only the **first laboratory of possibility**.

Future areas may take almost any form:

- A cavern that speaks through its measured topology.
- A warehouse of physical industrial automation.
- A pseudo-natural biosphere with evolving artificial organisms.
- A museum of mislabeled historical maps and artifacts.
- A weather station that receives broadcasts from objects that should not communicate.
- A machine shop where algorithms are manufactured as physical components.
- A city whose infrastructure follows bizarre graph-theoretic laws.
- A subterranean archive of lost software and extinct file formats.
- A room that expands or reorganizes its own geometry.
- Entirely different games embedded as experiments—tactical combat, simulation, investigative puzzles, strange social encounters, or generative art.

Those are **directional examples**. Nothing should force F-round to choose a science-museum theme, a bureaucratic comedy setting, or an endless series of puzzle rooms.

We can add NPCs, lore, goals, quests, stakes, threat, survival mechanics, procedural world generation, multiplayer or something else if a prototype makes them compelling. None is a prerequisite to build the room.

**Tonal scope:** intelligent, serious, silly, uncanny, moving, ridiculous, grotesque and unexpectedly sincere, with no obligation to stay in one register. Let bizarre consequences emerge from understandable rules instead of substituting random jokes for mechanics.

---

## 6. Implementation direction for Claude (guidance, not hard architectural law)

Suggested Godot project location:

```
F-round/
  README.md                    # existing project manifesto
  data/                        # existing research catalogues; preserve
  godot/                       # new Godot 4.5.x project
    project.godot
    scenes/
      world/                    # room and future environments
      player/
      stations/
      artifacts/
      ui/
    scripts/
      interactions/
      artifacts/
      systems/
    assets/
      placeholders/
      imported/
    data/
      selected_repos.json       # generated subset if useful; not a replacement master
  experiments/                 # optional independent practical tools later
  docs/                         # plans and source/asset provenance
```

Names and directory layout may change if a simpler design is more natural. Do **not** restructure the existing catalogue without a reason.

Godot choices worth testing:

- `CharacterBody3D` + camera and ray interaction for the player.
- Small reusable `Interactable` logic with clear focus/exit and hold/place states.
- `SubViewport` / viewport textures when an in-world screen truly needs a rendered interface.
- Native Godot `Control` UI for computer work rather than trying to embed the project's existing HTML browser prematurely.
- Signals/events for station interaction. A tiny artifact resource or record for transfer.
- Instanced station scenes with their own logic; no monolithic script controlling every device.
- Light-weight procedural visuals/shaders for living or reactive phenomena.
- Modular scene assets, with collisions separated from decoration.

A practical stand-alone algorithm may remain in Python, JS, Rust or another language. Godot should not assume it can directly execute every repo. First implement a small locally reproducible bridge for **one verified capability**. External-process adapters, if added later, should use explicit allowlisted commands and isolated inputs rather than execute arbitrary GitHub code.

### Catalogue integration

`data/F_ROUND_MASTER_4100.csv` is a research source, not gameplay content that should be blindly loaded into the level.

Possible workflow:

- A small, reproducible importer builds a filtered `selected_repos.json` for the room.
- The computer UI can search names/categories and show real GitHub descriptions, source URLs and confidence markers.
- Selected discoveries can unlock an **experiment card** or station content.
- Most rows have not been inspected beyond GitHub metadata; keep that uncertainty explicit.
- Do not expose arbitrary external downloads, source execution, untrusted Markdown rendering, or live GitHub API requests as core first-slice features.

### Tests and verification

- Godot project imports and starts without requiring a paid asset, cloud service or API key.
- Player can walk, focus and interact; focus modes restore input/cursor correctly.
- At least one complete artifact exchange works repeatedly without losing state.
- Reloading the room does not create duplicate stations or orphan held objects.
- Real source metadata, fictitious observations and synthetic experiment data have distinct status.
- Check the Godot editor import/headless parse if the engine exists in the execution environment; report honestly if it doesn't.
- Include a short controls guide and a reproducible manual test path.
- Do not add speculative smoke tests for systems that don't yet exist.

---

## 7. Discovery backlog: directions to try after the first slice

Keep a **living pile of experiments**, not a committed feature checklist. We want diversity of mechanics and interaction modes:

| Strange pairing | Playable or physical test | Practical tangent |
| --- | --- | --- |
| Formant speech + map geometry | A machine speaks a cave or coastline | Accessible sonification tool |
| Artificial life + electronics | Growth network becomes a circuit | Educational graph simulator |
| Microscopy + plotter | A specimen becomes a reproducible drawing | Vector extraction |
| Atmospheric telemetry + radio | Invisible weather changes equipment | Weather sonification and signal visualizer |
| Origami + procedural geometry | Fold a computed shape into a physical tool | Fold-pattern converter |
| Historic borders + evidence wall | Competing timelines alter a place | Historical map comparison utility |
| Number stations + generated language | A signal seems to develop syntax | Generative speech instrument |
| Shipwrecks + astronomical navigation | A route is recoverable from different records | Spatial historical analysis |
| Plant signals + ferrofluid | A vessel responds to live or simulated measurements | Data-driven installation |
| Bacterial colonies + architecture | A room grows according to a simulation | Procedural morphology tool |
| Typewriters + terminal protocols | Obsolete hardware operates advanced systems | Retro interface toolkit |
| Music + mechanical plotting | Sound physically draws itself | Generative score/plot instrument |
| Particle simulations + social systems | Tiny agents influence larger structures | Simulation visual analytics |
| Thermal receipts + provenance | Every action leaves an auditable artifact | Event-to-print reporting |
| Ancient formats + scene geometry | Data from obsolete media changes 3D space | File format visual explorer |

Use the existing [COLLISIONS.md](../COLLISIONS.md), [FUTURES.md](../FUTURES.md), [ATLAS.md](../ATLAS.md), and [master catalogue](../data/F_ROUND_MASTER_4100.csv) as inspiration. The links above are relative to this document's proposed `docs/` location.

---

## 8. Parallel tracks: game and practical invention

When one experiment becomes interesting:

**Game track:** Express the capability as a tactile interactive station, systemic event, world change, puzzle, creature, machine or story consequence.

**Practical track:** Ask whether the same input/output transformation is valuable on its own as a small app, library, educational demonstration, hardware utility or generative art system.

Track experiments in a way that does not *force* practical tools to depend on a running game, nor force the game to import entire external applications.

Ideas can graduate independently—or be abandoned without harming the room.

---

## 9. The rough build sequence

These are **layers of exploration**, not schedule commitments or a rigid sprint plan.

### Layer 0 — Working foundation

- Inspect current repository and document how to launch the new Godot project.
- Create Godot 4.5.x project under a separate folder; preserve research files.
- Establish a basic 3D room and usable player movement/interaction.
- Ensure there is a visible, inspectable object and a functioning focus/exit loop.

### Layer 1 — First genuine experiment

- Implement a computer and one physically operated non-computer station.
- Produce one visible or audible phenomenon that is not a placeholder.
- Implement transferable artifact/output with a clear origin.
- Provide a short reproducible demo of the chain.

### Layer 2 — Disparate collisions

- Add a third station that behaves differently from the first two.
- Route one artifact into a surprising new context.
- Introduce at least one persistent environmental consequence or discoverable relationship.
- Capture which idea was fun and why; abandon weak interactions quickly.

### Layer 3 — Expansion without centralizing everything

- Build a few different station families and optional locations.
- Introduce richer catalogue browsing, provenance and a living discovery journal.
- Start optional independent practical prototypes as they become compelling.
- Refine visual identity using selected, properly licensed assets.

### Layer 4 — Let an actual game identity emerge

- Look for the experiences people repeatedly choose to engage with.
- Consider deeper goals, NPCs, environments, exploration, narrative, systemic complexity and long-term progression **based on what the experiments demonstrate**.
- Keep room for an entirely different concept if something better emerges.

---

## 10. Instructions to Claude for the next coding pass

**Start coding the Godot exploration now; do not respond with another purely conceptual proposal.**

Please:

1. Confirm the current repository head and inspect existing files before changing them. At this planning snapshot there is **no Godot project**; if one has since been added, adapt to it instead of creating a parallel duplicate.
2. Implement a simple **runnable 3D room** and usable first-person player with interact/focus/exit controls.
3. Put a **computer** in the room, but make at least one **non-computer apparatus** genuinely interactive in a physically distinct way.
4. Implement a **small artifact or signal handoff** so that an action in one station can produce a visible, audible or tangible consequence in another.
5. Use procedural placeholders; don't block on asset shopping or a polished UI. We can add CC0 / BlenderKit props later with per-asset provenance.
6. Build just enough shared logic to make a second and third apparatus practical. No universal framework, no mass-imported GitHub source, no fake capabilities, no sprawling menu system.
7. Write a short `godot/README.md` explaining how to launch, the current controls, what actually works, what is simulated, and the immediate next experiments.
8. Test the project with the available Godot binary and report **what you actually ran**, along with any missing engine/tool limitations.
9. Preserve Concept A (wild game) and Concept B (real experimental workshop) in the design. Neither should become a footnote.
10. Make creative decisions where the plan is loose. If you discover an obviously more interesting interaction, prioritize it and note why.

**The success condition isn't “a room with six labelled props.”** It's: *“I walked into a room, experimented with something physical, connected two unlikely systems, and got a result that made me want to try another connection.”*

## What not to overfit

- No fixed lore or narrative premise.
- No fixed number of stations.
- No requirement that every repo is represented in the game.
- No requirement that every experiment is amusing; some should be scientifically fascinating or genuinely useful.
- No assumption that computers are the only way to use software.
- No assumption that every component must be written in GDScript.
- No premature full-world roadmap or monolithic game architecture.
- No automatic arbitrary-code execution from catalogue entries.
- No unlicensed assets committed to the public repository.
- No pursuit of a polished art style at the expense of a working interesting interaction.

**F-round's scope remains extravagantly wide. The first step should be small only so that we can start discovering which directions deserve to become enormous.**
