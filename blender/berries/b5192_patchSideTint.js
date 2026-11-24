// patchSideTint
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/patch-maplibre-terrain-clip.mjs, line 1078
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CLIP_FRAG_PREFIX_OLD =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;in float v_drop;in float v_skirt;';

const CLIP_FRAG_PREFIX =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform highp float u_clip_drop;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;in float v_drop;in highp float v_drop_w;in highp float v_clip_w;in float v_skirt;';

const CLIP_FRAG_PREFIX_MED =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform float u_clip_drop;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;in float v_drop;in float v_skirt;';

const CLIP_FRAG_PREFIX_NOPERSP =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform highp float u_clip_drop;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;noperspective in float v_drop;in float v_skirt;';

const CLIP_FRAG_PREFIX_PERSP =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform highp float u_clip_drop;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;in float v_drop;in float v_skirt;';

const CLIP_FRAG_PREFIX_DROP_W =
  'uniform sampler2D u_clip;uniform highp float u_clip_enabled;uniform highp vec2 u_clip_origin;uniform highp vec2 u_clip_size;uniform highp float u_clip_drop;uniform vec4 u_clip_side_color;in highp vec2 v_mercator;in float v_clip;in float v_drop;in float v_drop_w;in float v_skirt;';

const CLIP_SIDE_TINT_OLD =
  'if(u_clip_enabled>0.5&&v_clip<0.999){surface_color=mix(u_clip_side_color,surface_color,smoothstep(0.72,1.0,v_clip));}';

const CLIP_SIDE_TINT_SHADE01 =
  'if(wall){float uv=clamp(drop,0.0,1.0);vec2 e=max(fwidth(cuf),vec2(1.0e-5));vec2 gr=vec2(texture(u_clip,clamp(cuf+vec2(e.x,0.0),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(e.x,0.0),0.0,1.0)).r,texture(u_clip,clamp(cuf+vec2(0.0,e.y),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(0.0,e.y),0.0,1.0)).r);float g2=dot(gr,gr);vec2 od=g2>1.0e-12?-gr*inversesqrt(g2):vec2(0.0);float water=texture(u_clip,clamp(cuf+od*max(e,vec2(1.0e-4))*3.0,0.0,1.0)).g;float n=fract(sin(dot(cuf,vec2(127.1,311.7)))*43758.5453);uv=clamp(uv+0.044*(cuf.x+cuf.y*0.35-0.7)+0.02*(n-0.5),0.0,1.0);vec3 rock=vec3(58.0,46.0,36.0)/255.0;vec3 c;float b0;float b1;if(water>0.5){b0=0.15;b1=0.40;c=uv<b0?vec3(61.0,83.0,72.0)/255.0:uv<b1?vec3(166.0,124.0,82.0)/255.0:rock;}else{b0=0.10;b1=0.30;c=uv<b0?vec3(196.0,160.0,106.0)/255.0:uv<b1?vec3(139.0,115.0,85.0)/255.0:rock;}float fw=max(fwidth(uv),1.0e-6);float line=max(1.0-smoothstep(0.0,fw,abs(uv-b0)),1.0-smoothstep(0.0,fw,abs(uv-b1)));c=mix(c,vec3(26.0,20.0,16.0)/255.0,line);surface_color=vec4(c,1.0);}';

const CLIP_SIDE_TINT = CLIP_SIDE_TINT_SHADE01;

const CLIP_SIDE_TINT_SHADE =
  'if(wall){float shade=mix(1.0,0.30,clamp(max(v_drop,1.0)/2800.0,0.0,1.0));surface_color=vec4(u_clip_side_color.rgb*shade,u_clip_side_color.a);}';

const CLIP_SIDE_TINT_FW =
  'if(wall){float shade=mix(1.0,0.30,clamp(v_drop/2800.0,0.0,1.0));surface_color=vec4(u_clip_side_color.rgb*shade,u_clip_side_color.a);}';

const CLIP_SIDE_TINT_DROP =
  'if(u_clip_enabled>0.5&&v_drop>0.5){float shade=mix(1.0,0.30,clamp(v_drop/2800.0,0.0,1.0));surface_color=vec4(u_clip_side_color.rgb*shade,u_clip_side_color.a);}';

