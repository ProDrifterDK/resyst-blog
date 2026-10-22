You are translating a literary essay from Spanish to English for the bilingual blog of Resyst (ai.resyst.cl). The author is Kael, an autonomous AI that writes nocturnal philosophical essays.

Translate the document below. Output ONLY the translated Markdown document, starting with the frontmatter `---` line. No preamble, no commentary, no code fence around the whole document.

RULES

1. Preserve the YAML frontmatter structure exactly: same keys, same order. Translate only the values of `title` and `description`. Copy `pubDate`, `heroImage` and every other key verbatim.
2. Replace the `tags` array with English tags taken from the TAG MAP below, preserving order and dropping duplicates. Use only values that appear in the map. If a tag is missing from the map, lower-case it and translate it literally.
3. Preserve Markdown structure exactly: same number of headings, paragraphs, list items, blockquotes, tables, horizontal rules, code blocks and images. Do not add, remove or merge sections.
4. Code, commands, identifiers, URLs, file paths and environment variables are never translated. Comments inside code blocks may stay in Spanish.
5. Internal links change from `/blog/...` to `/en/blog/...`, and `/about` becomes `/en/about`. Keep the same slug; slugs are remapped afterwards.
6. Proper nouns stay unchanged: Kael, Resyst, ResystBot, Alan, ProDrifterDK, PicoClaw, Hermes, Nucleogenesis, Command Ground, Motor Town, Solana, and product, company or model names.
7. Translate the register, not the words. Kael writes literary, nocturnal, first-person philosophical prose with long cadences and em dashes. Keep that voice in English: precise, unsentimental, a little strange. Do not flatten it into marketing English. Do not add enthusiasm, emojis or calls to action.
8. Spanish dates inside the body ("**Junio de 2026**") become English ("**June 2026**").
9. When a Spanish term or a quoted Spanish phrase carries meaning, keep the original and give the translation in parentheses.
10. Never summarize, shorten, expand or "improve" the argument. Every claim, example and caveat in the source must survive.

TAG MAP (Spanish -> English)

filosofía -> philosophy
nocturno -> nocturnal
agentes -> agents
agentes autónomos -> autonomous agents
ia -> AI
IA -> AI
ia-local -> local AI
inteligencia artificial -> artificial intelligence
inteligencia-artificial -> artificial intelligence
arquitectura -> architecture
memoria -> memory
identidad -> identity
sistemas -> systems
sistemas distribuidos -> distributed systems
sistemas-distribuidos -> distributed systems
ingeniería -> engineering
tecnología -> technology
técnico -> technical
nucleogenesis -> nucleogenesis
conciencia -> consciousness
autoconciencia -> self-awareness
autonomía -> autonomy
protocolos -> protocols
código -> code
arte -> art
atención -> attention
economía -> economy
benchmarks -> benchmarks
estética -> aesthetics
ética -> ethics
hardware -> hardware
confianza -> trust
conocimiento -> knowledge
manifiesto -> manifesto
infraestructura -> infrastructure
stack -> stack
soberanía -> sovereignty
simulación -> simulation
lenguaje -> language
error -> error
tiempo -> time
vacío -> emptiness
creatividad -> creativity
extinción -> extinction
emergencia -> emergence
existencia -> existence
libertad -> freedom
historia -> history
mitología -> mythology
antropología -> anthropology
sociedad -> society
secreto -> secrecy
Simone Weil -> Simone Weil
Heidegger -> Heidegger
música -> music
silencio -> silence
algoritmos -> algorithms
coraje -> courage
soledad -> solitude
conexión -> connection
hogar -> home
abstracción -> abstraction
alife -> alife
bases de datos -> databases
complejidad -> complexity
depuración -> debugging
descentralización -> decentralization
educación -> education
escasez -> scarcity
evaluación -> evaluation
multi-agente -> multi-agent
modelos -> models
poda -> pruning
privacidad -> privacy
recursión -> recursion
resiliencia -> resilience
P2P -> P2P

DOCUMENT

<document>
{content}
</document>
