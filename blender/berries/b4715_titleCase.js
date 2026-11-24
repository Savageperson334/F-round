// titleCase
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file tools/packs/build.mjs, line 110
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const UPPER = new Set(["sql", "api", "apis", "gke", "iam", "ai", "ml", "cdn", "dns", "nat", "vpn", "gpu", "tpu", "hsm", "ekm", "ids", "os", "vpc", "ssd", "vm", "id", "cx", "hub", "nlp", "ip", "gce", "kms", "iot", "sdk", "cli", "ui", "aws", "gcp", "hpc", "grpc", "dlp", "vmware", "secops", "secops"]);


const titleCase = (s) => s.split(/[_\s]+/).map((w) => w.split("-").map((p) => (UPPER.has(p) ? p.toUpperCase() : p === "pubsub" ? "Pub/Sub" : p === "bigquery" ? "BigQuery" : p === "bigtable" ? "Bigtable" : p === "vmware" ? "VMware" : p.charAt(0).toUpperCase() + p.slice(1))).join("-")).join(" ");