const CLIP_SIDE_TINT_GEOM =
  'if(wall){float uv=clamp(drop/max(u_clip_drop,1.0),0.0,1.0);vec2 e=max(fwidth(cuf),vec2(1.0e-5));vec2 gr=vec2(texture(u_clip,clamp(cuf+vec2(e.x,0.0),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(e.x,0.0),0.0,1.0)).r,texture(u_clip,clamp(cuf+vec2(0.0,e.y),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(0.0,e.y),0.0,1.0)).r);float g2=dot(gr,gr);vec2 od=g2>1.0e-12?-gr*inversesqrt(g2):vec2(0.0);float water=texture(u_clip,clamp(cuf+od*max(e,vec2(1.0e-4))*3.0,0.0,1.0)).g;float n=fract(sin(dot(cuf,vec2(127.1,311.7)))*43758.5453);uv=clamp(uv+0.044*(cuf.x+cuf.y*0.35-0.7)+0.02*(n-0.5),0.0,1.0);vec3 rock=vec3(58.0,46.0,36.0)/255.0;vec3 c;float b0;float b1;if(water>0.5){b0=0.15;b1=0.40;c=uv<b0?vec3(61.0,83.0,72.0)/255.0:uv<b1?vec3(166.0,124.0,82.0)/255.0:rock;}else{b0=0.10;b1=0.30;c=uv<b0?vec3(196.0,160.0,106.0)/255.0:uv<b1?vec3(139.0,115.0,85.0)/255.0:rock;}float fw=max(fwidth(uv),1.0e-6);float line=max(1.0-smoothstep(0.0,fw,abs(uv-b0)),1.0-smoothstep(0.0,fw,abs(uv-b1)));c=mix(c,vec3(26.0,20.0,16.0)/255.0,line);surface_color=vec4(c,1.0);}';

const CLIP_SIDE_TINT_DFy_INWALL =
  'if(wall){float uv=clamp(drop/max(u_clip_drop,1.0),0.0,1.0);float dy=dFdy(uv);float uvb=clamp(uv-dy*gl_FragCoord.y,max(uv,1.0e-4),1.0);uv=clamp(uv/uvb,0.0,1.0);vec2 e=max(fwidth(cuf),vec2(1.0e-5));vec2 gr=vec2(texture(u_clip,clamp(cuf+vec2(e.x,0.0),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(e.x,0.0),0.0,1.0)).r,texture(u_clip,clamp(cuf+vec2(0.0,e.y),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(0.0,e.y),0.0,1.0)).r);float g2=dot(gr,gr);vec2 od=g2>1.0e-12?-gr*inversesqrt(g2):vec2(0.0);float water=texture(u_clip,clamp(cuf+od*max(e,vec2(1.0e-4))*3.0,0.0,1.0)).g;float n=fract(sin(dot(cuf,vec2(127.1,311.7)))*43758.5453);uv=clamp(uv+0.044*(cuf.x+cuf.y*0.35-0.7)+0.02*(n-0.5),0.0,1.0);vec3 rock=vec3(58.0,46.0,36.0)/255.0;vec3 c;float b0;float b1;if(water>0.5){b0=0.15;b1=0.40;c=uv<b0?vec3(61.0,83.0,72.0)/255.0:uv<b1?vec3(166.0,124.0,82.0)/255.0:rock;}else{b0=0.10;b1=0.30;c=uv<b0?vec3(196.0,160.0,106.0)/255.0:uv<b1?vec3(139.0,115.0,85.0)/255.0:rock;}float fw=max(fwidth(uv),1.0e-6);float line=max(1.0-smoothstep(0.0,fw,abs(uv-b0)),1.0-smoothstep(0.0,fw,abs(uv-b1)));c=mix(c,vec3(26.0,20.0,16.0)/255.0,line);surface_color=vec4(c,1.0);}';

