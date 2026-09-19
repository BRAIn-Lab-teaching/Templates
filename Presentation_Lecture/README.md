# BrainLab LaTeX presentation template

Шаблон лекционной презентации на `beamer`. Компилируется `pdflatex` (на Overleaf — настройки по умолчанию). [Ссылка на шаблон в оверлиф](https://www.overleaf.com/read/btpqwqvvzvmd#f07248)

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

Фолбэков нет намеренно: любая другая опция или другое значение — ошибка компиляции с подсказкой,
что допустимо.

## Venue

| `venue` | Основной цвет | Второй цвет | Организация |
|---|---|---|---|
| `fpmi` | Vintage Berry `#8D4865` | Apricot Cream `#F7C57C` | МФТИ |
| `innopolis` | зелёный `#40BB20` | тёмно-синий `#13152A` | Innopolis University |
| `isp` | синий `#035BA9` | белый | ИСП РАН |

**Расширенное оформление включается только при `venue=fpmi`**: светлый фон слайдов, плашки под
блоками и теоремами, абрикосовая подложка под названием на титуле, бордовая полоска под верхним
колонтитулом (только на титульном слайде). `isp` и `innopolis` остаются в классическом виде —
белый фон, стандартные блоки beamer в фирменных цветах.

### Палитра ФПМИ

| Роль | Цвет | Где видно |
|---|---|---|
| `primary` | `#8D4865` Vintage Berry | плашка заголовка слайда, шапки блоков, колонтитул, маркеры списков |
| `secondary` | `#F7C57C` Apricot Cream | панель разделов, подложка названия на титуле, example-блоки |
| `surface` | `#FBEDD6` Papaya Whip | тело блоков и теорем, `tcolorbox` |
| `background` | `#FBF8F1` Floral White | фон слайда |
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
```

**Теоремы** — без нумерации, названия по опции `lang`:

```latex
\begin{thm} ... \end{thm}      % Теорема / Theorem
\begin{lem} ... \end{lem}      % Лемма / Lemma
\begin{defn} ... \end{defn}    % Определение / Definition
\begin{proof} ... \end{proof}  % Доказательство / Proof, с квадратиком в конце
```

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
\pdflink{Ссылка}{https://example.com/}  % ссылка с красным бейджем PDF
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
\f^2_i(x)               % f^2_i(x) с масштабируемыми скобками; также \g и \h
\argmin \argmax \dom \conv \dist \diam \Var \sign
```

`\f`, `\g`, `\h` занимают короткие имена. Если подключите пакет, который их использует,
переименуйте вызовы `\newfuncmacro` в `shortcuts.sty`.

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
- **В середине `pres.sty` есть `\makeatother`.** Если дописываете туда код с `@` в именах,
  оборачивайте его в `\makeatletter ... \makeatother`, иначе получите `Undefined control sequence`.
- **`shortcuts.sty` объявляет себя как `utils/shortcuts`**, поэтому LaTeX выдаёт предупреждение
  `You have requested package 'shortcuts', but the package provides 'utils/shortcuts'`.
  Это безвредно; чтобы убрать — поправьте имя в `\ProvidesPackage` на `shortcuts`.
- **`\expect` сейчас не работает**: вспомогательная команда `\expect@split` в `shortcuts.sty`
  закомментирована (строки 97–103), и вызов падает с `Undefined control sequence`.
  Пока пользуйтесь `\EE`, `\Exp` или `\ED{...}`; чтобы вернуть `\expect` — раскомментируйте блок.
