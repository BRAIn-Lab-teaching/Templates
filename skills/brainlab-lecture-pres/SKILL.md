---
name: brainlab-lecture-pres
description: Сверстать или переоформить лекционную beamer-презентацию в стилевике лекций BrainLab (Presentation_Lecture — pres.sty + shortcuts.sty, venue=fpmi|innopolis|isp). Источник — чужой beamer-.tex с любой темой (Madrid, metropolis, свой стиль), PDF или .pptx слайдов, конспект, markdown или просто текст и формулы. Используй всегда, когда просят слайды к лекции или учебному курсу, «лекционный шаблон», «в стиле ФПМИ / Иннополиса / ИСП», pres.sty, переделать слайды лекции под BrainLab — даже если стилевик не назван. Не для докладов и выступлений (brainpres.sty, скилл brainlab-pres), не для .pptx (brainlab-presentation), не для статей и постеров (brainlab-article, brainlab-poster).
---

# Лекция в стилевике BrainLab (pres.sty)

Задача: получить собирающийся PDF лекционных слайдов в шаблоне `Presentation_Lecture`, не потеряв содержание. Текст, формулы, числа и формулировки теорем переносить как есть — менять оформление и разметку, а не смысл.

У BrainLab два beamer-шаблона. `Presentation_Lecture` (этот скилл) — для лекций и семинаров: 4:3, навигация разделов сверху, теоремы, алгоритмы, `pdflatex`. `Presentation_BrainLab` (`brainpres.sty`, скилл `brainlab-pres`) — для докладов и выступлений: 16:9, XeLaTeX, декор. Просят «доклад», «выступление на конференции» — это `brainlab-pres`; неясно, лекция это или доклад, — спросить.

## 0. Где взять шаблон

Файлы шаблона **копировать, никогда не набирать по памяти**:
1. Папка `Templates/Presentation_Lecture` у пользователя (обычно `~/edu_lab_github/Templates/Presentation_Lecture`).
2. Иначе `git clone https://github.com/BRAIn-Lab-teaching/Templates` → `Templates/Presentation_Lecture`.
3. Если ничего недоступно — попросить пользователя подключить папку или приложить файлы.

Нужны: `pres.sty`, `shortcuts.sty`, `logos/`, а `main.tex` и `README.md` — как основа и справка. Перед работой прочитать актуальные `README.md` и `pres.sty`: если стилевик обновился, они главнее этого скилла.

## 1. Подготовка

- Исходники пользователя не трогать. Создать новую папку `<имя>_lecture/`, скопировать туда файлы шаблона (`logos/` — обязательно рядом с главным файлом, путь к логотипу относительный), рисунки и `.bib`.
- Определить источник:
  - **beamer-.tex** — основной случай, переносить покадрово (разделы 2–5).
  - **.pptx** — текст и картинки извлечь средствами скилла `pptx` (или `python-pptx`), картинки сохранить в `figures/`. Формулы из pptx обычно картинки или OMML — набрать в LaTeX заново, сверяя с оригиналом.
  - **PDF слайдов** — текст через `pdftotext -layout`, рисунки вырезать векторно: `\includegraphics[page=N, trim=l b r t, clip]{slides.pdf}` (отступы в bp; найти по рендеру `pdftoppm -r 72`, 1 px = 1 bp).
  - **Конспект / markdown / текст** — разбить на кадры самому (см. раздел 6).
- Главный файл начинать с копии `main.tex`, пример-кадры заменить.
- Выяснить venue и язык. Если пользователь не сказал — `venue=fpmi`, язык по тексту слайдов (`lang=ru` для русского), `navsymbols=hide`; в конце сказать, что это переключается одной опцией.

## 2. Преамбула

