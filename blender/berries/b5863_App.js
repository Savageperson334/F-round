// App
//
// Copied verbatim from https://github.com/rewonc/pastalog
//   file src/components/App.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const App = (child) =>
  `<!DOCTYPE html>
  <html>
    <head>
      <title>pastalog ~~~~~~~</title>
      <script src='app.js' defer></script>
    </head>
    <body>
      <div id="container" class="max">${child}</div>
    </body>
  </html>`;
