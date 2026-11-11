---
name: brainlab-article
description: Перегнать произвольную LaTeX-статью (NeurIPS, ICML, ICLR, IEEE, ACM, LNCS, elsarticle, arXiv и т.п.) в стилевик статьи BrainLab (brainlab.sty + shortcuts.sty).
---

# Перевод LaTeX-статьи в стилевик BrainLab

Задача: взять исходники чужой статьи (любой класс/стиль конференции) и получить собирающийся проект в шаблоне статьи BrainLab, не потеряв содержание. Текст статьи не переписываем — меняем только оформление и разметку.

## 0. Где взять шаблон

Файлы шаблона **копировать, никогда не набирать по памяти**:
1. Папка `Templates/Article` у пользователя (обычно `~/edu_lab_github/Templates/Article`; если подключена — брать оттуда через device-shell).
2. Иначе `git clone https://github.com/BRAIn-Lab-teaching/Templates` → `Templates/Article`.
3. Если ничего недоступно — попросить пользователя подключить папку или приложить файлы.

Нужны: `brainlab.sty`, `shortcuts.sty`, `logos/` (без `NeurIPS-logo.svg`), для справки `demo.tex` и `README.md`. Перед работой прочитать актуальные `README.md` и `demo.tex` — если стилевик обновился, они главнее этого скилла.

## 1. Подготовка

- Исходник не трогать. Создать рядом новую папку `<имя>_brainlab/`, скопировать туда все исходники статьи (рисунки, .bib/.bbl, подфайлы `\input`) и файлы шаблона.
- Найти главный .tex (тот, где `\documentclass`), собрать список `\input/\include`.
- Определить: класс/стиль (neurips_*, icml*, iclr*, IEEEtran, acmart, llncs, elsarticle, revtex, amsart, article…), язык, одна или две колонки, natbib/biblatex/thebibliography, какие пакеты алгоритмов.
- Режим колонок: если пользователь не сказал — `twocolumnmode` (как в `demo.tex`), в конце сказать, что переключается одной строкой.

## 2. Преамбула

Новая шапка главного файла:

```latex
\pdfoutput=1
\documentclass[11pt]{article}
\usepackage[
  twocolumnmode,
  citingstyle=numbers,      % authoryear, если в исходнике author-year (ICLR/ICML/ACL)
  bibliostyle=unsrtnat,     % plainnat/abbrvnat при authoryear
  bibfile=references,       % имя .bib БЕЗ расширения
]{brainlab}
\usepackage{shortcuts}
```

**Удалить** (brainlab уже грузит или они конфликтуют): стилевые файлы конференций (`neurips_20xx`, `icml20xx`, `iclr20xx_conference`, `aaai`, `acl`…), `geometry`, `hyperref`, `natbib`, `cleveref`, `amsmath/amssymb/amsthm`, `graphicx`, `float`, `booktabs`, `array`, `colortbl`, `xcolor`, `caption`, `subcaption`, `microtype`, `fontenc`, `babel` (см. ниже про русский), `authblk`, `titlesec`, `fancyhdr`, `multicol`, `tcolorbox`, `varwidth`, `algorithm`, `algpseudocode`, `times`-подобные шрифтовые хаки конференций.

**Несовместимые — конвертировать:**
- `subfig`/`subfigure` → `subcaption` (`\subfloat[cap]{…}` → `\begin{subfigure}[b]{0.48\columnwidth}…\caption{cap}\end{subfigure}`).
- `algorithmic` (капсом `\STATE`, `\FOR`, `\ENDFOR`, `\IF`, `\ELSE`, `\ENDIF`, `\WHILE`, `\REQUIRE`, `\ENSURE`, `\RETURN`, `\COMMENT`) → `algpseudocode` (`\State`, `\For`, `\EndFor`, `\If`, `\Else`, `\EndIf`, `\While`, `\EndWhile`, `\Require`, `\Ensure`, `\State \Return`, `\Comment`).
- `algorithm2e` → `algpseudocode`: `\KwIn{}`→`\Require`, `\KwOut{}`→`\Ensure`, `\For{c}{body}`→`\For{c} body \EndFor`, `\eIf{c}{a}{b}`→`\If{c} a \Else b \EndIf`, убрать `\;` в концах строк.
- `biblatex` → natbib: `\addbibresource{x.bib}` → `bibfile=x`, удалить `\printbibliography`, `\textcite`→`\citet`, `\parencite`/`\autocite`→`\citep`.