```latex
\documentclass[aspectratio=43,11pt]{beamer}   % 16:9 исходника — aspectratio=169, работает
\usepackage[venue=fpmi,lang=ru,navsymbols=hide]{pres}

\title[Лекция 5]{Негладкая оптимизация. Проксимальный метод}  % [короткое] — в колонтитул
\subtitle{Методы оптимизации}                                 % название курса
\author[И. Фамилия]{Имя Фамилия}
\date{20 марта 2024}
```

Ещё опции: `braces=smart|physics` (умные скобки у `\qty`/`\norm`/`\scalar`, по умолчанию `smart`), `plots=on|off` (`pgfplots` + `tikz-3dplot`; `off` — если графиков нет, сборка быстрее), `braket=on|off` (пакет `braket`). Неизвестная опция — ошибка компиляции (так задумано). `\institute` и `\titlegraphic` (логотип) ставит сам стилевик по `venue` — из исходника их удалить. Дополнительные логотипы на титуле — `\AddLogo{logos/x.png}` (или `\AddLogo[height=1cm]{…}`) после `\usepackage{pres}`, полностью свой набор — `\ClearLogos` и затем `\AddLogo`. Если организации автора нет среди venue — спросить пользователя; можно переопределить `\institute{...}` после `\usepackage{pres}`.

Старые презентации под любую прежнюю версию `pres.sty` (в том числе `pres-2.sty`) достаточно собрать с новыми `pres.sty` и `shortcuts.sty` — переписывать их не нужно.

**Удалить из исходника** — стилевик это уже задаёт или грузит:
- оформление: `\usetheme`, `\usecolortheme`, `\usefonttheme`, `\useinnertheme`, `\useoutertheme`, свои `\setbeamercolor`/`\setbeamertemplate`/`\setbeamerfont` для цветов, шапки, колонтитула, блоков; `\logo`, `\definecolor` фирменных цветов прошлого шаблона;
- пакеты: `inputenc`, `fontenc`, `babel`, `amsmath/amssymb/amsthm/amsfonts`, `mathtools`, `physics`, `xcolor`, `graphicx`, `tikz`, `tcolorbox`, `hyperref`, `url`, `multicol`, `multirow`, `tabularx`, `makecell`, `wrapfig`, `subfigure`, `algorithm`, `algpseudocode`, `etoolbox`, `ulem`, `pifont`, `svg`, `units`, `braket`, `pgfplots` и `\pgfplotsset{compat=…}`, `tikz-3dplot`, `dsfont`. Библиотеки TikZ `positioning, calc, automata, arrows.meta, intersections, decorations.markings, patterns, patterns.meta` и pgfplots-библиотека `fillbetween` уже подключены — остальные (`shapes`, `fit`, `decorations.pathreplacing`…) оставить.

**Несовместимое — конвертировать:**
- **XeLaTeX/LuaLaTeX и `fontspec`** — убрать: стилевик рассчитан на `pdflatex` (T2A + inputenc). Под XeLaTeX кириллица молча пропадает из PDF (в логе только `Missing character`).
- `metropolis`/`mtheme` и прочие темы — их команды (`\metroset`, `[standout]` у кадра) удалить, `standout`-кадр → обычный кадр с `\centering\Large\alert{…}`.
- `subfig` (`\subfloat`) → уже загруженный `\subfigure[подпись]{…}` или `columns`.
- `algorithmic` капсом (`\STATE`, `\FOR`, `\ENDFOR`, `\IF`, `\ENDIF`, `\REQUIRE`, `\RETURN`) и `algorithm2e` (`\KwIn`, `\KwOut`, `\For{c}{body}`, `\;`) → `algpseudocode` (`\State`, `\For … \EndFor`, `\If … \EndIf`, `\Require`, `\Ensure`, `\State \Return`).
- `amsxtra` и `pstricks` не подключать (см. «Известные особенности» в README).

