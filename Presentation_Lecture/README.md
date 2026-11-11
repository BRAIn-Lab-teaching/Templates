# BrainLab: beamer-шаблон для лекций

Шаблон лекционной презентации на `beamer` для курсов и семинаров: формат 4:3,
панель разделов сверху, теоремы и алгоритмы, оформление под площадку
(`venue=fpmi|innopolis|isp`). Компилируется `pdflatex` (на Overleaf — компилятор pdfLaTeX по умолчанию).
[Шаблон в Overleaf](https://www.overleaf.com/read/btpqwqvvzvmd#f07248)

> **TeX Live 2026** (минимум 2025). На Overleaf: Menu → Settings → TeX Live version →
> **2026**. Старые версии, особенно 2020 (Legacy), не поддерживаются: часть команд
> стилевика там не определена, и сборка падает или печатает мусор на первой странице.

Для докладов и публичных выступлений (16:9, декор, XeLaTeX) есть отдельный шаблон —
[`Presentation_BrainLab`](../Presentation_BrainLab/README.md).

> **Скилл для Claude:** [`brainlab-lecture-pres`](../skills/brainlab-lecture-pres/SKILL.md)
> ([скачать `.skill`](../skills/brainlab-lecture-pres.skill)) — верстает или
> переоформляет лекцию в этом стилевике из чужого beamer-`.tex` с любой темой,
> PDF или `.pptx` слайдов, конспекта, markdown или просто текста и формул. Как
> установить — в [корневом README](../README.md#скиллы-для-claude).

## Быстрый старт

1. Скопируйте папку `Presentation_Lecture/` целиком. Для старой лекции достаточно
   положить рядом с ней новые `pres.sty` и `shortcuts.sty` (см. «Совместимость»).
2. В `main.tex` выберите площадку и язык: `\usepackage[venue=fpmi,lang=ru]{pres}`.
3. Замените `\title`, `\subtitle`, `\author`, `\date`, разбейте лекцию на `\section`
   — из них строится панель навигации.
4. Соберите (два прохода, см. ниже):

   ```bash
   latexmk -pdf main.tex
   ```

> **Нужно минимум два прохода компиляции.** Верхняя панель разделов (`miniframes`) строится
> по файлу `.nav`, при одном проходе она пустая. `latexmk` и Overleaf делают это сами;
> голый `pdflatex` запускайте дважды.

```bash
pdflatex main.tex && pdflatex main.tex
```

## Файлы

| Файл | Что это |
|---|---|
| `main.tex` | Пример презентации, он же точка входа. Отсюда и начинайте |
| `pres.sty` | Оформление: опции, цвета venue, теоремы, алгоритмы, макросы |
| `shortcuts.sty` | Математические сокращения |
| `logos/` | Логотипы в PNG, обычные и квадратные версии |

## Опции пакета

Передаются в `\usepackage[...]{pres}`:

```latex
\usepackage[venue=fpmi,lang=ru,navsymbols=hide]{pres}
```

| Опция | Значения | По умолчанию | Что делает |
|---|---|---|---|
| `venue` | `fpmi`, `innopolis`, `isp` | `fpmi` | Цвета, логотип, название организации |
| `lang` | `ru`, `en` | `ru` | Названия теорем, алгоритмов, подписей |
| `navsymbols` | `show`, `hide` | `show` | Кнопки навигации внизу справа |
| `braces` | `smart`, `physics` | `smart` | `smart` — «умные» скобки у `\qty`, `\norm`, `\scalar` (см. ниже); `physics` — как в пакете `physics` |
| `plots` | `on`, `off` | `on` | `pgfplots` и `tikz-3dplot`; `off` ускоряет сборку, если графиков нет |
| `braket` | `on`, `off` | `on` | Пакет `braket` (`\bra`, `\ket`, `\braket`, `\set`, `\Set`) поверх `physics` |

Фолбэков нет намеренно: любая другая опция или другое значение — ошибка компиляции с подсказкой,
что допустимо.

## Совместимость со старыми версиями

Этот `pres.sty` (v3.1) собирает презентации, написанные под все прежние варианты стилевика:
исходный `pres.sty` из этого репозитория, `pres.sty` с pgfplots и `braket` и `pres-2.sty` (v3.0)
с логотипами и опциями. Достаточно положить рядом с презентацией новые `pres.sty` и
`shortcuts.sty`. Что для этого сделано:

- `prop`, `\AlgInput`, `\AlgOutput` создаются, только если презентация не объявила их сама —
  старые `\newtheorem*{prop}{...}` в преамбуле не падают с `already defined`.
- Умные скобки не трогают формы `physics`, которых не знают: `\norm*{x}`, `\norm\big{x}`,
  `\qty\big(x)` работают как раньше.
- `\braket` понимает оба синтаксиса: `\braket{a|b}` (braket) и `\braket{a}{b}` (physics).
- `\expect` работает и с индексами: `\expect_{\xi}{X | Y}`.

Внешний вид старых презентаций может немного отличаться: скобки `\qty(...)` у невысокого
содержимого теперь `\bigl`/`\bigr`, наконечник `->` в TikZ — `latex`. Вернуть скобки
`physics` — опция `braces=physics`.

## Venue

| `venue` | Основной цвет | Второй цвет | Организация |
|---|---|---|---|
| `fpmi` | Vintage Berry `#8D4865` | Apricot Cream `#F7C57C` | МФТИ |
| `innopolis` | зелёный `#40BB20` | тёмно-синий `#13152A` | Innopolis University |
| `isp` | синий `#035BA9` | белый | ИСП РАН |

**Расширенное оформление включается только при `venue=fpmi`**: плашки под
блоками и теоремами, абрикосовая подложка под названием на титуле, бордовая полоска под верхним
колонтитулом (только на титульном слайде). Фон слайдов белый во всех venue. `isp` и `innopolis`
остаются в классическом виде — стандартные блоки beamer в фирменных цветах.

### Палитра ФПМИ

| Роль | Цвет | Где видно |
|---|---|---|
| `primary` | `#8D4865` Vintage Berry | плашка заголовка слайда, шапки блоков, колонтитул, маркеры списков |
| `secondary` | `#F7C57C` Apricot Cream | панель разделов, подложка названия на титуле, example-блоки |
| `surface` | `#FBEDD6` Papaya Whip | тело блоков и теорем, `tcolorbox` |
| `background` | `#FFFFFF` белый | фон слайда |
| `accent` | `#8A5A12` | ссылки, `\alert`, alert-блоки |
| `ink` | `#3A2233` | основной текст |

Названия ролей одинаковы для всех venue, значения — разные. В своих слайдах используйте роли
(`\color{primary}`), а не сырые имена палитры (`berry`, `apricot`), иначе при смене venue цвета
разъедутся.

## Что доступно в документе

**Цвета:** `primary`, `secondary`, `accent`, `surface`, `background`, `ink`, `onPrimary`,
`onSecondary`, а также `statusOk` / `statusBad` для галочек и предупреждений.

**Готовые стили:**

```latex
\begin{tcolorbox}[title=Заголовок] ... \end{tcolorbox}   % стиль presbox применён по умолчанию
\node[presnode] (a) {узел};                              % tikz: узел в цветах venue
\draw[presedge] (a) -- (b);                              % tikz: стрелка
\node[dot] at (0,0) {};                                  % tikz: точка
```

Подключены TikZ-библиотеки `positioning, calc, automata, arrows.meta, intersections,
decorations.markings, patterns, patterns.meta`; при `plots=on` — `pgfplots`
(`compat=1.17`) с библиотекой `fillbetween` и `tikz-3dplot`.

**Логотипы на титуле.** По умолчанию — логотип площадки. Добавить ещё (в преамбуле, после
`\usepackage{pres}`):

```latex
\AddLogo{logos/isp.png}
\AddLogo[height=1.1cm]{logos/other.pdf}   % своя высота или width=...
\ClearLogos                               % убрать все, включая логотип площадки
```

Размеры: `\LogoHeight` (0.8cm), `\LogoSep` (1.2em), `\LogoMaxWidth` (0.9\paperwidth — шире ряд
ужимается целиком).

**Теоремы** — без нумерации, названия по опции `lang`:

```latex
\begin{thm} ... \end{thm}      % Теорема / Theorem
\begin{lem} ... \end{lem}      % Лемма / Lemma
\begin{defn} ... \end{defn}    % Определение / Definition
\begin{prop} ... \end{prop}    % Утверждение / Proposition
\begin{proof} ... \end{proof}  % Доказательство / Proof, с квадратиком в конце
```

Длинное доказательство можно разорвать между кадрами: `\proofhead` (или `\proofhead[Набросок]`)
в начале на одном слайде, `\proofqed` в конце на другом.

**Алгоритмы** — подпись без номера, `\Require` / `\Ensure` переведены по `lang`:

```latex
\begin{algorithm}[H]
  \caption{Субградиентный метод}
  \begin{algorithmic}[1]
    \Require шаг $\gamma > 0$        % "Вход:" / "Input:"
    \State $w^{k+1} = w^k - \gamma g^k$
    \Ensure $w^K$                    % "Выход:" / "Output:"
  \end{algorithmic}
\end{algorithm}
```

`\AlgInput{...}` / `\AlgOutput{...}` — то же, что `\Require` / `\Ensure`, но строкой без номера.

**Рисунки и таблицы** — нумерация подписей включена, `\ref` работает:

```latex
\begin{figure}
  \includegraphics[width=0.5\linewidth]{plot.pdf}
  \caption{Подпись}\label{fig:plot}
\end{figure}
См. рис.~\ref{fig:plot}.   % -> "Рис. 1: Подпись"
```

**Макросы:**

```latex
\pdflink{Ссылка}{https://example.com/}  % ссылка с бейджем PDF (в fpmi — бордовым)
\cmark  \xmark                          % зелёная галочка / красный крестик
\oldstuff{текст}  \redstuff{текст}      % мелкие цветные пометки
\blfootnote{сноска без номера}
\Exp  \eqdef  \ve{a}{b}  \<a,b>         % E, "=" с def, скалярное произведение
```

## Сокращения из `shortcuts.sty`

Множества `\R \N \Z \Q \Ss \Rd`, каллиграфические `\cA`–`\cZ` (кроме `\cI`),
матрицы `\mA`–`\mZ` (кроме `\mD`), буквенные векторы `\vc`–`\vz` (кроме `\vd`, `\vk`),
`\e` = `\varepsilon`.

Три коротких имени заняты другим: `\va{x}`, `\vb{x}`, `\vu{x}` — это команды пакета `physics`
(вектор со стрелкой, жирный вектор, единичный вектор), они требуют аргумент;
`\ve{a}{b}` из `pres.sty` — скалярное произведение, вектор `e` называется `\vve`.

```latex
\scalar{a, b}           % <a, b>
\norm{x} \abs{x} \set{a,b} \cbraces{x} \sbraces{x}
\EE  \Exp  \ED{X}       % математическое ожидание
\expect{X}  \expect_{\xi}{X | Y}   % E[X], условное E_xi[X | Y]
\PP(A)                  % вероятность (\mathds из dsfont)
\f^2_i(x)               % f^2_i(x) с масштабируемыми скобками; также \g и \h
\argmin \argmax \dom \conv \dist \diam \Var \sign
```

`\f`, `\g`, `\h` занимают короткие имена. Если подключите пакет, который их использует,
переименуйте вызовы `\newfuncmacro` в `shortcuts.sty`.

**Умные скобки** (`braces=smart`): `\qty(...)`, `\qty[...]`, `\qty{...}`, `\qty|...|`, `\norm{...}`,
`\scalar{...}` измеряют содержимое. Если оно не выше `x^{k+1+f}_f`, ставятся `\bigl`/`\bigr`,
иначе `\left`/`\right`. Формы `\norm*{x}`, `\norm\big{x}`, `\qty\big(x)` обрабатывает `physics`.

**`braket`** (`braket=on`) переопределяет `\bra`, `\ket`, `\set` и добавляет `\Set`, `\Braket`.
`\set{x | x > 0}` — множество с вертикальной чертой; `\braket` понимает и `\braket{a|b}`,
и `\braket{a}{b}`.

## Известные особенности

- **Кириллица требует шрифтов `cm-super` и `lh`.** Без них `pdflatex` сыплет
  `Font T2A/cmss/... not loadable` и выдаёт пустые страницы — текст молча теряется.
  На Overleaf всё уже стоит, локально: `sudo tlmgr install cm-super lh`.
- **Главный язык babel — русский, независимо от опции `lang`.** `lang` меняет только названия
  теорем, алгоритмов и подписей. Для англоязычной презентации переносы будут по русским
  правилам; если это важно, добавьте `\selectlanguage{english}` в начало документа.
- **`amsxtra` намеренно не подключён.** Он переопределяет `\nobreakspace` как
  `\unskip\nobreak\ \ignorespaces`, и `\unskip` съедает пробел перед `~` — заметно на `\pdflink`.
- **`pstricks` закомментирован** в списке пакетов: он несовместим с `pdflatex`. Если нужен,
  раскомментируйте и собирайте через `latex` + `dvips` или `xelatex`.
- **`svg`** подключён, но `\includesvg` требует `--shell-escape` и установленного inkscape.
- **Подписи алгоритмов без номеров** — это задумано (`\thealgorithm` пустой). Рисунки и таблицы
  при этом нумеруются.
- **`pgfplots` замедляет сборку.** Если в лекции нет графиков — `plots=off`.
