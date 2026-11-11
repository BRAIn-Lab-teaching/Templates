---
name: brainlab-pres
description: Сверстать презентацию для доклада в LaTeX-теме beamer BrainLab (brainpres.sty, папка Presentation_BrainLab) — из статьи (LaTeX-исходники, arXiv, PDF), из чужой beamer-презентации (Madrid, metropolis, pres.sty из Presentation_Lecture и т. п.), из .pptx/PDF со слайдами или из текста и картинок пользователя. Используй всегда, когда просят слайды/доклад/презентацию «в LaTeX», «в beamer», «в нашей теме», «в стиле BrainLab» для семинара, конференции или публичного выступления, даже если тема не названа. Не для .pptx-файлов (brainlab-presentation), не для постеров (brainlab-poster) и не для статей (brainlab-article).
---

# Презентация в beamer-теме BrainLab

Задача: получить собирающийся PDF-доклад в теме BrainLab, который можно сразу показывать. Содержание берётся только из материалов пользователя — числа, результаты, цитаты, формулировки теорем не выдумывать и не «улучшать».

## 0. Где взять шаблон

Файлы шаблона **копировать, никогда не набирать по памяти**:
1. Папка `Templates/Presentation_BrainLab` у пользователя (обычно `~/edu_lab_github/Templates/Presentation_BrainLab`).
2. Иначе `git clone https://github.com/BRAIn-Lab-teaching/Templates` → `Templates/Presentation_BrainLab`.
3. Если ничего недоступно — попросить пользователя подключить папку или приложить файлы.

Нужны: `brainpres.sty`, `shortcuts.sty`, `logos/`, `art/`, `latexmkrc`; `demo.tex` и `README.md` — как основа и справка. Перед работой прочитать актуальные `README.md` и `demo.tex`: если тема обновилась, они главнее этого скилла.

## 1. Подготовка

- Исходники пользователя не трогать. Создать новую папку `<имя>_talk/` и скопировать туда файлы шаблона, рисунки и `.bib`.
- Главный файл начинать с копии `demo.tex`: там готовы преамбула и примеры всех типов слайдов. Пример-контент заменить, структуру оставить.
- Если материал только в PDF — текст брать через `pdftotext -layout`, рисунки вырезать из PDF без потери векторности (раздел 6). Из `.pptx` — текст через `python-pptx` (или скилл pptx), картинки из `ppt/media/`.
- Выяснить, сколько минут доклад и на каком языке. Если не сказано — ориентироваться на 15–20 минут и язык материалов, и сказать об этом в конце.

## 2. Преамбула и сборка

```latex
% !TEX program = xelatex
\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[lang=ru]{brainpres}     % lang=ru|en, sectionframes=auto|off, font=...
\title[Короткое название для колонтитула]{Полное название}
\subtitle{Конференция / семинар}
\author{...}
\institute{BRAIn lab, МФТИ}
\date{...}
```

- **Собирать XeLaTeX** (`latexmk` подхватит `latexmkrc`; на Overleaf — Menu → Compiler → XeLaTeX). Под pdflatex тема соберётся, но с Lato вместо Montserrat — так не сдавать.
- Шрифт текста — Montserrat (`font=` меняет: `inter`, `nunito`, `roboto`, `sourcesans`, `arsenal`, `plex`, `fira`, `comfortaa`). Без просьбы пользователя не менять. Формулы всегда классические (Latin Modern Math).
- Не подключать заново то, что грузит тема: `fontspec`, `unicode-math`, `fontenc`, `inputenc`, `babel`, `amsmath/amssymb/amsthm/mathtools`, `physics`, `xcolor`, `graphicx`, `tikz`, `tcolorbox`, `booktabs`, `multirow`, `tabularx`, `algorithm/algpseudocode`, `pifont`, `hyperref`. Не задавать `\usetheme`, `\usecolortheme`, `\usefonttheme`, `\setbeamertemplate`, `\logo`, `\AtBeginSection` — всё это задаёт тема.
- Пакеты, несовместимые с `unicode-math`: `bm`, `mathptmx`, `newtxmath`, `txfonts`, `eulervm`, любые пакеты математических шрифтов — удалить из преамбулы. `\bm` и `\boldsymbol` тема уже определяет (жирный курсив), `\mathbb`, `\mathcal`, `\mathbf` работают как обычно.

## 3. Типы слайдов

