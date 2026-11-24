// shortFishLabel
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file frontend/modules/marine-map/web/index.js, line 532
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseStr = (value, fallback = '') => {
  if (typeof value === 'string') return value;
  if (value === null || value === undefined) return fallback;
  return String(value);
};


function shortFishLabel(commonName, sciName) {
  const sci = parseStr(sciName, '').toLowerCase();
  if (sci.includes('thunnus')) return 'Tuna';
  if (sci.includes('katsuwonus')) return 'Cakalang';
  if (sci.includes('euthynnus')) return 'Tongkol';
  if (sci.includes('rastrelliger')) return 'Kembung';
  if (sci.includes('decapterus')) return 'Layang';
  if (sci.includes('scomberomorus')) return 'Tenggiri';
  if (sci.includes('lutjanus')) return 'Kakap';
  if (sci.includes('epinephelus') || sci.includes('plectropomus')) return 'Kerapu';
  if (sci.includes('sardinella')) return 'Lemuru';
  if (sci.includes('coryphaena')) return 'Lemadang';
  if (sci.includes('cheilinus')) return 'Napoleon';
  if (sci.includes('penaeus')) return 'Udang';

  const raw = parseStr(commonName, '').trim();
  const parenMatch = raw.match(/\(([^)]+)\)/);
  let idPart = raw;
  if (raw.includes('/')) {
    idPart = raw.split('/').pop().trim();
  } else if (parenMatch) {
    idPart = parenMatch[1].trim();
  } else if (!raw) {
    idPart = parseStr(sciName, 'Ikan').trim();
  }
  const lower = idPart.toLowerCase();
  if (lower.includes('madidihang') || lower.includes('tuna')) return 'Tuna';
  if (lower.includes('kembung')) return 'Kembung';
  if (lower.includes('cakalang')) return 'Cakalang';
  if (lower.includes('tongkol') || lower.includes('bonito')) return 'Tongkol';
  if (lower.includes('layang')) return 'Layang';
  if (lower.includes('kakap')) return 'Kakap';
  if (lower.includes('kerapu') || lower.includes('grouper')) return 'Kerapu';
  if (lower.includes('lemuru') || lower.includes('sardinella')) return 'Lemuru';
  if (lower.includes('lemadang') || lower.includes('dolphin') || lower.includes('mahi')) return 'Lemadang';
  if (lower.includes('tenggiri')) return 'Tenggiri';
  if (lower.includes('udang') || lower.includes('prawn')) return 'Udang';
  if (lower.includes('napoleon')) return 'Napoleon';
  const cleaned = idPart.replace(/^ikan\s+/i, '').trim();
  if (!cleaned) return 'Ikan';
  const firstWord = cleaned.split(/\s+/)[0];
  return firstWord.charAt(0).toUpperCase() + firstWord.slice(1);
}