Остальные пакеты оставить. Если пакет грузился с опциями, которые конфликтуют с загрузкой из brainlab (option clash) — `\PassOptionsToPackage{…}{pkg}` до `\usepackage{brainlab}` или убрать опции.

**Свои макросы автора** оставить, но разрулить конфликты с `shortcuts.sty`. Частые пересечения: `\R \N \Z \Q \E \eps \norm \abs \set \qty \dv \pdv \grad \hess \trans \argmin \argmax \Var \Cov \diag \sign \rank \Tr \cX \cD \cL…`, а также короткие `\g`, `\h`. На ошибку `Command \X already defined`: если смысл тот же — удалить определение автора; если отличается — `\renewcommand` (для `\DeclareMathOperator` — сначала `\let\X\relax`). Если исходник грузит `physics` или `braket` — `shortcuts.sty` не подключать вообще.

**Русский текст:** `\PassOptionsToPackage{russian}{babel}` перед brainlab и `\AtBeginDocument{\selectlanguage{russian}}` (T2A в brainlab уже есть). Проверить переносы в собранном PDF.

## 3. Титульник

`\title/\author/\maketitle/abstract/keywords` любого формата перенести в `\setbrainmeta` (после преамбулы, до `\begin{document}`):

```latex
\setbrainmeta{
  title={...},
  authors={Jane Doe\textsuperscript{1,*}, John Smith\textsuperscript{2}},
  affiliations={
    \textsuperscript{1}Org One \\
    \textsuperscript{2}Org Two \\[0.3em]
    {\small \textsuperscript{*}Equal contribution. Correspondence to: \href{mailto:a@b.c}{a@b.c}}
  },
  keywords={...},   % только в метаданные PDF
  abstract={...},   % текст из environment abstract
}
```

- `\footnote`/`\thanks` в титульнике не работают → всё в строку `affiliations` через `\textsuperscript`.
- Разобрать форматы: NeurIPS (`\And`, `\AND`, `\texttt{email}` в `\author`), ICML (`\icmltitle`, `\icmlauthor`, `\icmlaffiliation`, `\icmlcorrespondingauthor`, `\icmlkeywords`, `\printAffiliationsAndNotice`), IEEE (`\IEEEauthorblockN/A`, `\IEEEkeywords`, `\IEEEPARstart`→обычный текст), ACM (`\affiliation{\institution}`, `\email`, CCS concepts, `\keywords`, teaser → обычный первый `figure*`), LNCS (`\inst`, `\institute`, `\email`, `\titlerunning`), elsarticle (`frontmatter`, `\author[1]`, `\affiliation`). Одинаковые организации объединить под одним номером.
- Удалить: `\maketitle`, копирайты, `\acmConference`, `\setcopyright`, `\icmlsetsymbol`, служебные `\vskip`/отрицательные `\vspace`, `\linenumbers`.
- Логотипы: по умолчанию стоят МФТИ/ИСП/Иннополис/BRAIn. Если авторы не из этих организаций — спросить; без ответа оставить дефолт и упомянуть `nodefaultlogos` и `additionallogos={file.pdf,...}` (имена с расширением, файлы в `logos/`).

## 4. Тело документа

Структура:

```latex
\begin{document}
\begin{mainpart}
  ... основной текст, благодарности ...
\end{mainpart}       % здесь сама печатается библиография
\begin{appendixpart}
  ... всё, что было после \appendix ...
\end{appendixpart}
\end{document}
```

- `\bibliographystyle{}` и `\bibliography{}` удалить — их вызывает `mainpart`. Несколько .bib → слить в один файл. Если библиография стояла после приложения — она переедет перед ним, это нормально.
- **Только .bbl (частый случай у arXiv-исходников):** переименовать в `<главный>.bbl`, bibtex не запускать — `\bibliography` его подхватит. Работает, если .bbl natbib-совместимый; если он от biblatex — восстанавливать .bib или конвертировать `thebibliography`.
- **`thebibliography` внутри .tex:** перевести записи в .bib, сохранив ключи `\bibitem`.
- `\cite` в шаблоне = `\citep`. При `numbers` ничего не менять. При `authoryear` проверить места, где `\cite` используется как подлежащее ("\cite{x} showed") → `\citet`.
- NeurIPS checklist / broader impact — перенести в `appendixpart`, не выкидывать молча; в конце сказать пользователю.