```latex
\titleframe                                  % титул; \titleframe[арт] — другой декор
\begin{frame}{\contentsname}\tableofcontents\end{frame}   % план: 01, 02, 03
\section{Метод}                              % слайд раздела «02 Метод» появится сам
\begin{frame}{Заголовок}{Подзаголовок} ... \end{frame}    % обычный светлый слайд
\begin{frame}[dark]{Заголовок} ... \end{frame}            % то же на бордовом
\begin{frame}[c,dark]\statement[подпись]{Одна крупная мысль}\end{frame}
\imageframe{figures/photo.jpg}{Заголовок}{Текст справа}   % фото на левую половину
\quoteframe{Текст цитаты}{Автор}             % только настоящая цитата от пользователя
\finalframe{Спасибо за внимание!}{контакты}  % \finalframe[qr.png]{...}{...} — с QR справа
```

- **Арт** (декор из фирменного шаблона, ставится как есть): `network` (титул по умолчанию), `network-light`, `molecule`, `molecule-light`, `nodes` (разделы по умолчанию), `nodes-light`, `3d` (финал по умолчанию), `3d-light`, `3d-side`, `3d-blue`, `section-molecule`, `none`, `none-light`. Арт сам задаёт фон кадра (тёмный/светлый). Глобально: `\settitleart{...}`, `\setsectionart{...}`, `\setfinalart{...}`. Свой декор не рисовать и логотип не перерисовывать.
- **Карточки:** `\begin{card}{Заголовок}`, `cardgold`, `plaincard` (без заголовка); опции tcolorbox в `[]`, например `[height=4.6cm]` для выравнивания карточек в колонках. Стандартные `block` / `alertblock` / `exampleblock` и `thm`, `lem`, `defn` — те же карточки (бордовая / синяя / золотая полоса). Доказательство — `proof`; разорвать между слайдами — `\proofhead` … `\proofqed`.
- **Цифры:** `\statcard{87\%}{подпись}` — три-четыре в ряд через `columns` (`\column{0.31\textwidth}`). Только числа из материалов.
- **Колонки:** `\begin{columns}[T,onlytextwidth] \column{0.49\textwidth} ... \end{columns}`.
- **Списки:** `itemize` (точки-«узлы»), `enumerate` (номера в кружках). Не больше двух уровней.
- **Прочее:** `\pdflink{Подпись}{URL}` — ссылка с бейджем PDF, `\cmark` / `\xmark`, `\alert{...}` (синий акцент), цвета-роли `bltitle`, `bltext`, `blmuted`, `blaccent` — ими красить свой текст, не сырыми HEX: роли правильно меняются на тёмных слайдах.

## 4. Отбор содержания

Доклад — не статья: слушатель видит слайд 30–90 секунд и одновременно слушает.

- **Объём:** ~1 слайд на минуту доклада (15 минут → 12–16 слайдов, считая титул, план и разделы). Разделов 3–5.
- **Один слайд — одна мысль.** Заголовок слайда — по возможности утверждение («Метод сходится в 3 раза быстрее»), а не тема («Результаты»). До ~40 слов и до 5–6 пунктов на слайде; пункты — в одну-две строки.
- **Типичная структура:** титул → план → мотивация/постановка (1–2 слайда) → главная идея (`\statement` на тёмном) → метод (2–4 слайда: определение, теорема без доказательства, алгоритм/схема) → результаты (2–4 слайда: таблица, графики, `\statcard`) → выводы (`enumerate` из 3 пунктов) → финал с контактами.
- Из статьи выкидывать: related work (максимум один слайд), доказательства (только идея в 1–2 строки, если просят), второстепенные леммы, абляции, большую часть ссылок. Если существенное пришлось убрать — перечислить пользователю в конце.
- Формулы и теоремы переносить дословно, с нотацией источника. Макросы автора перенести в преамбулу, разрулив конфликты с `shortcuts.sty` и темой: заняты `\R \N \Z \Q \Rd \Ss \EE \ED \PP \VV \Exp \Var \norm \abs \set \argmin \argmax \dom \conv \dist \diam \sign \e \eps \f \g \h \ve \< \eqdef`, каллиграфические `\cA…\cZ`, матрицы `\mA…\mZ`, векторы `\vc…\vz`; `\va \vb \vu` — команды пакета `physics`. Совпадает по смыслу — использовать готовое, иначе переименовать макрос автора.
- `\quoteframe`, `\imageframe` с фото, `\statcard` ставить только если есть настоящий материал под них. Заглушки («Здесь может быть цитата») в итоговую презентацию не оставлять.

## 5. Перевод из чужой beamer-презентации

