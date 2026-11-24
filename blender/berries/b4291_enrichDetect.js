// enrichDetect
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-remaining-narrative.mjs, line 19
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DETECT_RE =
  /\b(?:Event(?:\s*ID)?\s*\d+|EID\s*\d+|Sysmon|auditd|CloudTrail|Suricata|Security Event|Bits-Client|Okta|Azure AD|Windows Security|cwpsrv|Sigma|journalctl|kube-apiserver|Zeek|EDR|pcap|W3SVC|IIS|Tomcat|nginx|httpd|mcpd|tmsh|access[_-]?log|auth\.log|syslog)\b|\/var\/log/i;


function enrichDetect(text, mitre) {
  let t = String(text || '').replace(/\s+/g, ' ').trim();
  if (!DETECT_RE.test(t)) {
    t = `${t.replace(/\.\s*$/, '')}. Correlate Sysmon Event 1 and Windows Security Event telemetry for ${mitre} (pairing parent/child process and destination fields) and contain the offending session.`;
  }
  while (t.length < 160) {
    t +=
      ' Preserve the raw event fields with the containment ticket for forensic replay.';
  }
  return t;
}
