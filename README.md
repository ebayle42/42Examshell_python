*This project has been created by ebayle, to practice the 42 exams.*

# 42_examshell_python

## Description

42_examshell_python, because training for the exam is easier when someone checks your code every time you type `test`

An interactive practice shell for the 42 exams: Rank 02 in C and the new curriculum Python
exams (Rank 03 to Rank 06), 94 subjects in total, each one with a reference solution and an
automatic tester. It works like [terminal-42s/42_examshell](https://github.com/terminal-42s/42_examshell),
with the subjects published on [42exam.net](https://42exam.net/)

- `exam.sh` : entry point, launches the menu
- `Makefile` : `make` launches the shell, `make test` checks every exercise
- `update.sh` : updates the shell with `git pull`
- `.resources/main/menu.sh` : main menu, ranks are found from the folders
- `.resources/main/modes.sh` : Level Mode, Real Exam Mode, rank menu, commands screen
- `.resources/main/common.sh` : helpers (paths, language, subjects, `rendu/` folder, tests)
- `.resources/main/colors.sh` : colors of the interface
- `.resources/lib/pytester.py` : test engine of the Python exercises
- `.resources/lib/ctester.py` : test engine of the C exercises
- `.resources/tools/selftest.sh` : checks that every reference passes and a wrong solution fails
- `.resources/rank02/levelN/<subject>/` : C subject, `sub.txt`, `ref/` (reference), `main.c`
  (test main of the function exercises), `given/` (files handed to you), `tester.py`
- `.resources/rankXX/levelN/<subject>/` : Python subject, `sub.txt` (EN), `sub.fr.txt` (FR),
  `<subject>.py` (reference), `tester.py`

## Instructions

Install:

```sh
git clone git@github.com:ebayle42/42Examshell_python.git
```
```sh
cd 42_examshell_python
```

Run:

```sh
make        # launches the exam shell
```
```sh
bash exam.sh # same thing
```
```sh
make test   # checks the 94 testers against their reference
```
```sh
make clean  # removes the rendu folder
```
```sh
make fclean # clean + removes the trace folder
```

Requirements: `bash`, `python3` (3.10 or more recommended) and `cc` (gcc or clang) for Rank 02,
on Linux or macOS, no extra package

Menu:

```
📖 1. Commands
⚙️  2. Exam Rank 02 (C)  (57 subjects, 4 levels)
🐍 3. Exam Rank 03 (Python)  (14 subjects, 6 levels)
🐍 4. Exam Rank 04 (Python)  (7 subjects, 4 levels)
🐍 5. Exam Rank 05 (Python)  (7 subjects, 3 levels)
🐍 6. Exam Rank 06 (Python)  (9 subjects, 2 levels)
📁 7. Open Rendu Folder
🌐 8. Subject language: EN  (switch EN/FR)
🔄 9. Update ExamShell
```

Each rank has two modes

- `Level Mode` : every subject of the chosen level, in a random order
- `Real Exam Mode` : one random subject per level, you must pass it to unlock the next level,
  with a timer and an attempt counter

Commands at the `/>` prompt:

| Command | Action |
|---|---|
| `test` | tests your code in `rendu/<subject>/` |
| `next` | next subject (in Real Exam Mode, another subject of the same level) |
| `sub` | displays the subject again |
| `menu` | goes back to the menu |
| `exit` | quits, your `rendu/` folder is saved in `trace/` |

The expected files are created for you in `rendu/<subject>/`, and the files given by the
subject (`list.h`, `ft_list.h`) are copied there

## Testers

Your code and the reference solution are run on the same inputs, the subject examples plus
many random inputs, and the first difference is shown with the expected and the obtained result

- Python : your function or class is imported and compared with the reference, forbidden
  functions and modules (`sorted()`, `.sort()`, `heapq`, `json`, `OrderedDict`,
  `graphlib.TopologicalSorter`...) are detected by reading the code, 10 s time limit
- C : compiled with `cc -Wall -Wextra -Werror`, the output is compared byte by byte and shown
  like `cat -e`, functions that are not in *Allowed functions* are detected with `nm`,
  segfaults and infinite loops are reported, function exercises are linked with a test `main.c`

- when a subject leaves a detail open (order of the results, choice of the room...), every
  answer allowed by the subject is accepted

```
/> test
FAIL  test 5: $> ./first_word '  lorem,ipsum  ' | cat -e
Expected:
    lorem,ipsum$
Got:
    $
```

## Subjects

| Rank | Language | Levels | Subjects |
|---|---|---|---|
| 02 | C | 4 | 57 |
| 03 | Python | 6 | 14 |
| 04 | Python | 4 | 7 |
| 05 | Python | 3 | 7 |
| 06 | Python | 2 | 9 |

- Rank 02
  - level 1 : `first_word`, `fizzbuzz`, `ft_putstr`, `ft_strcpy`, `ft_strlen`, `ft_swap`, `repeat_alpha`, `rev_print`, `rot_13`, `rotone`, `search_and_replace`, `ulstr`
  - level 2 : `alpha_mirror`, `camel_to_snake`, `do_op`, `ft_atoi`, `ft_strcmp`, `ft_strcspn`, `ft_strdup`, `ft_strpbrk`, `ft_strrev`, `ft_strspn`, `inter`, `is_power_of_2`, `last_word`, `max`, `print_bits`, `reverse_bits`, `snake_to_camel`, `swap_bits`, `union`, `wdmatch`
  - level 3 : `add_prime_sum`, `epur_str`, `expand_str`, `ft_atoi_base`, `ft_list_size`, `ft_range`, `ft_rrange`, `hidenp`, `lcm`, `paramsum`, `pgcd`, `print_hex`, `rstr_capitalizer`, `str_capitalizer`, `tab_mult`
  - level 4 : `flood_fill`, `fprime`, `ft_itoa`, `ft_list_foreach`, `ft_list_remove_if`, `ft_split`, `rev_wstr`, `rostring`, `sort_int_tab`, `sort_list`
- Rank 03
  - level 1 : `py_bracket_validator`, `py_cryptic_sorter`
  - level 2 : `py_echo_validator`, `py_mirror_matrix`
  - level 3 : `py_hidenp`, `py_inter`, `py_number_base_converter`, `py_pattern_tracker`
  - level 4 : `py_anagram`, `py_shadow_merge`, `py_string_permutation_checker`
  - level 5 : `py_string_sculptor`, `py_twist_sequence`
  - level 6 : `py_whisper_cipher`
- Rank 04
  - level 1 : `py_array_rotation_detector`, `py_constellation_mapper`
  - level 2 : `py_list_intersection_finder`, `py_merge_sorted_lists`
  - level 3 : `py_package_dependency_resolver`, `py_palindrome_partitioner`
  - level 4 : `py_sliding_window_maximum`
- Rank 05
  - level 1 : `py_compress_decompress`, `py_room_scheduler`, `py_spiral_matrix`
  - level 2 : `py_graph_cycle_detector`, `py_island_matrix_counter`
  - level 3 : `py_prism_detector`, `py_word_ladder`
- Rank 06
  - level 1 : `pack_strings`, `prefix_dictionary`, `redundant_link`, `task_order`, `trie_autocomplete`
  - level 2 : `bridge_finder`, `cache_keeper`, `min_heap`, `union_find_system`

To add a subject, create a `rankXX/levelN/<subject>/` folder laid out like the others, the
menus are built from the folders

## Resources

- [42exam.net](https://42exam.net/) : the subjects (unofficial, made by students)
- [terminal-42s/42_examshell](https://github.com/terminal-42s/42_examshell) : the original exam shell
- [Python documentation](https://docs.python.org/3/) : `ast`, `importlib`, `subprocess`
- `man 1 nm`, `man 1 gcc`
- [Bash reference manual](https://www.gnu.org/software/bash/manual/bash.html)
- [GNU Make manual](https://www.gnu.org/software/make/manual/make.html)

Unofficial tool, not affiliated with 42, the reference solutions are in the subject folders,
try not to look at them before you pass 😉

AI usage: the code of this shell, the testers and the reference solutions were written with Claude
