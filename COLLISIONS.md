# F-round — Collision Proposals

These are **proposed original mashups**, not existing integrations. Source repositories are real; design concepts, feasibility estimates, and product names are our inventions. We should make small tests before copying code. Check every code/data/model license independently, including unknown licenses. See [ATLAS.md](ATLAS.md) for the raw parts inventory.

## 1. The Accidental Time Machine

*Historical maps + accidental shipwrecks + living geography*

**Ingredients:** [`aourednik/historical-basemaps`](https://github.com/aourednik/historical-basemaps) · [`timwaters/mapwarper`](https://github.com/timwaters/mapwarper) · [`Tristan-Hotham/world-shipwrecks`](https://github.com/Tristan-Hotham/world-shipwrecks) · [`Tristan-Hotham/did-lighthouses-work`](https://github.com/Tristan-Hotham/did-lighthouses-work) · [`OpenRefine/OpenRefine`](https://github.com/OpenRefine/OpenRefine)

**Why it might matter:** A map you can scrub across centuries, but the remarkable events are where the layers disagree: new lighthouses, vanished shipping routes, borders changing under a wreck site. It is a historical comparison instrument, not just a timeline.

**Build-one-evening proof:** Use local GeoJSON boundaries plus a subset of shipwreck points. Click a date, animate borders, show primary-source links and map-data uncertainty. Add a 'this might be wrong' pane that preserves provenance.

**Unhinged extension:** Let one time period slowly leak into another and print a receipt for each historical inconsistency.

**Actual complications:** Historic dates and locations are inconsistently recorded. Do not imply causation from a visual correlation. Check dataset reuse rights separately.

---

## 2. The Number Station of the Living Earth

*Wildlife acoustics + weather transmissions + analog encoding*

**Ingredients:** [`kitzeslab/opensoundscape`](https://github.com/kitzeslab/opensoundscape) · [`birdnet-team/BirdNET-Analyzer`](https://github.com/birdnet-team/BirdNET-Analyzer) · [`wojlin/WEFAX`](https://github.com/wojlin/WEFAX) · [`dnet/pySSTV`](https://github.com/dnet/pySSTV) · [`chamelaeon/Numbers-Station-Generator`](https://github.com/chamelaeon/Numbers-Station-Generator) · [`nthmost/artery-thermal`](https://github.com/nthmost/artery-thermal)

**Why it might matter:** Public environmental recordings become a very old-fashioned station log: identifiable animals, dates and places translated into eerie coded voice, imagery and physical paper.

**Build-one-evening proof:** Use an existing labelled audio sample; emit a plain JSON observation, generate a station message and render an SSTV image. Label synthetic signals clearly. No radio transmitter required.

**Unhinged extension:** An underwater call from a whale becomes a weatherfax; a bird detected before dawn becomes a numbers-station call sign.

**Actual complications:** Use recorded/cited observations; classification probabilities are not guaranteed species facts. Some source code has no declared license.

---

## 3. The Fossil That Can Knit

*Palaeontology + botanical diagrams + textiles*

**Ingredients:** [`XiaokangLiuCUG/DeepMorph`](https://github.com/XiaokangLiuCUG/DeepMorph) · [`lrncrd/PyPottery`](https://github.com/lrncrd/PyPottery) · [`rybakov-ks/ParticleAnalyzer`](https://github.com/rybakov-ks/ParticleAnalyzer) · [`inkstitch/inkstitch`](https://github.com/inkstitch/inkstitch) · [`severalprojects/Mosaic_Knitting`](https://github.com/severalprojects/Mosaic_Knitting) · [`friedrich-goetze/punch-card-maker`](https://github.com/friedrich-goetze/punch-card-maker)

**Why it might matter:** Scientific shape measurements become physical patterns: a cephalopod cross-section or fragment profile could drive repeatable embroidery and knitting designs.

**Build-one-evening proof:** Start with an openly licensed contour image. Extract and simplify its geometry, convert to monochrome tiled stitch-map and export SVG. No machine required to preview.

**Unhinged extension:** Every geological period yields its own family of garments and loomed patterns.

**Actual complications:** Do not pretend decorative stitches preserve measurement accuracy. Textile patterns have hardware-specific requirements and unknown source licenses.

---

## 4. The Cave Organ

*Cave surveys + 3D geometry + spoken resonance*

**Ingredients:** [`Stalagmight/Stalagmight`](https://github.com/Stalagmight/Stalagmight) · [`ndschonegg/CaveCAD`](https://github.com/ndschonegg/CaveCAD) · [`james-trayford/strauss`](https://github.com/james-trayford/strauss) · [`chdh/klatt-syn`](https://github.com/chdh/klatt-syn) · [`ArtInLines/VectorFields`](https://github.com/ArtInLines/VectorFields)

**Why it might matter:** A surveyed cave becomes a playable spatial instrument. Tunnel lengths, turns and branching determine rhythms, tones and phonemes; the data remains inspectable.

**Build-one-evening proof:** Import a tiny sample cave survey CSV/GPX, show a 2D network, synthesize one pitched event per segment. Click a segment to hear it.

**Unhinged extension:** The cave 'speaks' its own branching grammar; two connected caves form a duet.

**Actual complications:** Coordinate systems, survey metadata, and whether the actual cave can be publicly located need careful handling.

---

## 5. The Misbehaving Instrument

*Geochemical calculations + real instrument protocols + absurd displays*

**Ingredients:** [`jedick/CHNOSZ`](https://github.com/jedick/CHNOSZ) · [`ignasi-p/piper-diagrams`](https://github.com/ignasi-p/piper-diagrams) · [`ohlincha/crosstitrate`](https://github.com/ohlincha/crosstitrate) · [`rybakov-ks/ParticleAnalyzer`](https://github.com/rybakov-ks/ParticleAnalyzer) · [`iclubu/Plotter-Studio`](https://github.com/iclubu/Plotter-Studio) · [`kineteklabs/twotone`](https://github.com/kineteklabs/twotone)

**Why it might matter:** An unusual lab workstation that turns legitimate science data into simultaneously precise diagrams and playful physical or sonic outputs.

**Build-one-evening proof:** Use synthetic data only. Build an input table, one valid scientific plot, one experimental sonification. Keep measured/scientific and artistic outputs visually separate.

**Unhinged extension:** A titration becomes a pen-plotting choreography or a sound sculpture.

**Actual complications:** Never let artistic transformations masquerade as validated instrument results; check hardware support and calibration.

---

## 6. The Forgotten Computer Department

*Virtual old computers + forgotten media + cryptography + mechanical typewriting*

**Ingredients:** [`elmerucr/punch`](https://github.com/elmerucr/punch) · [`johnsonwust/pico-retrotouch`](https://github.com/johnsonwust/pico-retrotouch) · [`latchdevel/HxCFloppyImageConverter`](https://github.com/latchdevel/HxCFloppyImageConverter) · [`RealGrep/lorenz-cipher-sim`](https://github.com/RealGrep/lorenz-cipher-sim) · [`xunker/panasonic_typewriter_interface`](https://github.com/xunker/panasonic_typewriter_interface) · [`Timwi/EsotericIDE`](https://github.com/Timwi/EsotericIDE)

**Why it might matter:** A fictional computer archaeology workbench that accepts old disk images and produces reproducible artifacts from vintage-inspired virtual machines.

**Build-one-evening proof:** Start with a wholly synthetic dataset and build a CLI that archives an input blob, generates a checksum, encodes a note and prints it in a retro format.

**Unhinged extension:** A fake 1982 department continues mailing diagnostic reports in 2026.

**Actual complications:** Disk image formats are many; avoid assuming any tool can execute arbitrary historical software. Security-sandbox untrusted files.

---

## 7. The Silent Cosmic Observatory

*Invisible sky events + weather + E-ink*

**Ingredients:** [`roman-dvorak/caelum`](https://github.com/roman-dvorak/caelum) · [`Smerity/bitflipped`](https://github.com/Smerity/bitflipped) · [`zacharyd3/Blitz-LightningTracker`](https://github.com/zacharyd3/Blitz-LightningTracker) · [`k-a-d-y/cosmobarometer`](https://github.com/k-a-d-y/cosmobarometer) · [`tyler-void/kinda-frame`](https://github.com/tyler-void/kinda-frame) · [`zc00838/ESP32-Eink-Mosaic`](https://github.com/zc00838/ESP32-Eink-Mosaic)

**Why it might matter:** A slow changing physical display of real events we normally never notice: meteors, aurora forecasts, lightning and the rare bit flip.

**Build-one-evening proof:** Consume cached/recorded sample JSON events with provenance. Render a black-and-white card per event. Refresh a web dashboard before considering real hardware.

**Unhinged extension:** An E-ink wall that ages like geological strata, storing a physical daily calendar of Earth's invisible moments.

**Actual complications:** Models and feeds have outages, usage limits, false positives and incompatible location scopes. Cosmic-ray inference from bit flips is uncertain.

---

## 8. The Artificial Ecology That Writes Poetry

*Artificial organisms + emergent graphs + poetry and voice*

**Ingredients:** [`xcontcom/neuroparticles2`](https://github.com/xcontcom/neuroparticles2) · [`gkirgizov/die`](https://github.com/gkirgizov/die) · [`mundyreimer/rewriting_systems`](https://github.com/mundyreimer/rewriting_systems) · [`rossgoodwin/poetizer`](https://github.com/rossgoodwin/poetizer) · [`chdh/klatt-syn`](https://github.com/chdh/klatt-syn) · [`cosmosgl/graph`](https://github.com/cosmosgl/graph)

**Why it might matter:** A simulation where language is genuinely derived from agent events rather than pasted on top. Evolutionary history creates grammatical events, and voices narrate failures and discoveries.

**Build-one-evening proof:** Generate a deterministic set of ecosystem events (birth, split, contact, death). Convert event records into sentences with a tiny grammar and render a graph.

**Unhinged extension:** Each artificial species develops a dialect from its lineage.

**Actual complications:** Neither ecological realism nor genuine language emergence is guaranteed. Use seeded simulations and treat output as artwork.

---

## 9. The Cabinet of Erroneous Maps

*Map anomalies + scanned artifacts + forensic inspection*

**Ingredients:** [`aourednik/historical-basemaps`](https://github.com/aourednik/historical-basemaps) · [`timwaters/mapwarper`](https://github.com/timwaters/mapwarper) · [`tropy/tropy`](https://github.com/tropy/tropy) · [`GuidoBartoli/sherloq`](https://github.com/GuidoBartoli/sherloq) · [`OpenRefine/OpenRefine`](https://github.com/OpenRefine/OpenRefine)

**Why it might matter:** The data errors become objects of research: who labelled this border, which 1800 polygon absorbed a city, how trustworthy is the scan?

**Build-one-evening proof:** Use one known historical map discrepancy. Show neighbouring-year source maps, feature geometries, confidence notes and a small evidence ledger.

**Unhinged extension:** A museum of contradictions in supposedly authoritative maps.

**Actual complications:** A discrepancy is not always a mistake. Retain disputed claims rather than auto-correcting history.

---

## 10. The Apiary Radio

*Beehive sensors + bioacoustic analysis + generative music*

**Ingredients:** [`MacNite/HiveHub`](https://github.com/MacNite/HiveHub) · [`limousyf/BeehiveSensor`](https://github.com/limousyf/BeehiveSensor) · [`kitzeslab/opensoundscape`](https://github.com/kitzeslab/opensoundscape) · [`interactive-sonification/pya`](https://github.com/interactive-sonification/pya) · [`tyler-void/kinda-frame`](https://github.com/tyler-void/kinda-frame)

**Why it might matter:** A useful monitoring station whose status is audible as well as visible. Ambient layers can encode sensor changes without pretending to diagnose hive health.

**Build-one-evening proof:** Replay a synthetic JSON stream of hive weight, humidity and sound level. Produce a graph and a two-minute sonic/weather summary.

**Unhinged extension:** A hive broadcasts its slow internal weather to a disused weather station.

**Actual complications:** Audio and temperature fluctuations are not reliable swarm/health diagnoses without domain validation. Hardware support varies.

---

## 11. The World in Three Different Motions

*Planes + wildlife migration + ships and wrecks*

**Ingredients:** [`MrJohn6774/SkyPulse`](https://github.com/MrJohn6774/SkyPulse) · [`aloftdata/bird-migration-flow-visualization`](https://github.com/aloftdata/bird-migration-flow-visualization) · [`Tristan-Hotham/world-shipwrecks`](https://github.com/Tristan-Hotham/world-shipwrecks) · [`cosmosgl/graph`](https://github.com/cosmosgl/graph) · [`ArtInLines/VectorFields`](https://github.com/ArtInLines/VectorFields)

**Why it might matter:** A map that simultaneously visualizes human-machine motion, seasonal animal motion and the historical consequences of ocean travel.

**Build-one-evening proof:** Start with archived openly licensed trajectories from all three domains and show time-series layers. Compare speed and density in explicitly different units.

**Unhinged extension:** Mix them into a 3D field of all the things that crossed this point in Earth's recent memory.

**Actual complications:** Data periods, coverage, privacy, and ADS-B radio collection limits are not naturally comparable.

---

## 12. The Internet Is a Geological Layer

*Protocol archaeology + code ancestry + old texts*

**Ingredients:** [`dirtbags/fluffy`](https://github.com/dirtbags/fluffy) · [`OpenRefine/OpenRefine`](https://github.com/OpenRefine/OpenRefine) · [`matheusabrantes/genealogy-atlas`](https://github.com/matheusabrantes/genealogy-atlas) · [`zakkariyaa/digital-garden`](https://github.com/zakkariyaa/digital-garden) · [`dloscutoff/Esolangs`](https://github.com/dloscutoff/Esolangs) · [`latchdevel/HxCFloppyImageConverter`](https://github.com/latchdevel/HxCFloppyImageConverter)

**Why it might matter:** Study software ecosystems as archaeological sites: format migrations, forks, protocols and forgotten interface conventions form strata.

**Build-one-evening proof:** Take a small hand-curated set of open-source projects, their release dates and file formats; render a lineage network with source citations.

**Unhinged extension:** Classify extinct file formats as fossils and active libraries as strange descendant species.

**Actual complications:** Repo history is incomplete; code genealogies and claims of derivation require evidence. Do not include token speculation.

---

## 13. The Texture That Became a Tree

*Micrograph → flow field → procedural organism → plotter*

**Ingredients:** [`rybakov-ks/ParticleAnalyzer`](https://github.com/rybakov-ks/ParticleAnalyzer) · [`IMBalENce/openECCI`](https://github.com/IMBalENce/openECCI) · [`sleeping-h/vector-fields`](https://github.com/sleeping-h/vector-fields) · [`paulina-duda/on-growth-and-form`](https://github.com/paulina-duda/on-growth-and-form) · [`davidhampgonsalves/Generative-Tree-Rings`](https://github.com/davidhampgonsalves/Generative-Tree-Rings) · [`lilkraftwerk/lineboi3000`](https://github.com/lilkraftwerk/lineboi3000)

**Why it might matter:** Use real scientific textures as material for generative physical art while retaining a clear path back to the source image.

**Build-one-evening proof:** Input public-domain sample microscopy image, compute a simple orientation field, trace streamlines and export SVG with provenance embedded in metadata.

**Unhinged extension:** Tree rings grow according to defects in the crystal they're printed from.

**Actual complications:** Image rights and scientific labels; large rasters need decimation. This is a visual transformation, not scientific inference.

---

## 14. The Universal Receipt

*Anything measurable → tiny illustrated physical evidence*

**Ingredients:** [`nthmost/artery-thermal`](https://github.com/nthmost/artery-thermal) · [`zoetrope69/now-playing-printer`](https://github.com/zoetrope69/now-playing-printer) · [`Tristan-Hotham/world-shipwrecks`](https://github.com/Tristan-Hotham/world-shipwrecks) · [`roman-dvorak/caelum`](https://github.com/roman-dvorak/caelum) · [`james-trayford/strauss`](https://github.com/james-trayford/strauss) · [`tyler-void/kinda-frame`](https://github.com/tyler-void/kinda-frame)

**Why it might matter:** A single simple interface for taking one odd event from a dataset and making it tangible: a meteor streak, a species detection, a wreck coordinate, a computed chemical result.

**Build-one-evening proof:** Implement a canonical Event schema with source/title/time/place/value/uncertainty and an HTML/SVG receipt renderer; add one data adapter.

**Unhinged extension:** A vending machine that dispenses slips of reality rather than products.

**Actual complications:** Different event sources need explicit time zones, units, privacy and permissions; paper and online previews first.

---

## 15. F-round: The Collision Engine

*The catalog becomes the instrument*

**Ingredients:** [`OpenRefine/OpenRefine`](https://github.com/OpenRefine/OpenRefine) · [`cosmosgl/graph`](https://github.com/cosmosgl/graph) · [`zakkariyaa/digital-garden`](https://github.com/zakkariyaa/digital-garden) · [`Timwi/EsotericIDE`](https://github.com/Timwi/EsotericIDE) · [`iclubu/Plotter-Studio`](https://github.com/iclubu/Plotter-Studio)

**Why it might matter:** A local research utility that rolls three distant repo 'parts', asks for one measurable bridge between them, and records evidence, licensing and build status.

**Build-one-evening proof:** A static page with 3 random cards from different categories, a reroll lock, an editable hypothesis and a saved Markdown idea. Entirely dependency-free at first.

**Unhinged extension:** Eventually the engine can run read-only capability probes, then automatically assemble reproducible prototypes in disposable containers.

**Actual complications:** This is a new idea inspired by research systems, not an existing integration. The Plotter-Studio link above should use iclubu/Plotter-Studio; do not assume cited software components integrate automatically.
