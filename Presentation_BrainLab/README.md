# BrainLab: beamer-шаблон для докладов и выступлений

Тема `beamer` для докладов, конференций и публичных выступлений BrainLab.
Формат 16:9, фирменная палитра и логотип. Декор на титуле, слайдах разделов и
финальном слайде — оригинальная графика из шаблона BrainLab (папка `art/`), с теми же
позициями, поворотами и прозрачностью, что в pptx.
[Шаблон в Overleaf](https://www.overleaf.com/project/6af4821c40a785d6b31c2e0d/share#252d6cfe829accfded108d77dded3fb3c1d09364cc45f4e0)

Для лекций и семинаров (4:3, навигация разделов, `pdflatex`) есть отдельный шаблон —
[`Presentation_Lecture`](../Presentation_Lecture/README.md).

> **Скилл для Claude:** [`brainlab-pres`](../skills/brainlab-pres/SKILL.md)
> ([скачать `.skill`](../skills/brainlab-pres.skill)) — собирает доклад в этой
> теме из статьи (LaTeX, arXiv, PDF), из чужой beamer-презентации, из `.pptx`/PDF
> со слайдами или из ваших текста и картинок. Как установить — в
> [корневом README](../README.md#скиллы-для-claude).

## Быстрый старт

1. Скопируйте папку `Presentation_BrainLab/` целиком — вместе с `latexmkrc`, `art/` и `logos/`.
2. В `demo.tex` замените `\title`, `\subtitle`, `\author`, `\institute`, `\date`;
   язык подписей — опция `lang=ru|en`.
3. Слайды пишите обычными `frame`, разделы — через `\section` (слайд раздела появится
   сам), для титула, цитат, фото и финала используйте готовые команды (см. «Типы слайдов»).
4. Соберите XeLaTeX (подробности ниже):

   ```bash
   latexmk demo.tex
   ```

Собирается **XeLaTeX** (текст Montserrat, формулы — классический шрифт LaTeX). `pdflatex` тоже работает,
но тогда текст будет набран Lato.

```bash
latexmk demo.tex      # latexmkrc в папке уже включает XeLaTeX
```

На Overleaf: Menu → Settings → Compiler → **XeLaTeX** (или загрузите `latexmkrc` вместе с проектом).

> **TeX Live 2026** (минимум 2025). На Overleaf: Menu → Settings → TeX Live version →
> **2026**. Старые версии, особенно 2020 (Legacy), не поддерживаются: часть команд
> стилевика там не определена, и сборка падает или печатает мусор на первой странице.

Титул, разделы и спецслайды позиционируются через `tikz` `remember picture`, поэтому
нужно два прохода — `latexmk` и Overleaf делают их сами.

## Файлы

| Файл | Что это |
|---|---|
| `demo.tex` | Пример доклада со всеми типами слайдов, отсюда и начинайте |
| `brainpres.sty` | Оформление |
| `shortcuts.sty` | Математические сокращения (те же, что в `Presentation_Lecture`) |
| `logos/` | Логотип и знак BrainLab для светлого и тёмного фона |
| `art/` | Декор из шаблона: сеть, молекулы, водяные знаки, 3D-молекулы |
| `figures/example.jpg` | Картинка для примера `\imageframe` |
| `latexmkrc` | Включает XeLaTeX для `latexmk` и Overleaf |

```latex
\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[lang=ru]{brainpres}
```

| Опция | Значения | По умолчанию | Что делает |
|---|---|---|---|
| `lang` | `ru`, `en` | `ru` | Названия «План», теорем, алгоритмов, подписей |
| `sectionframes` | `auto`, `off` | `auto` | Слайд раздела после каждого `\section` |
| `font` | `montserrat`, `inter`, `nunito`, `roboto`, `sourcesans`, `arsenal`, `plex`, `fira`, `comfortaa` | `montserrat` | Шрифт текста (`comfortaa` — заголовки Comfortaa, текст Nunito) |

## Типы слайдов

```latex
\titleframe                                % титул (арт по умолчанию — network)
\titleframe[3d]                            % титул с другим артом, см. «Арт» ниже

\begin{frame}{\contentsname}\tableofcontents\end{frame}   % план: 01, 02, 03

\section{Метод}                            % слайд раздела «02 Метод» появится сам
\sectionframe                              % (или вручную, при sectionframes=off)

\begin{frame}{Заголовок}{Подзаголовок} ... \end{frame}    % обычный светлый слайд
\begin{frame}[dark]{Заголовок} ... \end{frame}            % тот же слайд на бордовом

\begin{frame}[c,dark]
  \statement[подпись]{Крупная мысль на весь слайд}
\end{frame}

\imageframe{figures/photo.jpg}{Заголовок}{Текст справа}   % фото на левую половину
\quoteframe{Текст цитаты}{Автор}
\finalframe{Спасибо!}{почта \\ telegram}                   % финал с 3D-молекулой
\finalframe[qr.png]{Спасибо!}{почта}                       % финал с QR-кодом справа
```

`\imageframe` обрезает картинку под левую половину слайда, сохраняя пропорции.

## Арт

Декор берётся из шаблона как есть. Арт задаёт и фон слайда: тёмный (бордовый) или светлый.

| Арт | Фон | Что это |
|---|---|---|
| `network` | тёмный | яркая сеть голубых и золотых узлов + бледная сеть (титул по умолчанию) |
| `network-light` | светлый | то же на светлом фоне |
| `molecule`, `molecule-light` | тёмный / светлый | крупный бледный водяной знак-молекула |
| `nodes`, `nodes-light` | тёмный / светлый | бледные узлы по краям (разделы по умолчанию) |
| `3d` | тёмный | 3D-молекула BrainLab (финал по умолчанию) |
| `3d-light`, `3d-side`, `3d-blue` | светлый | другие 3D-молекулы |
| `section-molecule` | светлый | бледная молекула справа |
| `none`, `none-light` | тёмный / светлый | без декора |

```latex
\titleframe[3d-light]        % арт титула
\settitleart{molecule}       % арт титула по умолчанию
\setsectionart{nodes-light}  % арт всех слайдов разделов
\setfinalart{network}        % арт финального слайда
\settitlewidth{8cm}          % ширина названия, если оно наезжает на арт
```

Ширина названия на титуле подобрана под каждый арт. На 3D-артах места меньше,
длинное название займёт 3–4 строки.

## Карточки и блоки

Белая карточка с цветной полосой слева, заголовок внутри:

```latex
\begin{card}{Заголовок} ... \end{card}          % бордовая полоса
\begin{cardgold}{Заголовок} ... \end{cardgold}  % золотая
\begin{plaincard} ... \end{plaincard}           % без заголовка
\begin{card}[height=4cm]{...} ... \end{card}    % в [] — любые опции tcolorbox

\statcard{87\%}{качества полного дообучения}    % крупная цифра с подписью
```

Стандартные `block`, `alertblock`, `exampleblock` и теоремы `thm`, `lem`, `defn`
оформлены так же: бордовая, синяя и золотая полосы. На тёмном слайде карточки тёмные.

Нумерованные списки — номера в кружках, маркированные — точки-«узлы».

## Шрифты

По умолчанию текст набирается **Montserrat** (полужирный — SemiBold), код — Fira Mono.
Формулы — классическим шрифтом LaTeX (**Computer Modern**, под XeLaTeX — его OpenType-версия
Latin Modern Math), как в обычных статьях. Все шрифты есть в TeX Live и на Overleaf;
шрифт текста выбирается опцией `font=` (см. таблицу опций), формулы от неё не зависят.

## Цвета

Палитра: `brainMaroon` `#854C65`, `brainMaroonDark` `#5B3445`, `brainPlum` `#412430`,
`brainCream` `#FAF8F1`, `brainGold` `#F0C987`, `brainGoldDark` `#A8731C`,
`brainSky` `#9DE1FC`, `brainBlue` `#0681B2`, `brainMauve` `#C397AA`.

Роли переключаются вместе с `[dark]`: `bltitle`, `bltext`, `blmuted`, `blaccent`,
`blitem`, `blnumber`, `blockbg`, `blocktext`. В своих слайдах используйте роли
(`\color{bltitle}`), тогда цвета будут правильными и на светлом, и на тёмном фоне.

## Что перенесено из `Presentation_Lecture`

Теоремы без нумерации (`thm`, `lem`, `defn`, `proof`, `\proofhead` / `\proofqed`),
подписи алгоритмов по `lang`, нумерация рисунков и таблиц, `\pdflink`, `\cmark`,
`\xmark`, `\oldstuff`, `\redstuff`, `\blfootnote`, `\Exp`, `\eqdef`, `\ve`, `\<a,b>`,
tikz-стили `presnode` / `presedge` и сокращения из `shortcuts.sty`.

## Известные особенности

- **Спецслайды не поддерживают оверлеи.** В `\titleframe`, `\sectionframe`,
  `\imageframe`, `\quoteframe`, `\finalframe` `\pause` и `\only` не работают:
  текст рисуется TikZ-узлами.
- **`\statement` центрируется по вертикали** только в кадре `[c]` (по умолчанию в beamer
  он и так `[c]`, если не задан `t` в `\documentclass`).
- **Под pdflatex** нужна `cm-super` для кириллицы (на Overleaf есть, локально
  `sudo tlmgr install cm-super lh`).
- Пакет `unicode-math` пишет в лог предупреждение о переопределении команд — это
  ожидаемо и безвредно.
- **Пакет `bm` не подключать** — он несовместим с `unicode-math`. `\bm{x}` и
  `\boldsymbol{x}` тема уже определяет сама (жирный курсив).