**Макросы автора** оставить, но разрулить конфликты. `pres` грузит `physics` (`\qty \norm \abs \dv \pdv \grad \div \curl \Tr \tr \Re \Im \order \comm \bra \ket \va \vb \vu \dd \vdot`), `braket` (`\bra \ket \braket \set \Set \Braket`; `\braket` понимает и `{a|b}`, и `{a}{b}`) и `shortcuts.sty` (`\R \N \Z \Q \Rd \cA…\cZ \mA…\mZ \vc…\vz \e \eps \EE \expect \PP \scalar \dotprod \argmin \argmax \Var \sign \dist \f \g \h`), сам определяет `\Exp \eqdef \ve \< \minleft \minright`. На `Command \X already defined`: смысл тот же — удалить определение автора; иначе — `\renewcommand` (для `\DeclareMathOperator` сначала `\let\X\relax`). Определения `\norm`/`\abs` автора через `\left\| … \right\|` почти всегда совпадают с `physics` — удалить.

**Английская лекция:** `lang=en` меняет только названия теорем, алгоритмов и подписей; главный язык babel остаётся русским. Добавить `\AtBeginDocument{\selectlanguage{english}}` в преамбулу, чтобы переносы шли по английским правилам.

## 3. Структура и навигация

- Верхняя панель показывает **разделы** (`\section`) и точку на каждый кадр; `\subsection` не показывается, но не мешает. Без `\section` панель пустая — разметить лекцию на 3–6 разделов, если в исходнике их нет.
- Титул — `\begin{frame}\titlepage\end{frame}`; свои титульные кадры из старой темы заменить им.
- Кадры с оглавлением (`\tableofcontents[currentsection]` в `\AtBeginSection`) можно оставить.
- Оверлеи (`\pause`, `<+->`, `\only`, `\uncover`), `columns`, `[fragile]` для `verbatim`/`lstlisting` — переносить без изменений.

## 4. Окружения

**Теоремы.** В стилевике есть `thm` (Теорема/Theorem), `lem` (Лемма/Lemma), `defn` (Определение/Definition), `prop` (Утверждение/Proposition) и `proof` — без нумерации, названия по `lang`:

```latex
\begin{thm}[Нестеров] ... \end{thm}
\begin{proof} ... \end{proof}           % квадратик в конце
```

Встроенные окружения beamer `theorem`, `lemma`, `definition`, `corollary`, `example` тоже собираются, **но печатают английское название даже при `lang=ru`** — поэтому `theorem→thm`, `lemma→lem`, `definition→defn`, `proposition→prop`. Остальным (следствие, предположение, замечание, пример) объявить своё ненумерованное окружение в преамбуле:

```latex
\newtheorem*{cor}{Следствие}      % lang=en: Corollary
\newtheorem*{asm}{Предположение}  % Assumption
\newtheorem*{rem}{Замечание}      % Remark
```

Свои `\newtheorem{theorem}…` из исходника удалить (конфликт `Command \theorem already defined`). Нумерации нет намеренно; ссылки вида «по теореме 2» в тексте слайда заменить на название («по теореме Нестерова»), а не придумывать номер.

**Длинное доказательство** на несколько кадров: в первом `\proofhead` (или `\proofhead[Набросок]`) вместо `\begin{proof}`, в последнем `\proofqed` вместо `\end{proof}`.

**Блоки** `block`, `alertblock`, `exampleblock` и `tcolorbox` (стиль `presbox` уже применён) — оставить, цвета подставятся сами. Опции цвета у `tcolorbox` (`colback=…`, `colframe=…`) из старой темы убрать.

**Алгоритмы** — плавающий `algorithm` с `[H]`, подпись без номера (так задумано):

```latex
\begin{algorithm}[H]
  \caption{Субградиентный метод}
  \begin{algorithmic}[1]
    \Require шаг $\gamma > 0$
    \State $w^{k+1} = w^k - \gamma g^k$
    \Ensure $w^K$
  \end{algorithmic}
\end{algorithm}
```

`\AlgInput{…}` / `\AlgOutput{…}` — «Вход/Выход» строкой без номера (по `lang`); удобно для `\KwIn`/`\KwOut` из `algorithm2e`.

