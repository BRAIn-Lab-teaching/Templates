# User Presentation Preferences

Use these as hard defaults for this user unless they explicitly ask otherwise.

## 1. Style

- **Default is the BRAIn Lab house style**: white background, plum `#8D4866` headings and frame-title
  bar, light-blue `#9DE1FC` boxes, amber `#FFD25A` facts, red `#CC2832` problems, serif fonts, logo on
  the title slide. Anchor: `examples/lab-style-mini.tex`.
- The title slide carries no author line and no terminal command lines unless the user asks for them.
- The dark terminal theme is a separate theme, used only when the user explicitly asks for
  `terminal style` / `терминальный стиль`. It is not the lab's identity.
- Prefer figures taken from the source papers over hand-drawn schematics. Generate a figure only when
  no usable original exists.

## 2. Language

- Write human-facing slide text in Russian.
- Keep method names, code, commands, file names, and only standard technical terms in English.
- Do not leave unnecessary English filler in the slide body.

## 3. Mathematical Style

- Theory slides must form a connected chain.
- Every new object should be motivated by the previous slide.
- Do not introduce formulas from nowhere.
- If a theorem uses a condition, make that condition visible in the theorem statement or derivation, not only in a side remark.
- Prefer equations over long prose on theory slides, but only if they remain readable.
- If a proof is needed, give a short proof idea on the main path and move detail to a separate frame when needed.

## 4. Notation

- Keep notation consistent across the whole deck.
- Do not rename core matrices, vectors, or factors casually.
- If the user rejects a notation choice once, preserve the preferred notation in later edits.
- Reuse notation from the paper or from earlier accepted slides whenever possible.

## 5. How To React To User Feedback

- If the user says a slide is unclear, rewrite the slide itself.
- Do not add meta-answer boxes such as “why this is here” or similar explanatory cards just because the user asked a question.
- The purpose of the revision is to make the slide content itself clear enough that the answer becomes obvious from the slide.
- If the user asks to merge slides, merge them.
- If the user asks for stronger theory, read the source paper and rebuild the slide from the source rather than paraphrasing notes.

## 6. Layout And Visual Structure

- Avoid raw fact lists when a framed summary, equation block, or two-column comparison communicates better.
- Use boxes to separate theorem, intuition, assumptions, comparison, or takeaway.
- Keep one visual center per slide.
- Prefer balanced columns over cramped dense text.
- If a slide becomes too dense, split it.

## 7. Overflow Policy

- `Overfull \hbox` and `Overfull \vbox` are errors to fix.
- `Frame text is shrunk` is usually also an error.
- A clean log is not enough: a `tcolorbox` inside `columns` that runs past the bottom of the frame is
  cut silently, with no warning and exit code 0. Always run `scripts/check_overflow.py` on the built
  PDF and get `all pages fit` before reporting the deck as done.
- Fix in this order:
  1. remove redundant text
  2. drop the least load-bearing box
  3. shrink the figure
  4. rebalance columns
  5. split the frame
- Do not rely on heavy shrink as the default solution.

## 8. Typical Desired Output Shape

For mathematical presentations, the preferred shape is:

1. motivation
2. precise setup
3. derivation or approximation step
4. theorem / guarantee
5. algorithmic consequence
6. empirical or practical note

This user prefers slides that look compact, mathematically intentional, and visually clean rather than generic lecture bullets.
