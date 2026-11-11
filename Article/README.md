# BrainLab: шаблон статьи

Шаблон статьи лаборатории: препринты, arXiv, приложения к заявкам, внутренние
отчёты. Одна или две колонки, фирменный титульник с логотипами, боксы для
теорем, таблиц и алгоритмов. Компилируется `pdflatex` + `bibtex` (на Overleaf —
компилятор pdfLaTeX по умолчанию). [Шаблон в Overleaf](https://www.overleaf.com/read/ctmzkhnmckpw#e2be80)

> **TeX Live 2026** (минимум 2025). На Overleaf: Menu → Settings → TeX Live version →
> **2026**. Старые версии, особенно 2020 (Legacy), не поддерживаются: часть команд
> стилевика там не определена, и сборка падает или печатает мусор на первой странице.

> **Скилл для Claude:** [`brainlab-article`](../skills/brainlab-article/SKILL.md)
> ([скачать `.skill`](../skills/brainlab-article.skill)) — переводит готовую
> статью из любого шаблона конференции (NeurIPS, ICML, ICLR, IEEE, ACM, LNCS,
> elsarticle…) в этот стилевик, не трогая текст. Как установить — в
> [корневом README](../README.md#скиллы-для-claude).

## Быстрый старт

1. Скопируйте папку `Article/` целиком (или откройте шаблон в Overleaf → Menu → Copy Project).
2. Переименуйте `demo.tex` под свою статью, если нужно, и замените в нём содержимое
   `\setbrainmeta{...}` (название, авторы, аффилиации, аннотация).
3. Пишите текст внутри `\begin{mainpart} ... \end{mainpart}`, приложение — в `appendixpart`.
4. Литературу добавляйте в `references.bib`, ссылайтесь через `\citep` / `\citet`.
5. Соберите:

   ```bash
   latexmk -pdf demo.tex
   ```

Одна колонка вместо двух — закомментируйте `twocolumnmode` в опциях пакета.

## Файлы

| Файл | Что это |
|---|---|
| `demo.tex` | Пример статьи, он же точка входа. Отсюда и начинайте |
| `brainlab.sty` | Оформление: опции, титульник, боксы для теорем/таблиц/алгоритмов |
| `shortcuts.sty` | Математические сокращения |
| `references.bib` | Библиография |
| `logos/` | Логотипы в PDF. `NeurIPS-logo.svg` лежит для справки — `pdflatex` его не умеет |

## Опции пакета

Передаются в `\usepackage[...]{brainlab}`.

**Режимы:** `twocolumnmode`, `shownumpages`, `darkheaders`, `nodefaultlogos`.

**Библиография:** `citingstyle=numbers|authoryear|super`, `bibliostyle=unsrtnat|plainnat|abbrvnat`, `bibfile=references`.

**Логотипы:** `logopath=logos/` — папка с файлами логотипов, со слэшем на конце.

**Рамки:** `boxrule=0.3pt`, `arc=2mm`.

**Отступы:** двенадцать отдельных ключей — `titleleftpad`, `titlerightpad`, `titletopad`, `titlebottompad` и такие же с префиксами `table` и `algor`. Ключ `padding=30pt` задаёт все двенадцать сразу и перекрывает индивидуальные значения, поэтому одновременно их использовать бессмысленно.

## Мета-информация

```latex
\setbrainmeta{
  title={...}, authors={...}, affiliations={...}, abstract={...},
  keywords={...},                             % только в метаданные PDF
  additionallogos={innopolis.pdf,mipt.pdf},   % имена С расширением, из папки logopath
}
```

`title`, `authors` и `keywords` автоматически попадают в метаданные PDF (Title, Author, Keywords). Надстрочные номера и `\\` из списка авторов при этом выкидываются. Если нужно иначе, после `\setbrainmeta` напишите `\hypersetup{pdfauthor={...}}`.

**Равный вклад и контакты.** `\footnote` и `\thanks` в титульнике не работают, поэтому звёздочку ставьте через `\textsuperscript{1,*}`, а расшифровку и почту пишите отдельной строкой в `affiliations` (пример в `demo.tex`).

Дополнительные логотипы удобнее всего готовить так: взять `.svg`, открыть в Figma, перекрасить, сохранить `.png`, затем онлайн-конвертером сделать `.pdf`.

## Окружения

```latex
\begin{mainpart} ... \end{mainpart}          % титульник + текст + библиография
\begin{appendixpart} ... \end{appendixpart}  % приложение (в двухколоночном режиме — одна колонка)
```

**Таблицы.** Ширина — необязательный аргумент в фигурных скобках после `[placement]`:

```latex
\begin{table}[ht] ... \end{table}                  % ширина = \columnwidth
\begin{table}[ht]{0.7\columnwidth} ... \end{table}
\begin{table*}[t] ... \end{table*}                 % ширина = \textwidth
```

Единственное ограничение: тело таблицы не должно начинаться с группы в фигурных скобках, иначе она будет прочитана как ширина. Начинайте с `\centering`.

Текст в таблицах набирается `\small`. Вернуть обычный размер: `\renewcommand{\braintablefont}{\normalsize}`.

Если таблица всё равно шире колонки (в логе `Overfull \hbox`, подсветка упирается в рамку), то по порядку: `\setlength{\tabcolsep}{4pt}` внутри таблицы, `table*` на всю ширину страницы, и только в крайнем случае `\resizebox{\linewidth}{!}{\begin{tabular}...\end{tabular}}` — он уменьшает и шрифт.

**Алгоритмы.** Тоже принимают ширину необязательно:

```latex
\begin{algorithm}{Projected Gradient Descent} ... \end{algorithm}
\begin{algorithm}{0.8\columnwidth}{Название} ... \end{algorithm}
```

Опциональный аргумент в квадратных скобках — это ключи `tcolorbox`, а не `[htbp]`: алгоритм не является плавающим объектом.

**Теоремы.** Доступны `theorem`, `lemma`, `proposition`, `corollary`, `definition`, `assumption`, `remark`. Сигнатура — `[название][ширина]`:

```latex
\begin{theorem}[Cauchy--Schwarz] ... \end{theorem}
\begin{theorem}[Cauchy--Schwarz][0.8\columnwidth] ... \end{theorem}
```

Все боксы разрываются между колонками и страницами, `\verb` и `verbatim` внутри работают.

**Рисунки** — стандартный `figure` / `figure*`, без рамки. Подрисунки (a), (b) — через `subfigure` из пакета `subcaption`, пример в `demo.tex`.

**Доказательства** — стандартное окружение `proof` из `amsthm`. Ссылку в заголовке раздела пишите как `\texorpdfstring{Proof of \Cref*{thm:x}}{Proof of Theorem 1}`: звёздочка убирает гиперссылку, второй аргумент идёт в закладки PDF.

**Подсветка в таблицах:** `\highlightrow` ставится в самом начале строки, `\highlightcell` — перед содержимым ячейки.

## Сокращения из `shortcuts.sty`

Множества `\R \N \Z \Q \Ss \Rd`, каллиграфические `\cX \cD \cL` и т. д.

```latex
\expect{X}              % E[X]
\expect_{x\sim p}{X}    % E_{x~p}[X]
\expect{X | Y}          % E[X | Y]
\trans(A+B)             % (A+B)^T
\trans*(A)  \trans*{A}  % A^T
\funcf^2_i(x)           % f^2_i(x); также \g и \h
\norm{x} \abs{x} \set{a,b} \setof{x}{x>0} \qty{a}
\dv{y}{x} \pdv{f}{x} \pdvmix{f}{x}{y} \grad{f} \hess{f}
\argmin \argmax         % индекс снизу
\Var \diag \trace \rank % индекс справа внизу
```

## Загрузка на arXiv

1. Соберите статью локально (`latexmk -pdf demo.tex` или на Overleaf) и убедитесь, что в логе нет ошибок.
2. В архив положите: главный `.tex`, `brainlab.sty`, `shortcuts.sty`, папку `logos/` и все рисунки, **и файл `.bbl`**. arXiv не запускает bibtex сам, поэтому без `.bbl` список литературы будет пустым. Имя `.bbl` должно совпадать с именем главного `.tex` (`demo.tex` → `demo.bbl`). На Overleaf `.bbl` берётся в Logs and output files → Other logs and files.
3. `references.bib`, `.aux`, `.log`, `.pdf`, `NeurIPS-logo.svg`, `.DS_Store` не нужны — лучше удалить, иначе arXiv может выложить их в открытый доступ вместе с исходниками. Закомментированный текст в `.tex` тоже будет виден всем.
4. Первая строка `demo.tex` — `\pdfoutput=1`. Не удаляйте её: по ней arXiv понимает, что собирать надо через pdfLaTeX.
5. После загрузки откройте PDF, который собрал arXiv: проверьте список литературы и что вертикальный штамп слева не наезжает на текст.

Архив можно собрать так (после локальной сборки):

```bash
zip -r arxiv.zip demo.tex demo.bbl brainlab.sty shortcuts.sty logos -x "*.svg" -x "*.DS_Store"
```

## Известные особенности

- Подключены `microtype` (меньше переполненных строк в узких колонках) и `subcaption`. Повторно подключать их в документе не нужно.
- `\cite` переопределён на `\citep`. Для ссылки в тексте используйте `\citet`.
- Кодировка по умолчанию — T1, T2A подключена дополнительно. Если пишете основной текст по-русски, добавьте `russian` в `babel`, иначе не будет переносов.
- Поля страницы — 1 дюйм по бокам, 0.8 дюйма сверху и снизу. Меньше по бокам делать не стоит: arXiv ставит вертикальный штамп в левое поле, и при узком поле он наезжает на текст.
- `\g` и `\h` занимают короткие имена. Если подключаете пакет, который их использует, переименуйте в `shortcuts.sty`.
