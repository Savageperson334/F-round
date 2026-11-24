// eraseOutcome
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/installer_state.js, line 31
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ERASE = {
  label: "Erase my saved data after installing (start from scratch)",
  help: "Erases your settings (theme, scale, MIDI channels, favourites), the autosave, your patches, your multis and your patterns. " +
        "The factory sounds, multis and patterns come back. This cannot be undone: back up first. " +
        "Left off, your saved data stays and the unit comes back as you left it.",
  status: "Erasing your data ...",
  done: "Done. Your saved data was erased. The unit starts as new.",
  lockNote: "Locked: the install is running.",
};


function eraseOutcome(rc, err = null) {
  if (rc === 0) return { erased: true, bad: false, text: ERASE.done };
  const why = rc === 3 ? "The unit was playing." : rc === 1 ? "The unit refused the request." : rc === 4 ? "The unit could not write its memory." :
    err ? "The unit could not be reached." : "The unit did not confirm.";
  return { erased: false, bad: true,
    text: `The install itself succeeded, but your saved data was NOT erased (${why}) and is still on the unit. ` +
          "To start from scratch, use MENU > SYSTEM > ERASE DATA on the unit." };
}
