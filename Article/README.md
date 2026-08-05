# BrainLab LaTeX template

Шаблон статьи лаборатории. Компилируется `pdflatex` + `bibtex` (на Overleaf — настройки по умолчанию). [Ссылка на шаблон в Overleaf](https://www.overleaf.com/read/ctmzkhnmckpw#e2be80)

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
  additionallogos={innopolis.pdf,mipt.pdf},   % имена С расширением, из папки logopath
}
```

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

**Рисунки** — стандартный `figure` / `figure*`, без рамки.

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

## Известные особенности

- `\cite` переопределён на `\citep`. Для ссылки в тексте используйте `\citet`.
- Кодировка по умолчанию — T1, T2A подключена дополнительно. Если пишете основной текст по-русски, добавьте `russian` в `babel`, иначе не будет переносов.
- Поля страницы — 0.5 дюйма по бокам. Некоторые площадки такое не принимают, проверяйте требования конференции.
- `\g` и `\h` занимают короткие имена. Если подключаете пакет, который их использует, переименуйте в `shortcuts.sty`.
