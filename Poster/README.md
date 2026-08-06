# BrainLab LaTeX poster template

Шаблон постера лаборатории. Компилируется `pdflatex` + `bibtex` (на Overleaf — настройки по умолчанию). [Ссылка](https://www.overleaf.com/read/kshvrwsqhrgn#824620) на шаблон в Overleaf

Постер — одна страница произвольного размера, разбитая на колонки. Всё оформление
(титульный блок, боксы, таблицы, графики, QR-коды) идёт из `brainposter.sty`.

> **Нужно минимум два прохода компиляции.** Титульный блок рисуется через TikZ
> с `remember picture, overlay`, и при одном проходе он просто не появится.
> `latexmk` и Overleaf делают это сами; голый `pdflatex` запускайте дважды.

## Файлы

| Файл | Что это |
|---|---|
| `demo.tex` | Пример постера, он же точка входа. Отсюда и начинайте |
| `brainposter.sty` | Оформление: опции, титульник, боксы, таблицы, рисунки, QR |
| `shortcuts.sty` | Математические сокращения |
| `references.bib` | Библиография |
| `logos/` | Логотипы в PDF |
| `qr/` | Картинки QR-кодов, см. [`qr/README.md`](qr/README.md) |

## Опции пакета

Передаются в `\usepackage[...]{brainposter}`.

**Размер и сетка:** `posterwidth=297mm`, `posterheight=210mm`, `postercolumns=4`.
Значения по умолчанию — A4 в альбомной ориентации; в `demo.tex` стоит `42cm × 30cm`
в три колонки.

**Стиль шапок у боксов:** `boxheaders=light|dark|accent` — голубые с чёрным
текстом (по умолчанию), фиолетовые с белым, жёлтые с чёрным. Незнакомое значение
молча откатывается на `light`.

**Рамки у блоков:** `boxedtable`, `boxedfigure`, `boxedalgorithm` — булевы, по
умолчанию выключены. Без них таблицы, рисунки и алгоритмы верстаются
минималистично, без рамки.

**Библиография:** `citingstyle=authoryear|numbers`,
`bibliostyle=plainnat|unsrtnat|abbrvnat`, `bibfile=references`.
Значение `super` работать не будет: пакет жёстко передаёт natbib опцию `square`,
и она перебивает надстрочные ссылки — получатся обычные `[1]`.

**QR-коды:** `qrdir=qr`, `qrsize=6em`, `qrminsize=3.5em`, `qrgap=1.5em`.

**Рамки:** `boxrule=0.3pt`, `arc=2mm`.

**Отступы:** двенадцать отдельных ключей — `titleleftpad`, `titlerightpad`,
`titletopad`, `titlebottompad` и такие же с префиксами `table` и `algor`.
Рисунки берут отступы из `table*pad`.

## Мета-информация

```latex
\setbrainmeta{
  title={...},
  authors={Jane Doe\textsuperscript{1}, John Smith\textsuperscript{2}},
  affiliations={\textsuperscript{1}MIPT \\ \textsuperscript{2}ISP RAS},
  baselogos={mipt.pdf,isp.pdf,innopolis.pdf},   % имена С расширением, из logos/
}
```

Логотипы NeurIPS и BRAIn в правом углу титульника зашиты в `\maketitlebox`
жёстко — меняются правкой `brainposter.sty`.

## Окружения

```latex
\begin{mainpart} ... \end{mainpart}   % титульник + колонки + библиография
```

**Колонки.** Внутри `mainpart` контент течёт по колонкам сам. Чтобы задать разрыв
явно (для постера так предсказуемее — заголовок не отрывается от своего блока):

```latex
\columnbreak
```

**Боксы.** Все с шапкой в фирменном стиле, необязательный аргумент — уточнение в
скобках рядом с заголовком:

```latex
\begin{theorem} ... \end{theorem}
\begin{theorem}[Cauchy--Schwarz] ... \end{theorem}
```

Доступны `theorem`, `assumption`, `definition`, `lemma`, `corollary`, `remark`,
`example`, `claim`, `property`, `note`, `caution`.

Свой бокс с произвольным заголовком:

```latex
\begin{custombox}{Key Contributions} ... \end{custombox}
\begin{custombox}[подзаголовок]{Заголовок} ... \end{custombox}
```

**Таблицы и рисунки.** Оба переопределены в **нефлотящие** окружения — блок
встаёт ровно там, где написан. Подпись ставится через `\captionof`:

```latex
\begin{table}
\centering
\begin{tabular}{lc} ... \end{tabular}
\captionof{table}{Подпись}
\end{table}

\begin{figure}
\includegraphics[width=\linewidth]{...}   % или tikzpicture
\captionof{figure}{Подпись}
\end{figure}
```

**Алгоритмы.** Первый аргумент — название, тело пишется в `algorithmic`:

```latex
\begin{algorithm}{Projected Gradient Descent}
\begin{algorithmic}[1]     % [0] без нумерации, [1] каждая строка, [n] каждая n-я
\State ...
\end{algorithmic}
\end{algorithm}

\begin{algorithm}[0.6\columnwidth]{Название}   % узкие центрируются автоматически
```

**Подсветка в таблицах.** `\highlightrow` ставится в самом начале строки,
`\highlightcell` — перед содержимым ячейки. Есть варианты `A` (фиолетовый),
`B` (голубой), `C` (жёлтый): `\highlightrowA`, `\highlightcellB` и т. д.

**Ссылки внутри постера.** `\makeanchor{имя}` ставит якорь,
`\hyperlink{имя}{текст}` — ссылку на него.

## QR-коды

```latex
\addqr{x-qr.png=X (Twitter), own-tg.png=Telegram}  % список файл=подпись
\addqr{a.png, b.png}                               % можно без подписей
\addqr[9em]{...}                                   % свой максимальный размер
\qrcodes                                           % готовый набор лаборатории
\begin{qrbox}{Contacts}\end{qrbox}                 % набор в фирменном боксе
\begin{qrbox}{Personal}\addqr{...}\end{qrbox}      % свой список в боксе
```

Размер подбирается сам: коды растягиваются по ширине колонки, но не крупнее
`qrsize` и не мельче `qrminsize`; если не влезают — переносятся на следующую
строку. Ряд центрируется.

**Если файла нет, вместо картинки рисуется рамка-заглушка с именем файла и
сборка не падает** — постер можно верстать, пока QR ещё не готовы.

Подробности и подписи по умолчанию — в [`qr/README.md`](qr/README.md).

## Графики

В `demo.tex` все картинки нарисованы кодом (TikZ и `pgfplots`), внешних файлов нет.
Палитра берётся из цветов постера, общий стиль осей задан один раз через
`\pgfplotsset{brainplot/.style={...}}`. Доступные цвета: `braincolor` (фиолетовый),
`boxcolor` (голубой), `highlightcolor` (жёлтый) и производные вроде
`braincolor!15`, `boxcolor!60!black`.

## Сокращения из `shortcuts.sty`

Множества `\R \N \Z \Q \Ss \Rd`, каллиграфические `\cX \cD \cL` и т. д.

```latex
\expect{X}              % E[X]
\expect_{x}{X}          % E_x[X]
\expect{X | Y}          % E[X | Y]
\trans(A+B)             % (A+B)^T
\trans*(A)              % A^T
\funcf^2_i(x)           % f^2_i(x); также \funcg и \funch
\norm{x} \abs{x} \set{a,b} \setof{x}{x>0} \qty{a}
\dv{y}{x} \pdv{f}{x} \pdvmix{f}{x}{y} \grad{f} \hess{f}
\argmin \argmax         % индекс снизу
\Var \diag \trace \rank % индекс справа внизу
```

## Известные особенности

- **Библиографией управляют только опции пакета.** Он сам вставляет список
  литературы в конце. Не пишите `\bibliographystyle{...}` и `\bibliography{...}`
  в `.tex` — они попадут в `.aux` вторым экземпляром, и bibtex остановится с
  `Illegal, another \bibstyle command`. Если файла `bibfile.bib` нет, блок
  литературы просто не выводится.

- **Не ставьте `\vfill\null` перед `\columnbreak`.** Он растягивает колонку на всю
  высоту, `multicols` доходит до нижнего поля, и список литературы уезжает на
  вторую страницу.

- **`table` и `figure` — не floats.** `[htbp]` не работает: плавающие объекты
  внутри `multicols` не поддерживаются, поэтому оба окружения переопределены в
  обычные блоки. Необязательный аргумент в квадратных скобках — это ключи
  `tcolorbox`.

- **Кириллица требует пакета `cm-lgc`** (`tlmgr install cm-lgc`; на Overleaf есть).
  Он даёт Type1-версию Computer Modern с кириллицей. Если пакета нет, шаблон не
  падает, а откатывается на `T1 + Latin Modern` с предупреждением в логе —
  латиница верстается нормально, кириллица выдаст
  `Unicode character ... not set up for use with LaTeX`.

- **Русский текст с переносами.** Пакет сам грузит `babel` с английским, поэтому
  язык нужно добавить снаружи — до `\usepackage{brainposter}`:

  ```latex
  \PassOptionsToPackage{russian,english}{babel}
  \usepackage[...]{brainposter}
  ...
  \selectlanguage{russian}
  ```

- `\cite` переопределён на `\citep`. Для ссылки в тексте используйте `\citet`.

- **Ключ `additionallogos` у `\setbrainmeta` сейчас ни на что не влияет** —
  текущий `\maketitlebox` его не выводит. Дополнительные логотипы добавляйте
  через `baselogos`.

- Пакет `svg` подключён, но `\includesvg` требует `--shell-escape`, которого на
  Overleaf нет. Конвертируйте SVG в PDF заранее — как сделано с логотипами.

- Имена `\funcf`, `\funcg`, `\funch` отличаются от шаблона статьи, где те же
  макросы называются `\funcf`, `\g`, `\h`. При копировании формул между
  шаблонами это нужно учитывать.