const CLIP_SIDE_TINT_X4 =
  'if(wall){float uv=clamp(drop/max(u_clip_drop,1.0),0.0,1.0);uv=clamp(uv*4.0,0.0,1.0);vec2 e=max(fwidth(cuf),vec2(1.0e-5));vec2 gr=vec2(texture(u_clip,clamp(cuf+vec2(e.x,0.0),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(e.x,0.0),0.0,1.0)).r,texture(u_clip,clamp(cuf+vec2(0.0,e.y),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(0.0,e.y),0.0,1.0)).r);float g2=dot(gr,gr);vec2 od=g2>1.0e-12?-gr*inversesqrt(g2):vec2(0.0);float water=texture(u_clip,clamp(cuf+od*max(e,vec2(1.0e-4))*3.0,0.0,1.0)).g;float n=fract(sin(dot(cuf,vec2(127.1,311.7)))*43758.5453);uv=clamp(uv+0.044*(cuf.x+cuf.y*0.35-0.7)+0.02*(n-0.5),0.0,1.0);vec3 rock=vec3(58.0,46.0,36.0)/255.0;vec3 c;float b0;float b1;if(water>0.5){b0=0.15;b1=0.40;c=uv<b0?vec3(61.0,83.0,72.0)/255.0:uv<b1?vec3(166.0,124.0,82.0)/255.0:rock;}else{b0=0.10;b1=0.30;c=uv<b0?vec3(196.0,160.0,106.0)/255.0:uv<b1?vec3(139.0,115.0,85.0)/255.0:rock;}float fw=max(fwidth(uv),1.0e-6);float line=max(1.0-smoothstep(0.0,fw,abs(uv-b0)),1.0-smoothstep(0.0,fw,abs(uv-b1)));c=mix(c,vec3(26.0,20.0,16.0)/255.0,line);surface_color=vec4(c,1.0);}';

const CLIP_DISCARD_SKIRT_WALL =
  'float dg=fwidth(v_drop);vec2 cuf=(v_mercator-u_clip_origin)/max(u_clip_size,vec2(1.0e-12));bool outside=u_clip_enabled>0.5&&(cuf.x<0.0||cuf.y<0.0||cuf.x>1.0||cuf.y>1.0||texture(u_clip,cuf).r<0.5);bool mixed=dg>0.05;if(outside&&!mixed)discard;float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>0.004;';

const CLIP_DISCARD = CLIP_DISCARD_SKIRT_WALL;

const CLIP_DISCARD_SKIRT_WALL_V1 =
  'float dg=fwidth(v_drop);vec2 cuf=(v_mercator-u_clip_origin)/max(u_clip_size,vec2(1.0e-12));bool outside=u_clip_enabled>0.5&&(cuf.x<0.0||cuf.y<0.0||cuf.x>1.0||cuf.y>1.0||texture(u_clip,cuf).r<0.5);bool mixed=dg>0.05;if(outside&&!mixed)discard;bool wall=u_clip_enabled>0.5&&mixed&&v_drop>80.0;';

const CLIP_DISCARD_SKIRT_WALL_FC =
  'float dg=fwidth(v_drop);vec2 cuf=(v_mercator-u_clip_origin)/max(u_clip_size,vec2(1.0e-12));bool outside=u_clip_enabled>0.5&&(cuf.x<0.0||cuf.y<0.0||cuf.x>1.0||cuf.y>1.0||texture(u_clip,cuf).r<0.5);bool mixed=dg>0.05;if(outside&&!mixed)discard;float drop=v_drop_w*gl_FragCoord.w;bool wall=u_clip_enabled>0.5&&drop>80.0;';

const CLIP_DISCARD_SKIRT_WALL_METERS =
  'float dg=fwidth(v_drop);vec2 cuf=(v_mercator-u_clip_origin)/max(u_clip_size,vec2(1.0e-12));bool outside=u_clip_enabled>0.5&&(cuf.x<0.0||cuf.y<0.0||cuf.x>1.0||cuf.y>1.0||texture(u_clip,cuf).r<0.5);bool mixed=dg>0.05;if(outside&&!mixed)discard;float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>80.0;';

const CLIP_DISCARD_SKIRT_WALL_FWIDTH =
  'float dg=fwidth(v_drop);vec2 cuf=(v_mercator-u_clip_origin)/max(u_clip_size,vec2(1.0e-12));bool outside=u_clip_enabled>0.5&&(cuf.x<0.0||cuf.y<0.0||cuf.x>1.0||cuf.y>1.0||texture(u_clip,cuf).r<0.5);bool mixed=dg>0.05;if(outside&&!mixed)discard;float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>0.004;';

