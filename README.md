# 42 Exam Practice Shell — Python (new curriculum)

⚡ An interactive practice environment for the **42 School new-curriculum Python exams (Ranks 03 → 06)** ⚡

> 🇫🇷 Un shell d'entraînement aux examens Python du nouveau cursus 42 : menus, mode Level, mode
> Real Exam, dossier `rendu/`, et un testeur automatique pour chaque exercice. Les sujets sont
> disponibles en anglais **et en français** (option *Subject language* du menu).

Inspired by [terminal-42s/42_examshell](https://github.com/terminal-42s/42_examshell) (C exams),
rebuilt for Python with the subjects published on [42exam.net](https://42exam.net/).

## 🚀 Features

- **Interactive menu** — same look & flow as the classic exam shell
- **4 Python ranks, 37 subjects** — Rank 03 (14), Rank 04 (7), Rank 05 (7), Rank 06 (9)
- **Level Mode** — practice every subject of a level, in random order
- **Real Exam Mode** — one random subject per level, you must pass it to unlock the next level
  (timer + attempt counter)
- **Automatic tester** for every subject:
  - your function is compared with a reference solution on the subject examples
    **plus hundreds of random inputs**
  - forbidden functions / modules (`sorted()`, `.sort()`, `heapq`, `json`, `OrderedDict`,
    `graphlib.TopologicalSorter`, …) are detected
  - 10 s time limit (infinite loops, too slow algorithms)
  - clear `Expected / Got` report on the first failing case
- **EN / FR subjects**
- **`rendu/` workspace** — the expected file is created for you; your work is saved in `trace/`
  when you leave
- **Update** from the menu (`git pull`)

## 🔧 Installation & usage

```bash
git clone <this repository> 42_examshell_python
cd 42_examshell_python
make            # or: bash exam.sh
```

Requirements: `bash`, `python3` (3.10+ recommended), Linux or macOS. No extra package.

### Menu

```
📖 1. Commands
🐍 2. Exam Rank 03  (14 subjects, 6 levels)
🐍 3. Exam Rank 04  (7 subjects, 4 levels)
🐍 4. Exam Rank 05  (7 subjects, 3 levels)
🐍 5. Exam Rank 06  (9 subjects, 2 levels)
📁 6. Open Rendu Folder
🌐 7. Subject language: EN  (switch EN/FR)
🔄 8. Update ExamShell
```

Each rank offers **Level Mode** and **Real Exam Mode**.

### Commands (at the `/>` prompt)

| Command | Action |
|---|---|
| `test` | run the tester on `rendu/<subject>/<file>.py` |
| `next` | next subject (Real mode: another subject of the same level) |
| `sub`  | display the subject again |
| `menu` | back to the menu |
| `exit` | quit (your `rendu/` is saved in `trace/`) |

### Example

```
/> test
Testing rendu/py_twist_sequence/py_twist_sequence.py ...

FAIL  test 5: twist_sequence([], 3) raised an exception:
    ZeroDivisionError: integer modulo by zero
```

```
/> test
PASSED  409 tests OK 🎉
✔ Level 5 passed!
```

## 📁 Project structure

```
.
├── exam.sh                 # entry point
├── Makefile                # make / make test / make clean / make fclean
├── update.sh               # git pull from the menu
└── .resources/
    ├── main/               # shell: menu.sh, modes.sh, common.sh, colors.sh
    ├── lib/pytester.py     # shared test engine
    ├── tools/selftest.sh   # maintainer check (make test)
    └── rankXX/levelN/<subject>/
        ├── sub.txt         # subject (EN)
        ├── sub.fr.txt      # subject (FR)
        ├── <subject>.py    # reference solution
        └── tester.py       # test cases
```

The menus are built from the folders, so **adding a subject** only requires a new
`rankXX/levelN/<subject>/` folder with the four files above. `make test` checks that every
reference solution passes its tester and that a wrong solution fails it.

## 📚 Subjects

### Exam Rank 03 — 14 subjects, 6 levels

| Level | Subject | Function / class |
|---|---|---|
| 1 | `py_bracket_validator` | `bracket_validator` |
| 1 | `py_cryptic_sorter` | `cryptic_sorter` |
| 2 | `py_echo_validator` | `echo_validator` |
| 2 | `py_mirror_matrix` | `mirror_matrix` |
| 3 | `py_hidenp` | `hidenp` |
| 3 | `py_inter` | `inter` |
| 3 | `py_number_base_converter` | `number_base_converter` |
| 3 | `py_pattern_tracker` | `pattern_tracker` |
| 4 | `py_anagram` | `anagram` |
| 4 | `py_shadow_merge` | `shadow_merge` |
| 4 | `py_string_permutation_checker` | `string_permutation_checker` |
| 5 | `py_string_sculptor` | `string_sculptor` |
| 5 | `py_twist_sequence` | `twist_sequence` |
| 6 | `py_whisper_cipher` | `whisper_cipher` |

### Exam Rank 04 — 7 subjects, 4 levels

| Level | Subject | Function / class |
|---|---|---|
| 1 | `py_array_rotation_detector` | `array_rotation_detector` |
| 1 | `py_constellation_mapper` | `constellation_mapper` |
| 2 | `py_list_intersection_finder` | `list_intersection_finder` |
| 2 | `py_merge_sorted_lists` | `merge_sorted_lists` |
| 3 | `py_package_dependency_resolver` | `package_dependency_resolver` |
| 3 | `py_palindrome_partitioner` | `palindrome_partitioner` |
| 4 | `py_sliding_window_maximum` | `sliding_window_maximum` |

### Exam Rank 05 — 7 subjects, 3 levels

| Level | Subject | Function / class |
|---|---|---|
| 1 | `py_compress_decompress` | `compress`, `decompress` |
| 1 | `py_room_scheduler` | `py_room_scheduler` |
| 1 | `py_spiral_matrix` | `generate_spiral` |
| 2 | `py_graph_cycle_detector` | `py_graph_cycle_detector` |
| 2 | `py_island_matrix_counter` | `island_matrix_counter` |
| 3 | `py_prism_detector` | `prism_detector` |
| 3 | `py_word_ladder` | `word_ladder` |

### Exam Rank 06 — 9 subjects, 2 levels

| Level | Subject | Function / class |
|---|---|---|
| 1 | `pack_strings` | `pack`, `unpack` |
| 1 | `prefix_dictionary` | `PrefixDictionary` |
| 1 | `redundant_link` | `redundant_link` |
| 1 | `task_order` | `task_order` |
| 1 | `trie_autocomplete` | `trie_autocomplete` |
| 2 | `bridge_finder` | `bridge_finder` |
| 2 | `cache_keeper` | `CacheKeeper` |
| 2 | `min_heap` | `MinHeap` |
| 2 | `union_find_system` | `UnionFind` |

## ⚠️ Notes

- Where a subject leaves a detail open (e.g. the order of results), the tester accepts every
  answer the subject allows — for instance any valid room assignment in `py_room_scheduler`,
  or any order of matches in `py_prism_detector`.
- Reference solutions are in the subject folders. Try not to look at them before you pass. 😉
- Unofficial, student-made tool, not affiliated with 42. Subjects come from the community
  site [42exam.net](https://42exam.net/) — please report outdated subjects there.

**Good luck with your exams! 🍀**
