// Figma Plugin — Cria a capa completa de "Liderando na Era dos Agentes"
// Como usar:
// 1. Figma → Menu → Plugins → Development → New Plugin
// 2. Cole este código no editor
// 3. Clique "Run"

// ── Cores ──
const PAPEL    = {r:0.980, g:0.969, b:0.949};  // #FAF7F2
const CONCRETO = {r:0.176, g:0.165, b:0.149};  // #2D2A26
const ARGILA   = {r:0.769, g:0.271, b:0.212};  // #C44536
const BRANCO   = {r:1, g:1, b:1};
const CINZA    = {r:0.353, g:0.337, b:0.322};  // #5A5652

// ── Fontes ──
const FONT = {family:"DM Sans", style:"Regular"};
const FONT_BOLD = {family:"DM Sans", style:"Bold"};
const FONT_BLACK = {family:"DM Sans", style:"Black"};

// ── Helpers ──
function createFrame(name, x, y, w, h, color) {
  const f = figma.createFrame();
  f.name = name; f.x = x; f.y = y;
  f.resize(w, h); f.fills = [{type:'SOLID', color}];
  f.clipsContent = true;
  return f;
}

function createRect(parent, name, x, y, w, h, color) {
  const r = figma.createRectangle();
  r.name = name; r.x = x; r.y = y;
  r.resize(w, h); r.fills = [{type:'SOLID', color}];
  parent.appendChild(r);
  return r;
}

function createText(parent, name, x, y, w, content, fontSize, font, color, opts={}) {
  const t = figma.createText();
  t.name = name; t.x = x; t.y = y;
  t.resize(w, fontSize * 1.5);
  t.fontName = font;
  t.fontSize = fontSize;
  t.fills = [{type:'SOLID', color}];
  t.characters = content;
  if (opts.letterSpacing) t.letterSpacing = {value:opts.letterSpacing, unit:'PERCENT'};
  if (opts.lineHeight) t.lineHeight = {value:opts.lineHeight, unit:'PERCENT'};
  if (opts.textCase) t.textCase = opts.textCase;
  if (opts.textAlign) t.textAlignHorizontal = opts.textAlign;
  parent.appendChild(t);
  return t;
}

function createCircle(parent, name, x, y, size, strokeColor, strokeWidth) {
  const c = figma.createEllipse();
  c.name = name; c.x = x; c.y = y;
  c.resize(size, size);
  c.fills = [];
  c.strokes = [{type:'SOLID', color:strokeColor}];
  c.strokeWeight = strokeWidth;
  parent.appendChild(c);
  return c;
}

function createLine(parent, name, x, y, w, color) {
  const l = figma.createRectangle();
  l.name = name; l.x = x; l.y = y;
  l.resize(w, 3); l.fills = [{type:'SOLID', color}];
  parent.appendChild(l);
  return l;
}

// ═══════════════════════════════════════════
// MAIN
// ═══════════════════════════════════════════

const page = figma.currentPage;
page.name = "📘 Capa — Liderando na Era dos Agentes";

// ── FRENTE ──
const frente = createFrame("Frente", 0, 0, 420, 600, PAPEL);

// Geo block escuro
const geo = createRect(frente, "Geo Block", 0, 0, 420, 348, CONCRETO);
// Aplicar clip-path via vector
const clipVector = figma.createVector();
clipVector.vectorPaths = [{
  windingRule: "EVENODD",
  data: "M 0 0 L 420 0 L 420 285 L 0 348 Z"
}];
clipVector.fills = [{type:'SOLID', color:CONCRETO}];
clipVector.x = 0; clipVector.y = 0;
clipVector.resize(420, 348);
frente.insertChild(0, clipVector);

// Linha vermelha
createLine(frente, "Red Line", 0, 327, 420, ARGILA);

// Círculos
createCircle(frente, "Circle 1", 288, 56, 100, {r:1,g:1,b:1}, 1.5).opacity = 0.1;
createCircle(frente, "Circle 2", 318, 100, 40, {r:1,g:1,b:1}, 1).opacity = 0.08;