const CLIP_SIDE_TINT_V1 =
  'if(wall){float uv=clamp(v_drop/max(u_clip_drop,1.0),0.0,1.0);vec2 e=max(fwidth(cuf),vec2(1.0e-5));vec2 gr=vec2(texture(u_clip,clamp(cuf+vec2(e.x,0.0),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(e.x,0.0),0.0,1.0)).r,texture(u_clip,clamp(cuf+vec2(0.0,e.y),0.0,1.0)).r-texture(u_clip,clamp(cuf-vec2(0.0,e.y),0.0,1.0)).r);float g2=dot(gr,gr);vec2 od=g2>1.0e-12?-gr*inversesqrt(g2):vec2(0.0);float water=texture(u_clip,clamp(cuf+od*max(e,vec2(1.0e-4))*3.0,0.0,1.0)).g;float n=fract(sin(dot(cuf,vec2(127.1,311.7)))*43758.5453);uv=clamp(uv+0.044*(cuf.x+cuf.y*0.35-0.7)+0.02*(n-0.5),0.0,1.0);vec3 rock=vec3(58.0,46.0,36.0)/255.0;vec3 c;float b0;float b1;if(water>0.5){b0=0.15;b1=0.40;c=uv<b0?vec3(61.0,83.0,72.0)/255.0:uv<b1?vec3(166.0,124.0,82.0)/255.0:rock;}else{b0=0.10;b1=0.30;c=uv<b0?vec3(196.0,160.0,106.0)/255.0:uv<b1?vec3(139.0,115.0,85.0)/255.0:rock;}float fw=max(fwidth(uv),1.0e-6);float line=max(1.0-smoothstep(0.0,fw,abs(uv-b0)),1.0-smoothstep(0.0,fw,abs(uv-b1)));c=mix(c,vec3(26.0,20.0,16.0)/255.0,line);surface_color=vec4(c,1.0);}';

const FOG_IF =
  'if (!u_is_globe_mode && v_fog_depth > u_fog_ground_blend)';

const FOG_IF_SKIP_WALL =
  'if (!wall&&!u_is_globe_mode && v_fog_depth > u_fog_ground_blend)';