**Теоремы.** Определения `\newtheorem{theorem}…` для `theorem, lemma, proposition, corollary, definition, assumption, remark` удалить — они уже есть как боксы. Прочие (`claim`, `example`, `conjecture`, `fact`…) объявить в преамбуле: `\DeclareBrainTcbTheorem{claim}{Claim}` (вместо `\newtheorem`). Сигнатура `\begin{theorem}[Название]\label{…}`; второй необязательный аргумент — ширина. Длинные названия теорем и алгоритмов не сокращать: заголовок бокса сам переносится по ширине бокса. Общая нумерация (`\newtheorem{lemma}[theorem]`) теряется — у каждого окружения свой счётчик; упомянуть, если важно. `proof` стандартный, оставить.

**Таблицы.** Остаются `table`/`table*`, но тело должно начинаться с `\centering` (не с `{…}`, иначе прочитается как ширина). Ширина — `\begin{table}[t]{0.7\columnwidth}`. `\resizebox`, `\small`, `\scriptsize` перед tabular можно убрать (шрифт уже `\small`); если таблица шире колонки: `\setlength{\tabcolsep}{4pt}` → `table*` → в крайнем случае `\resizebox{\linewidth}{!}{…}`. Выделение лучших результатов можно (не обязательно) делать `\highlightcell`/`\highlightrow`.

**Алгоритмы.** Не плавающие, `[t]` и `\caption` убрать — опциональный аргумент это ключи tcolorbox:

```latex
% было: \begin{algorithm}[t]\caption{PGD}\label{alg:pgd}\begin{algorithmic}...
\begin{algorithm}{PGD}\label{alg:pgd}
\begin{algorithmic}[1] ... \end{algorithmic}
\end{algorithm}
```
`algorithm*` → `\begin{algorithm}{\textwidth}{Название}` только в одноколоночном режиме; в двухколоночном — обычный (бокс разрывается между колонками).

**Рисунки.** `figure`/`figure*` без изменений. В двухколоночном режиме ширины `\textwidth` внутри обычного `figure` → `\linewidth`/`\columnwidth` или перевести в `figure*`. `wrapfigure` → обычный `figure`. Пути `\graphicspath` проверить.

**Формулы.** В двух колонках широкие `equation`/`align` переносить (`multline`, `split`, разбивка строк), не трогая смысл.

**Заголовки в приложении** со ссылкой: `\section{\texorpdfstring{Proof of \Cref*{thm:x}}{Proof of Theorem 1}}`.

Остальную разметку (`\ref`, `\eqref`, `\cref`, макросы в тексте) не трогать.

## 5. Сборка и проверка

1. `latexmk -pdf -interaction=nonstopmode main.tex` (или pdflatex → bibtex → pdflatex ×2; при одном .bbl — pdflatex ×2). Нужен полноценный TeX Live (cyrillic/T2A, cm-super/lm). Если в окружении его нет — собирать там, где есть (у пользователя локально/Overleaf), не подменяя стилевик. TeX Live — 2026 (минимум 2025); на Overleaf проверить Menu → Settings → TeX Live version: на 2020 (Legacy) стилевик не собирается, а в старых проектах это частая настройка — сказать об этом пользователю.
2. В логе: 0 ошибок `^!`; нет `Citation … undefined` и `Reference … undefined`; `Overfull \hbox` больше ~5pt — чинить (таблицы, формулы, URL).
3. Отрендерить страницы (`pdftoppm -r 60 -png`) и посмотреть глазами: титульник (авторы, аффилиации, абстракт), таблицы не вылезают из рамок, заголовки боксов теорем/алгоритмов не вылезают за рамку, приложение начинается с плашки Appendix.
4. Сверить, что ничего не потерялось: число `\section`, `figure`, `table`, `\begin{theorem…}` и записей библиографии как в исходнике.

## 6. Результат

В `<имя>_brainlab/`: главный `.tex`, `brainlab.sty`, `shortcuts.sty`, `logos/`, рисунки, `.bib` (или `.bbl`), собранный PDF. PDF отправить пользователю. В ответе коротко: что пришлось поменять нетривиально (переименованные макросы, сконвертированные алгоритмы, общая нумерация теорем, логотипы, перенесённый checklist) и что осталось проверить руками. Для arXiv — сослаться на раздел «Загрузка на arXiv» в README шаблона.
