import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
const root = resolve(process.cwd(), '..');
const htmlPath = resolve(root, 'docs/item4/index.html');
const html = readFileSync(htmlPath, 'utf8');
const required = [
  '<!doctype html>',
  '<html lang="ko">',
  'data-tier="signature"',
  'data-style="circle"',
  'data-style="grid"',
  'data-style="glitch"',
  'data-style="prism"',
  'data-lang="ko"',
  'data-lang="en"',
  'photoInput',
  'pointermove',
  'requestAnimationFrame',
  'conic-gradient',
  'Weakness',
  'Resistance',
  'Retreat Cost',
  'GitHub Pages / Vercel'
];
for (const token of required) if (!html.includes(token)) throw new Error(`Missing token: ${token}`);
const banned = [/포켓몬/i, /유희왕/i, /pokemon/i, /yu-gi-oh/i, /yugioh/i];
for (const re of banned) if (re.test(html)) throw new Error(`Banned IP token found: ${re}`);
const openTags = (html.match(/<script\b/g) || []).length;
const closeTags = (html.match(/<\/script>/g) || []).length;
if (openTags !== closeTags) throw new Error(`script tag mismatch ${openTags}/${closeTags}`);
for (const path of ['package.json', 'vercel.json', 'TESTING_GUIDE.md', 'PAGES_404_FIX.md', 'COMMENT_RESPONSE_ROUND2.md', 'COMMENT_RESPONSE_ROUND3.md', 'GAME_CARD_MAPPING_SPEC.md', 'public/index.html']) {
  if (!existsSync(resolve(process.cwd(), path))) throw new Error(`Missing ${path}`);
}
console.log('OK: item4 high-detail game-card holo demo tokens/files validated');