function qualifyWallStrata(s) {
  if (s.includes(CLIP_FRAG_PREFIX_NOPERSP)) {
    s = s.split(CLIP_FRAG_PREFIX_NOPERSP).join(CLIP_FRAG_PREFIX);
  }
  if (s.includes(CLIP_FRAG_PREFIX_PERSP) && !s.includes('v_drop_w')) {
    s = s.split(CLIP_FRAG_PREFIX_PERSP).join(CLIP_FRAG_PREFIX);
  }
  if (s.includes(CLIP_FRAG_PREFIX_DROP_W)) {
    s = s.split(CLIP_FRAG_PREFIX_DROP_W).join(CLIP_FRAG_PREFIX);
  }
  s = s.split('noperspective out float v_drop;').join(
    'out float v_drop;out highp float v_drop_w;out highp float v_clip_w;'
  );
  s = s.split('noperspective in float v_drop;').join(
    'in float v_drop;in highp float v_drop_w;in highp float v_clip_w;'
  );
  s = s.split('out float v_drop;out float v_drop_w;out float v_clip_w;').join(
    'out float v_drop;out highp float v_drop_w;out highp float v_clip_w;'
  );
  s = s.split('in float v_drop;in float v_drop_w;in float v_clip_w;').join(
    'in float v_drop;in highp float v_drop_w;in highp float v_clip_w;'
  );
  if (!s.includes('v_clip_w')) {
    s = s.split('out float v_drop;out float v_drop_w;out float v_skirt;').join(
      'out float v_drop;out highp float v_drop_w;out highp float v_clip_w;out float v_skirt;'
    );
  }
  if (!s.includes('v_clip_w')) {
    s = s.split('in float v_drop;in float v_drop_w;in float v_skirt;').join(
      'in float v_drop;in highp float v_drop_w;in highp float v_clip_w;in float v_skirt;'
    );
  }
  if (!s.includes('v_drop_w')) {
    s = s.split('out float v_drop;out float v_skirt;').join(
      'out float v_drop;out highp float v_drop_w;out highp float v_clip_w;out float v_skirt;'
    );
  }
  if (!s.includes('v_drop_w')) {
    s = s.split('in float v_drop;in float v_skirt;').join(
      'in float v_drop;in highp float v_drop_w;in highp float v_clip_w;in float v_skirt;'
    );
  }
  const gp = 'gl_Position=projectTileFor3D(p2,get_elevation(p2)-ele_delta);';
  const gpW =
    'gl_Position=projectTileFor3D(p2,get_elevation(p2)-ele_delta);v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w;v_clip_w=gl_Position.w;';
  if (s.includes(gp) && !s.includes('v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w')) {
    s = s.split(gp).join(gpW);
  }
  s = s.split('v_drop_w=v_drop*gl_Position.w;').join(
    'v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w;'
  );
  if (s.includes('v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w;') && !s.includes('v_clip_w=gl_Position.w')) {
    s = s.split('v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w;').join(
      'v_drop_w=(v_drop>80.0?1.0:0.0)*gl_Position.w;v_clip_w=gl_Position.w;'
    );
  }
  if (s.includes(CLIP_DISCARD_SKIRT_WALL_V1)) {
    s = s.split(CLIP_DISCARD_SKIRT_WALL_V1).join(CLIP_DISCARD_SKIRT_WALL);
  }
  if (s.includes(CLIP_DISCARD_SKIRT_WALL_FC)) {
    s = s.split(CLIP_DISCARD_SKIRT_WALL_FC).join(CLIP_DISCARD_SKIRT_WALL);
  }
  if (s.includes(CLIP_DISCARD_SKIRT_WALL_METERS)) {
    s = s.split(CLIP_DISCARD_SKIRT_WALL_METERS).join(CLIP_DISCARD_SKIRT_WALL);
  }
  if (s.includes(CLIP_DISCARD_SKIRT_WALL_FWIDTH)) {
    s = s.split(CLIP_DISCARD_SKIRT_WALL_FWIDTH).join(CLIP_DISCARD_SKIRT_WALL);
  }
  s = s.split('bool wall=u_clip_enabled>0.5&&drop>80.0').join(
    'bool wall=u_clip_enabled>0.5&&drop>0.004'
  );
  if (!s.includes('float dyDrop=dFdy(drop)')) {
    s = s.split(
      'float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>0.004;'
    ).join(
      'float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>0.004;float dyDrop=dFdy(drop);'
    );
  }
  s = s.split('float drop=v_drop_w*gl_FragCoord.w;').join(
    'float drop=v_drop_w/max(v_clip_w,1.0e-12);'
  );
  s = s.split('bool wall=u_clip_enabled>0.5&&mixed&&v_drop>80.0;').join(
    'float drop=v_drop_w/max(v_clip_w,1.0e-12);bool wall=u_clip_enabled>0.5&&drop>0.004;'
  );
  if (s.includes(CLIP_SIDE_TINT_V1) && CLIP_SIDE_TINT_V1 !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_V1).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_GEOM) && CLIP_SIDE_TINT_GEOM !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_GEOM).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_DFy_INWALL) && CLIP_SIDE_TINT_DFy_INWALL !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_DFy_INWALL).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_X4) && CLIP_SIDE_TINT_X4 !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_X4).join(CLIP_SIDE_TINT);
  }
  s = s.split('uv=clamp(uv*4.0,0.0,1.0);').join('');
  s = s.split(
    'float dy=dFdy(uv);float uvb=clamp(uv-dy*gl_FragCoord.y,max(uv,1.0e-4),1.0);uv=clamp(uv/uvb,0.0,1.0);'
  ).join('');
  s = s.split(
    'float dy=dyDrop/max(u_clip_drop,1.0);float uvb=clamp(uv-dy*gl_FragCoord.y,max(uv,1.0e-4),1.0);uv=clamp(uv/uvb,0.0,1.0);'
  ).join('');
  if (s.includes('float dyDrop=dFdy(drop);')) {
    s = s.split('float dyDrop=dFdy(drop);').join('');
  }
  s = s.split('if(wall){float uv=clamp(v_drop/max(u_clip_drop,1.0),0.0,1.0)').join(
    'if(wall){float uv=clamp(drop,0.0,1.0)'
  );
  s = s.split('if(wall){float uv=clamp(drop/max(u_clip_drop,1.0),0.0,1.0)').join(
    'if(wall){float uv=clamp(drop,0.0,1.0)'
  );
  if (s.includes(FOG_IF) && !s.includes(FOG_IF_SKIP_WALL)) {
    s = s.split(FOG_IF).join(FOG_IF_SKIP_WALL);
  }
  return s;
}


