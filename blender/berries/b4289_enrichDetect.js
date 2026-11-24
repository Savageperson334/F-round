// enrichDetect
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 82
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DETECT_RE =
  /\b(?:Event(?:\s*ID)?\s*\d+|EID\s*\d+|Sysmon|auditd|CloudTrail|Suricata|Security Event|Bits-Client|Okta|Azure AD|Windows Security|cwpsrv|Sigma|journalctl|kube-apiserver|Zeek|EDR|pcap|W3SVC|IIS|Tomcat|nginx|httpd|mcpd|tmsh|access[_-]?log|auth\.log|syslog)\b|\/var\/log/i;


function strip(s) {
  return String(s || '')
    .replace(/—/g, '-')
    .replace(/\s+/g, ' ')
    .trim();
}


function enrichDetect(text, stage, mitre, stepNumber) {
  let t = strip(text);
  const log = stage?.logs?.[0];
  const hasSource = DETECT_RE.test(t);
  if (t.length >= 160 && hasSource) return t;

  if (log?.source && log?.EventCode != null) {
    t = `${t.replace(/\.\s*$/, '')}. Correlate ${strip(String(log.source))} Event ${
      log.EventCode
    } (the log record that proves this ${mitre} action occurred) and isolate the offending process before the next stage.`;
  } else if (log?.source) {
    t = `${t.replace(/\.\s*$/, '')}. Correlate ${strip(String(log.source))} telemetry (pairing process, auth, or network fields for ${mitre}) and contain the session before Stage ${
      (stage?.index ?? stepNumber) + 1
    }.`;
  } else if (!hasSource) {
    t = `${t.replace(/\.\s*$/, '')}. Correlate Sysmon or Windows Security Event telemetry for ${mitre} (pairing parent/child process and destination fields) and contain the offending session.`;
  }
  while (t.length < 160) {
    t +=
      ' Preserve the raw event fields and the related containment ticket for forensic replay.';
  }
  return strip(t);
}
