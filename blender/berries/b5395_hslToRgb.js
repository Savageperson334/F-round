// hslToRgb
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/colormanip.js, line 22
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hslToRgb(h, s, l) {
  var r, g, b;

  var myVersion=true;

  if(myVersion){

    h=(h-Math.floor(h)); // make it periodic 1; works for negative input

    var r_smax=Math.max(0, 1-6*Math.pow(h,2), 1-9*Math.pow(h-1,2));
    var g_smax=Math.max(0, 1-9*Math.pow(h-1/3,2));
    var b_smax=Math.max(0, 1-9*Math.pow(h-2/3,2));


    r = Math.min(255,Math.round(255*3.0*l*(0.5+s*(r_smax-0.5))));
    g = Math.min(255,Math.round(255*2.2*l*(0.5+s*(g_smax-0.5))));
    b = Math.min(255,Math.round(255*1.6*l*(0.5+s*(b_smax-0.5))));

  }

  else{ // not mt version

    if(s === 0){
        r = g = b = l; // achromatic
    }else{
        function hue2rgb(p, q, t){
            if(t < 0) t += 1;
            if(t > 1) t -= 1;
            if(t < 1/6) return p + (q - p) * 6 * t;
            if(t < 1/2) return q;
            if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = Math.round(255*hue2rgb(p, q, h + 1/3));
        g = Math.round(255*hue2rgb(p, q, h));
        b = Math.round(255*hue2rgb(p, q, h - 1/3));
    }
  }
  return [r, g, b];

}