// Label
createText(frente, "Label", 36, 42, 200, "PRODUTO · LIDERANÇA · IA", 9, FONT_BOLD, {r:1,g:1,b:1, a:0.45}, {letterSpacing:40, textCase:'UPPER'});

// Título
createText(frente, "Title L1", 36, 90, 348, "Liderando", 52, FONT_BLACK, BRANCO, {lineHeight:100, letterSpacing:-3});
createText(frente, "Title L2", 36, 140, 348, "na Era dos", 52, FONT_BLACK, BRANCO, {lineHeight:100, letterSpacing:-3});
createText(frente, "Title L3", 36, 190, 348, "Agentes", 52, FONT_BLACK, BRANCO, {lineHeight:100, letterSpacing:-3});

// Subtítulo
createText(frente, "Subtitle", 36, 410, 280, "O manual de liderança de produto para a era da IA — por quem opera a transformação", 14, FONT, CINZA, {lineHeight:150});

// Author line + name
createLine(frente, "Author Line", 36, 545, 28, ARGILA);
createText(frente, "Author Name", 74, 535, 200, "FERNANDA FARIA", 11, FONT_BOLD, CONCRETO, {letterSpacing:25, textCase:'UPPER'});

// ── LOMBADA ──
const lombada = createFrame("Lombada", 420, 0, 32, 600, CONCRETO);

createCircle(lombada, "Dot Top", 14, 52, 4, ARGILA, 0);
createCircle(lombada, "Dot Bottom", 14, 544, 4, ARGILA, 0);

const spineTitle = createText(lombada, "Spine Title", 8, 80, 16, "Liderando na Era dos Agentes", 13, FONT_BOLD, BRANCO, {letterSpacing:8});
spineTitle.rotation = 90; // Vertical text simulation
// Figma text doesn't rotate easily — we'll use vertical writing mode
const spineAuthor = createText(lombada, "Spine Author", 8, 520, 16, "FERNANDA FARIA", 9, FONT, {r:1,g:1,b:1,a:0.5}, {letterSpacing:15, textCase:'UPPER'});

// ── VERSO ──
const verso = createFrame("Verso", 452, 0, 420, 600, PAPEL);

// Barra vermelha topo
createLine(verso, "Top Bar", 0, 0, 420, ARGILA);

createText(verso, "Back Title L1", 36, 48, 348, "O manual de liderança de produto", 18, FONT_BOLD, CONCRETO, {lineHeight:130});
createText(verso, "Back Title L2", 36, 72, 348, "para a era da IA", 18, FONT_BOLD, ARGILA, {lineHeight:130});

const backBody = "Em 2026, o mercado está cheio de livros sobre\nAI Product Management. O problema: foram\nescritos por consultores e acadêmicos.\n\nEste livro é diferente. Ele foi escrito por quem\nopera a transformação — com as mãos sujas,\nos erros reais, e as decisões que não têm\nresposta certa.";
createText(verso, "Back Body", 36, 130, 348, backBody, 13, FONT, CINZA, {lineHeight:170});

const bullets = "— Descubra em que nível de maturidade sua área está\n— Aprenda a decidir entre build, buy ou borrow\n— Redesenhe times com o PM Brain OS\n— Implemente rituais e governança para agentes\n— Leve o Custo Real Calculator pro seu CFO";
createText(verso, "Back Bullets", 36, 320, 348, bullets, 12, FONT, CINZA, {lineHeight:180});

createText(verso, "Back Footer", 36, 480, 348, "Fernanda Faria lidera produtos e times de tecnologia há mais de uma década. Foi executiva em plataformas de escala global e operou a transformação de times tradicionais em organizações AI-native.", 9, FONT, {r:0.541, g:0.522, b:0.494}, {lineHeight:150, letterSpacing:5});

// ── Zoom to fit ──
figma.viewport.scrollAndZoomIntoView([frente, lombada, verso]);
figma.closePlugin("✅ Capa criada! Frente + Lombada + Verso com todas as cores, textos e elementos. Ajuste os textos da lombada para orientação vertical no painel de propriedades.");
