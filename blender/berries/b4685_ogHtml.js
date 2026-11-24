// ogHtml
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file media/brand/render.js, line 27
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function ogHtml(icon) {
  return `<html><body style="margin:0;width:1200px;height:630px;display:flex;align-items:center;gap:64px;padding:0 96px;box-sizing:border-box;
  background:radial-gradient(900px 480px at 50% -120px, rgba(26,124,255,0.28), transparent 70%), #0b0d12;color:#f4f6fb;
  font-family:'Segoe UI','Inter',system-ui,sans-serif">
  ${icon.replace("<svg ", '<svg width="240" height="240" style="flex:none;filter:drop-shadow(0 18px 40px rgba(0,82,214,0.35))" ')}
  <div>
    <div style="font-size:30px;font-weight:600;color:#9aa3b5;letter-spacing:-0.01em">Shipwreck for VS Code</div>
    <div style="margin-top:14px;font-size:66px;line-height:1.05;font-weight:800;letter-spacing:-0.035em">Run any ACP coding agent inside VS Code</div>
    <div style="margin-top:22px;font-size:26px;color:#9aa3b5">shipwreck.yaseen.zip</div>
  </div>
</body></html>`;
}