- Убрать `\usetheme`/`\usecolortheme`/`\usefonttheme`/`\useoutertheme`/`\useinnertheme`, `\setbeamercolor`/`\setbeamertemplate`/`\setbeamerfont`, `\logo`, `\titlegraphic`, `\AtBeginSection{...}` с ручными слайдами разделов, пакеты шрифтов.
- `\begin{frame}\titlepage\end{frame}` → `\titleframe`; ручной слайд «Спасибо/Вопросы» → `\finalframe`; ручной «Outline» с `\tableofcontents` оставить, заголовок — `\contentsname`.
- Блоки, теоремы, `columns`, `\pause`, `\only`, `\uncover`, `[fragile]` на обычных кадрах работают как есть. В спецкадрах (`\titleframe`, `\sectionframe`, `\imageframe`, `\quoteframe`, `\finalframe`) оверлеи не работают.
- Из `Presentation_Lecture` (`pres.sty`): `thm`, `lem`, `defn`, `proof`, `\proofhead`/`\proofqed`, `algorithm`, `\pdflink`, `\cmark`, `\xmark`, `\oldstuff`, `\redstuff`, `\blfootnote`, `\Exp`, `\eqdef`, `\ve`, `\<a,b>`, `presnode`/`presedge`, `\begin{tcolorbox}` переносятся без изменений. Опции `venue=…`, `navsymbols=…` убрать; `lang` оставить. Формат 4:3 (`aspectratio=43`) заменить на 16:9 и проверить, что слайды не переполнены.
- Цвета исходной темы (`primary`, `secondary`, `accent`, `structure`) заменить ролями `bltitle`, `blaccent`, `blnumber` и т. п.

## 6. Рисунки

- Картинки — `\includegraphics[width=\linewidth]{...}` внутри колонки или `\centering`; подпись — `figure` + `\caption` (нумеруется) или без подписи, если и так понятно.
- Рисунок из PDF статьи — вырезать прямо из PDF, он останется векторным: `\includegraphics[width=\linewidth, page=6, trim=105 553 106 69, clip]{paper.pdf}` (`trim` — отступы слева, снизу, справа, сверху в bp; найти по рендеру `pdftoppm -r 72`, 1 px = 1 bp). Сначала `pdfimages -list` — растровый рисунок останется растровым.
- На слайде шрифт подписей осей должен читаться из зала: рисунок из статьи давать на всю ширину слайда или половину, не ставить два мелких рядом. Если есть данные — лучше перерисовать график в `pgfplots` цветами `brainMaroon`, `brainBlue`, `brainGoldDark`. Данные — только из статьи/пользователя.
- SVG заранее перевести в PDF (`rsvg-convert -f pdf`): `\includesvg` без `--shell-escape` не работает.
- Схемы TikZ — стили `presnode` / `presedge` из темы.
- `\imageframe` обрезает картинку под левую половину (8 × 9 см) с сохранением пропорций — главное в кадре должно быть по центру картинки.

## 7. Сборка и проверка

1. `latexmk -interaction=nonstopmode talk.tex` (latexmkrc включает XeLaTeX; проходов нужно два — спецкадры позиционируются через `remember picture`). Нужен полноценный TeX Live (Montserrat, Latin Modern Math, Fira Mono, tcolorbox). TeX Live — 2026 (минимум 2025); на Overleaf проверить Menu → Settings → TeX Live version: на 2020 (Legacy) стилевик не собирается, а в старых проектах это частая настройка — сказать об этом пользователю.
2. Лог: 0 строк `^!`, нет `Missing character` (символ отсутствует в шрифте — заменить), нет `undefined` ссылок, нет `Overfull \hbox` больше ~5pt. Предупреждения `unicode-math` о переопределении команд — норма.
3. `pdffonts talk.pdf`: в колонке `emb` везде `yes`.
4. Отрендерить все слайды (`pdftoppm -r 50 -png`, собрать в лист) и посмотреть глазами. **beamer молча обрезает переполненный слайд** — лог об этом часто молчит, поэтому проверять каждый кадр:
   - текст и карточки не уходят под колонтитул и за правый край;
   - на титуле название не наезжает на логотип и на арт — иначе сократить название, разбить `\\` или `\settitlewidth{8cm}`; на 3D-артах места меньше;
   - заголовки слайдов в одну строку (в две — сократить);
   - формулы не вылезают из карточек и колонок;
   - номера страниц `N / M` идут подряд, слайды разделов на месте.
5. Переполнен слайд → сократить текст → разбить на два слайда → уменьшить рисунок. Не уменьшать шрифт ниже `\small` и не использовать `[shrink]`: из зала не прочитают.

## 8. Результат

В `<имя>_talk/`: `talk.tex`, `brainpres.sty`, `shortcuts.sty`, `latexmkrc`, `logos/`, `art/`, рисунки, собранный PDF. PDF отправить пользователю. В ответе коротко: сколько слайдов и на какую длительность рассчитано, что из материала сокращено или выброшено, какой арт выбран, что проверить руками (финальные цифры, контакты и QR на финальном слайде, компилятор XeLaTeX на Overleaf).