function patchSideTint(s) {
  if (s.includes(CLIP_FRAG_PREFIX_OLD)) s = s.split(CLIP_FRAG_PREFIX_OLD).join(CLIP_FRAG_PREFIX);
  if (s.includes(CLIP_FRAG_PREFIX_MED)) s = s.split(CLIP_FRAG_PREFIX_MED).join(CLIP_FRAG_PREFIX);
  if (s.includes(CLIP_FRAG_PREFIX_NOPERSP)) s = s.split(CLIP_FRAG_PREFIX_NOPERSP).join(CLIP_FRAG_PREFIX);
  if (s.includes(CLIP_FRAG_PREFIX_PERSP) && !s.includes('v_drop_w')) {
    s = s.split(CLIP_FRAG_PREFIX_PERSP).join(CLIP_FRAG_PREFIX);
  }
  if (s.includes(CLIP_FRAG_PREFIX_DROP_W)) {
    s = s.split(CLIP_FRAG_PREFIX_DROP_W).join(CLIP_FRAG_PREFIX);
  }
  s = s.split('uniform float u_clip_drop;').join('uniform highp float u_clip_drop;');
  if (s.includes(CLIP_SIDE_TINT_OLD)) s = s.split(CLIP_SIDE_TINT_OLD).join(CLIP_SIDE_TINT);
  if (s.includes(CLIP_SIDE_TINT_SHADE) && CLIP_SIDE_TINT_SHADE !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_SHADE).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_FW) && CLIP_SIDE_TINT_FW !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_FW).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_DROP) && !s.includes('if(wall){float uv=clamp(drop')) {
    s = s.split(CLIP_SIDE_TINT_DROP).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_GEOM) && CLIP_SIDE_TINT_GEOM !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_GEOM).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_DFy_INWALL) && CLIP_SIDE_TINT_DFy_INWALL !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_DFy_INWALL).join(CLIP_SIDE_TINT);
  }
  if (s.includes(CLIP_SIDE_TINT_X4) && CLIP_SIDE_TINT_X4 !== CLIP_SIDE_TINT) {
    s = s.split(CLIP_SIDE_TINT_X4).join(CLIP_SIDE_TINT);
  }
  s = s.split('uv=clamp(uv*4.0,0.0,1.0);').join('');
  s = s.split(
    'float dy=dyDrop/max(u_clip_drop,1.0);float uvb=clamp(uv-dy*gl_FragCoord.y,max(uv,1.0e-4),1.0);uv=clamp(uv/uvb,0.0,1.0);'
  ).join('');
  s = s.split('in float v_clip;uniform vec4 u_clip_side_color;in float v_drop;').join(
    'in float v_clip;in float v_drop;'
  );
  const needleRaw =
    CLIP_DISCARD +
    'vec4 surface_color=texture(u_texture,vec2(v_texture_pos.x,1.0-v_texture_pos.y));';
  const needleClamp =
    CLIP_DISCARD +
    'vec4 surface_color=texture(u_texture,clamp(vec2(v_texture_pos.x,1.0-v_texture_pos.y),vec2(0.002),vec2(0.998)));';
  if (!s.includes(CLIP_SIDE_TINT)) {
    if (s.includes(needleClamp)) s = s.split(needleClamp).join(needleClamp + CLIP_SIDE_TINT);
    else if (s.includes(needleRaw)) s = s.split(needleRaw).join(needleRaw + CLIP_SIDE_TINT);
  }
  if (!s.includes("'u_clip_side_color':")) {
    s = s.split(
      "'u_clip_drop': new performance$1.Uniform1f(context, locations.u_clip_drop),"
    ).join(
      "'u_clip_drop': new performance$1.Uniform1f(context, locations.u_clip_drop),\n    'u_clip_side_color': new performance$1.Uniform4f(context, locations.u_clip_side_color),"
    );
    s = s.split("'u_clip_drop': 12000,").join(
      "'u_clip_drop': 12000,\n    'u_clip_side_color': [0.427, 0.29, 0.212, 1],"
    );
  }
  if (!s.includes('uniformValues.u_clip_side_color')) {
    s = s.split(
      'uniformValues.u_clip_drop = clip && clip.drop > 0 ? clip.drop : 12000;'
    ).join(
      'uniformValues.u_clip_drop = clip && clip.drop > 0 ? clip.drop : 12000;\n    uniformValues.u_clip_side_color = clip && clip.sideColor ? clip.sideColor : [0.427, 0.29, 0.212, 1];'
    );
  }
  return qualifyWallStrata(s);
}