**Рисунки и таблицы** — `figure`/`table` с `\caption` нумеруются («Рис. 1»), `\ref` работает. Ширина — `\linewidth` (в `columns` это ширина колонки).

**Цвета.** Жёсткие цвета исходника заменить на роли, иначе при смене venue они разъедутся с палитрой:
- `\textcolor{red}{…}`, `{\color{blue} …}` для выделения → `\alert{…}`;
- пометки «верно/неверно» → `\cmark` / `\xmark`, мелкие замечания → `\oldstuff{}` / `\redstuff{}`;
- в TikZ: узлы `presnode`, стрелки `presedge`, цвета `primary`, `secondary`, `accent`, `surface`, `ink`; для двух-трёх серий на графике — `primary`, `secondary`, `accent`. Сырые `berry`, `apricot` не использовать.

**Ссылки и источники.** Ссылка на статью/материалы — `\pdflink{Название}{URL}` последней строкой кадра (сама прижимается вниз). Источник картинки или цитаты — `\blfootnote{…}`. Библиографию исходника (`thebibliography`, `\bibliography`) оставить как есть.

## 5. Содержание кадров

- Из beamer-исходника кадры переносить один к одному, текст не сокращать и не переписывать.
- Из конспекта или текста — одна мысль на кадр: заголовок-утверждение, 3–6 пунктов или одна-две ключевые формулы. Доказательство — отдельными кадрами после формулировки.
- Кадр не влезает (в логе `Overfull \vbox … detected at line N` — это номер строки `\end{frame}` переполненного кадра): разбить на два кадра с тем же заголовком (второй — с пометкой «(продолжение)» или через `\proofhead`/`\proofqed`), разбить длинную формулу на `align`/`multline`, уменьшить картинку. `\small`/`\footnotesize` для целого кадра — только если переполнение пара строк; `\tiny` и `allowframebreaks` не использовать: первое нечитаемо из аудитории, второе ломает навигацию.

## 6. Сборка и проверка

1. `latexmk -pdf -interaction=nonstopmode main.tex` или `pdflatex` **дважды** (+ `bibtex` при `.bib`): верхняя панель строится по `.nav`, после одного прохода она пустая. Нужен TeX Live с `cm-super` и `lh` (кириллица T2A); без них текст молча пропадает. Если TeX не установлен — собирать у пользователя или на Overleaf (pdfLaTeX), не подменяя стилевик. TeX Live — 2026 (минимум 2025); на Overleaf проверить Menu → Settings → TeX Live version: на 2020 (Legacy) стилевик не собирается, а в старых проектах это частая настройка — сказать об этом пользователю.
2. Лог:
   - 0 строк `^!`;
   - нет `Overfull \vbox` (переполненные кадры — см. раздел 5) и `Overfull \hbox` больше ~5pt;
   - нет `Reference … undefined` / `Citation … undefined`;
3. Отрендерить (`pdftoppm -r 50 -png main.pdf p`) и посмотреть глазами:
   - титул: название на абрикосовой плашке (fpmi), логотип, автор, дата;
   - шапка заполнена названиями разделов; заголовки и подзаголовки кадров читаются;
   - ничего не заходит под нижний колонтитул и не вылезает за правый край;
   - формулы и `\cmark`/`\xmark` на месте, на кадрах нет квадратиков вместо символов.
4. Сверить с исходником, что ничего не потерялось: число `\begin{frame}`, `\section`, рисунков, теорем.

## 7. Результат

В `<имя>_lecture/`: главный `.tex`, `pres.sty`, `shortcuts.sty`, `logos/`, рисунки, `.bib` при наличии, собранный PDF. PDF отправить пользователю. В ответе коротко: venue и язык, что пришлось поменять нетривиально (переименованные макросы, окружения теорем, сконвертированные алгоритмы, разбитые кадры, убранные цвета старой темы) и что проверить руками.
