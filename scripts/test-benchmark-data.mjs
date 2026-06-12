import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const modelPath = join(root, 'src/data/benchmarks/model-comparison.json');
const arenaPath = join(root, 'src/data/benchmarks/arena-snapshots.json');
const indexPath = join(root, 'src/pages/benchmarks/index.astro');
const arenaPagePath = join(root, 'src/pages/benchmarks/arena.astro');

assert.ok(existsSync(modelPath), 'model comparison data must exist');
assert.ok(existsSync(arenaPath), 'arena snapshot data must exist');
assert.ok(existsSync(indexPath), 'benchmark index page must exist');
assert.ok(existsSync(arenaPagePath), 'arena page must exist');

const modelData = JSON.parse(readFileSync(modelPath, 'utf8'));
assert.equal(modelData.artifact_type, 'resyst_labs_benchmark_rankings', 'model data must be public-site normalized');
assert.ok(modelData.generated_at, 'model data must include generated_at');
assert.ok(Array.isArray(modelData.rows), 'model data rows must be an array');
assert.ok(modelData.rows.length >= 5, 'model data must include at least five ranked rows');

for (const row of modelData.rows) {
  assert.ok(row.id, 'each row must include id');
  assert.ok(row.label, `row ${row.id} must include label`);
  assert.ok(row.basis, `row ${row.id} must include runtime/provider basis`);
  assert.ok(row.full?.final !== undefined, `row ${row.id} must include full.final`);
  assert.ok(row.swe?.swe_score !== undefined, `row ${row.id} must include swe.swe_score`);
  assert.ok(row.overall_score !== undefined, `row ${row.id} must include overall_score`);
}

const arenaData = JSON.parse(readFileSync(arenaPath, 'utf8'));
assert.equal(arenaData.artifact_type, 'resyst_labs_arena_snapshots', 'arena data must be public-site normalized');
assert.ok(Array.isArray(arenaData.matches), 'arena matches must be an array');
assert.ok(arenaData.matches.length >= 1, 'arena data must include at least one match');

for (const match of arenaData.matches) {
  assert.ok(match.id, 'each arena match must include id');
  assert.ok(match.entrants?.A && match.entrants?.B, `match ${match.id} must include entrants A/B`);
  assert.ok(['A', 'B', 'draw'].includes(match.winner), `match ${match.id} winner must be A, B, or draw`);
  assert.ok(Number.isFinite(match.turns), `match ${match.id} must include numeric turns`);
  assert.ok(match.artifacts?.replay, `match ${match.id} must include replay artifact path`);
}

const indexPage = readFileSync(indexPath, 'utf8');
assert.match(indexPage, /Resyst Labs Benchmarks/, 'index page must present the benchmark brand');
assert.match(indexPage, /Ranking/, 'index page must include ranking copy');
assert.match(indexPage, /Resyst Arena/, 'index page must link or describe Arena');

const arenaPage = readFileSync(arenaPagePath, 'utf8');
assert.match(arenaPage, /Resyst Arena/, 'arena page must present Resyst Arena');
assert.match(arenaPage, /turn-based/i, 'arena page must explain the turn-based lane');

console.log('benchmark data/page contract ok');
