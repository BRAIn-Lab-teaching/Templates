# BrainLab Templates

Шаблоны лаборатории [BRAIn Lab](https://t.me/brainlaboratory) (МФТИ) в едином
фирменном стиле: LaTeX-шаблоны статьи, постера и два beamer-шаблона (для докладов
и для лекций), шаблон презентации PowerPoint, а также PowerPoint-шаблон
Института искусственного интеллекта МФТИ (ИИИ).
К каждому шаблону есть скилл для Claude, который переводит в него готовые
материалы (чужую статью, постер, презентацию, конспект).

## Шаблоны

| Шаблон | Для чего | Сборка | Точка входа | Скилл |
|---|---|---|---|---|
| [`Article`](Article/README.md) | Статьи, препринты, arXiv | `pdflatex` + `bibtex` | `demo.tex` | [`brainlab-article`](skills/brainlab-article/SKILL.md) |
| [`Poster`](Poster/README.md) | Постеры A3–A0 для стендовых сессий | `pdflatex` + `bibtex` | `demo.tex` | [`brainlab-poster`](skills/brainlab-poster/SKILL.md) |
| [`Presentation_BrainLab`](Presentation_BrainLab/README.md) | Доклады, конференции, публичные выступления (16:9) | **XeLaTeX** | `demo.tex` | [`brainlab-pres`](skills/brainlab-pres/SKILL.md) |
| [`Presentation_Lecture`](Presentation_Lecture/README.md) | Лекции и семинары (4:3, ФПМИ / Иннополис / ИСП) | `pdflatex` | `main.tex` | [`brainlab-lecture-pres`](skills/brainlab-lecture-pres/SKILL.md) |
| [`Presentation_pptx`](Presentation_pptx/README.md) | Презентации в PowerPoint / Keynote / Google Slides (16:9) | — | `Шаблон презентации.pptx` | [`brainlab-presentation`](Presentation_pptx/brainlab-presentation.skill) |
| [`Presentation_IAI`](Presentation_IAI/README.md) | Презентации в бренде ИИИ МФТИ (PowerPoint, 16:9) | — | шаблон в Google Slides | [`iii-presentation`](Presentation_IAI/iii-presentation.skill) |

Шаблоны в Overleaf: [статья](https://www.overleaf.com/read/ctmzkhnmckpw#e2be80),
[постер](https://www.overleaf.com/read/kshvrwsqhrgn#824620),
[доклад](https://www.overleaf.com/project/6af4821c40a785d6b31c2e0d/share#252d6cfe829accfded108d77dded3fb3c1d09364cc45f4e0),
[лекция](https://www.overleaf.com/read/btpqwqvvzvmd#f07248).
Шаблоны PowerPoint в Google Slides:
[BrainLab](https://docs.google.com/presentation/d/11aaycj_GW3KmMylUzDNoXzLF9ZQMFGuL/edit?usp=sharing),
[ИИИ МФТИ](https://docs.google.com/presentation/d/1kO26Wkvut_Fq_815SXgKZ8tEGGAQh7l0/edit?usp=sharing).

**Какую презентацию брать.** Выступаете с результатами на конференции или
семинаре — `Presentation_BrainLab`. Читаете курс, нужны теоремы, алгоритмы и
навигация по разделам — `Presentation_Lecture`. Делаете слайды не в LaTeX, а в
PowerPoint или Google Slides — `Presentation_pptx`. Выступаете от имени ИИИ
МФТИ — `Presentation_IAI`.

## Как начать

1. Склонируйте репозиторий или скачайте нужную папку:

   ```bash
   git clone https://github.com/BRAIn-Lab-teaching/Templates.git
   ```

2. Скопируйте папку шаблона целиком — стилевик (`.sty`), `shortcuts.sty`,
   `logos/` и остальные ресурсы нужны вместе с главным `.tex`.
3. Откройте README в папке шаблона: там быстрый старт, все опции пакета,
   окружения и известные особенности.
4. Соберите через `latexmk` — он сам сделает нужное число проходов и запустит
   `bibtex`. На Overleaf компилятор по умолчанию (pdfLaTeX) подходит всем, кроме
   `Presentation_BrainLab`: там Menu → Settings → Compiler → **XeLaTeX** (или
   загрузите `latexmkrc` вместе с проектом).

### Версия TeX Live

Шаблоны рассчитаны на **TeX Live 2026** (минимум 2025). На Overleaf версия
задаётся в каждом проекте отдельно: Menu → Settings → TeX Live version →
**2026**. Проекты, созданные давно, часто стоят на 2020 (Legacy). На нём часть
команд стилевиков не определена: сборка падает или печатает мусор на первой
странице (например, `⟨⟩⟨mg⟩ 1|2 ()` на титуле лекции). Если скопировали шаблон
через Copy Project, проверьте версию в копии.

Для кириллицы под `pdflatex` нужны шрифты `cm-super` и `lh` (на Overleaf есть,
локально — `sudo tlmgr install cm-super lh`). Постеру дополнительно нужен `cm-lgc`.

## Скиллы для Claude

В папке [`skills/`](skills/) лежат скиллы — инструкции для Claude, по которым он
переносит материалы в шаблоны лаборатории: берёт файлы шаблона из этого
репозитория, переносит содержимое без изменений по смыслу, собирает PDF и
проверяет лог.

| Скилл | Шаблон | Что умеет | Архив |
|---|---|---|---|
| [`brainlab-article`](skills/brainlab-article/SKILL.md) | `Article` | Переводит статью из NeurIPS, ICML, ICLR, IEEE, ACM, LNCS, elsarticle, arXiv и т. п. в `brainlab.sty` | [`.skill`](skills/brainlab-article.skill) |
| [`brainlab-poster`](skills/brainlab-poster/SKILL.md) | `Poster` | Верстает постер из статьи, чужого постера (tikzposter, beamerposter, baposter…) или текста и картинок | [`.skill`](skills/brainlab-poster.skill) |
| [`brainlab-pres`](skills/brainlab-pres/SKILL.md) | `Presentation_BrainLab` | Собирает доклад из статьи, чужой beamer-презентации, `.pptx`/PDF слайдов или текста | [`.skill`](skills/brainlab-pres.skill) |
| [`brainlab-lecture-pres`](skills/brainlab-lecture-pres/SKILL.md) | `Presentation_Lecture` | Верстает или переоформляет лекцию из beamer-`.tex`, PDF/`.pptx`, конспекта, markdown | [`.skill`](skills/brainlab-lecture-pres.skill) |
| `brainlab-presentation` | `Presentation_pptx` | Собирает или переоформляет `.pptx` в бренде BrainLab из плана, заметок или готовой презентации | [`.skill`](Presentation_pptx/brainlab-presentation.skill) |
| `iii-presentation` | `Presentation_IAI` | То же для бренда ИИИ МФТИ (не BrainLab) | [`.skill`](Presentation_IAI/iii-presentation.skill) |

Скиллы для `.pptx` лежат только архивами, рядом со своими шаблонами — в
[`Presentation_pptx/`](Presentation_pptx/) и [`Presentation_IAI/`](Presentation_IAI/).

**Установка.**

- **Claude (приложение или claude.ai):** Settings → Capabilities → Skills →
  Upload skill, выберите нужный файл `.skill`.
- **Claude Code:** скопируйте папку скилла в `~/.claude/skills/` (для всех
  проектов) или в `.claude/skills/` внутри проекта. Архив `.skill` — это zip,
  его достаточно распаковать туда же:

  ```bash
  cp -r skills/brainlab-article ~/.claude/skills/
  ```

  ```bash
  unzip Presentation_pptx/brainlab-presentation.skill -d ~/.claude/skills/
  ```

**Использование.** Достаточно попросить своими словами и приложить материалы:
«переведи эту статью в шаблон BrainLab», «сделай постер A0 по этой статье»,
«собери доклад в нашей beamer-теме», «переоформи лекцию в стиле ФПМИ». Скилл
подхватится сам. Если репозиторий у Claude под рукой (папка подключена или есть
доступ к GitHub), файлы шаблона он возьмёт отсюда — актуальные README и
`demo.tex` для него главнее текста скилла.

## Структура репозитория

```
Templates/
├── Article/                  шаблон статьи (brainlab.sty)
├── Poster/                   шаблон постера (brainposter.sty), qr/ — QR-коды
├── Presentation_BrainLab/    beamer для докладов (brainpres.sty), art/ — декор
├── Presentation_Lecture/     beamer для лекций (pres.sty)
├── Presentation_IAI/         скилл для .pptx ИИИ МФТИ (сам шаблон — в Google Slides)
├── Presentation_pptx/        шаблон PowerPoint BrainLab и его скилл
└── skills/                   скиллы для Claude: папки с SKILL.md и архивы .skill
```

## Общее для LaTeX-шаблонов

- **`shortcuts.sty`** — математические сокращения (`\R`, `\norm`, `\expect`,
  `\argmin` и т. д.). Набор в шаблонах почти одинаковый, но имена функций
  отличаются: в статье `\funcf`, `\g`, `\h`, в постере `\funcf`, `\funcg`,
  `\funch`, в лекциях `\f`, `\g`, `\h`. При копировании формул между шаблонами
  это нужно учитывать.
- **`\cite` = `\citep`** в статье и постере; для ссылки в тексте — `\citet`.
- **Метаданные PDF** (Title, Author, Keywords) в статье и постере заполняются
  сами из `\setbrainmeta`.
- **Цвета** в своих рисунках и слайдах берите по ролям (`primary`, `bltitle`,
  `braincolor` и т. п. — см. README шаблона), а не сырыми hex-кодами: так они
  останутся правильными при смене площадки или тёмного фона.
