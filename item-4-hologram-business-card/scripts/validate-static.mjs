import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
const root = resolve(process.cwd(), '..');
const htmlPath = resolve(root, 'docs/item4/index.html');
const html = readFileSync(htmlPath, 'utf8');
const required = ['<!doctype html>', '<html lang="ko">', 'data-tier="signature"', 'photoInput', 'pointermove', 'requestAnimationFrame', 'conic-gradient', 'GitHub Pages / Vercel'];
for (const token of required) if (!html.includes(token)) throw new Error(`Missing token: ${token}`);
const openTags = (html.match(/<script\b/g) || []).length;
const closeTags = (html.match(/<\/script>/g) || []).length;
if (openTags !== closeTags) throw new Error(`script tag mismatch ${openTags}/${closeTags}`);
for (const path of ['package.json', 'vercel.json', 'TESTING_GUIDE.md', 'PAGES_404_FIX.md', 'COMMENT_RESPONSE_ROUND2.md', 'public/index.html']) {
  if (!existsSync(resolve(process.cwd(), path))) throw new Error(`Missing ${path}`);
}
console.log('OK: item4 static demo tokens/files validated');
