#!/bin/bash
# Shared helpers: paths, language, subjects, rendu folder, tests.

MAIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RES_DIR="$(cd "$MAIN_DIR/.." && pwd)"
ROOT_DIR="$(cd "$RES_DIR/.." && pwd)"
RENDU_DIR="$ROOT_DIR/rendu"
TRACE_DIR="$ROOT_DIR/trace"
LANG_FILE="$RES_DIR/.lang"
PYTHON="${PYTHON:-python3}"

source "$MAIN_DIR/colors.sh"

clear_screen() { printf '\033[H\033[2J'; }

pause() { read -rp "${GREEN}${BOLD}$1${RESET}" _; }

spinner() {
    local frames="◐ ◓ ◑ ◒" i f
    for i in 1 2 3; do
        for f in $frames; do
            printf '\r%s%s%s %s' "$GREEN$BOLD" "$1" "$RESET" "$f"
            sleep 0.08
        done
    done
    printf '\r\033[K'
}

label() {
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "███████╗██╗  ██╗ █████╗ ███╗   ███╗   ██████╗ ██╗   ██╗"
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║   ██╔══██╗╚██╗ ██╔╝"
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "█████╗   ╚███╔╝ ███████║██╔████╔██║   ██████╔╝ ╚████╔╝ "
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║   ██╔═══╝   ╚██╔╝  "
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██╗██║        ██║   "
    printf "${BG_BLUE}${WHITE}%s${RESET}\n" "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝        ╚═╝   "
    printf "${BOLD}${WHITE}%s${RESET}\n\n" " 42 Exam Practice (C & Python) · Level Mode & Real Exam Mode"
}

# ------------------------------------------------------------------ language
get_lang() {
    if [ -f "$LANG_FILE" ] && [ "$(cat "$LANG_FILE")" = "fr" ]; then echo fr; else echo en; fi
}

toggle_lang() {
    if [ "$(get_lang)" = "fr" ]; then echo en > "$LANG_FILE"; else echo fr > "$LANG_FILE"; fi
}

# ------------------------------------------------------------------ subjects
list_ranks() {
    local d
    for d in "$RES_DIR"/rank*; do [ -d "$d" ] && basename "$d"; done
}

list_levels() {  # $1 = rank
    local d
    for d in "$RES_DIR/$1"/level*; do [ -d "$d" ] && basename "$d"; done | sort
}

list_subjects() {  # $1 = rank, $2 = level
    local d
    for d in "$RES_DIR/$1/$2"/*; do [ -f "$d/tester.py" ] && basename "$d"; done
}

count_subjects() {  # $1 = rank
    find "$RES_DIR/$1" -name tester.py | wc -l | tr -d ' '
}

rank_label() {  # rank03 -> 03
    echo "${1#rank}"
}

subject_dir() { echo "$RES_DIR/$1/$2/$3"; }

expected_file() {  # $1 = subject dir
    sed -n 's/^Expected files *: *//p' "$1/sub.txt" | head -1
}

show_subject() {  # $1 = subject dir
    local f="$1/sub.txt"
    if [ "$(get_lang)" = "fr" ] && [ -f "$1/sub.fr.txt" ]; then f="$1/sub.fr.txt"; fi
    printf "${WHITE}"
    cat "$f"
    printf "${RESET}"
}

rank_lang() {  # Python or C
    if [ -n "$(find "$RES_DIR/$1" -name main.c -o -type d -name ref 2>/dev/null | head -1)" ]; then
        echo C
    else
        echo Python
    fi
}

prepare_rendu() {  # $1 = subject dir ; creates rendu/<subject>/ with the expected files
    local name f
    name="$(basename "$1")"
    mkdir -p "$RENDU_DIR/$name"
    expected_file "$1" | tr ',' '\n' | while read -r f; do
        case "$f" in
            "") continue ;;
            "*.c") f="$name.c" ;;
            "*"*) continue ;;
        esac
        [ -f "$RENDU_DIR/$name/$f" ] || touch "$RENDU_DIR/$name/$f"
    done
    if [ -d "$1/given" ]; then
        for f in "$1"/given/*; do
            [ -f "$RENDU_DIR/$name/$(basename "$f")" ] || cp "$f" "$RENDU_DIR/$name/"
        done
    fi
}

# Run the tester of a subject. Returns 0 if PASSED.
run_test() {  # $1 = subject dir
    local code
    printf "${CYAN}Testing ${BOLD}rendu/%s/${RESET}${CYAN} ...${RESET}\n\n" "$(basename "$1")"
    FORCE_COLOR=1 "$PYTHON" "$1/tester.py"
    code=$?
    find "$RENDU_DIR" -name "__pycache__" -type d -prune -exec rm -rf {} + 2>/dev/null
    return $code
}

shuffle_words() {  # prints its arguments in random order, one per line
    local arr=("$@") i j tmp
    for ((i = ${#arr[@]} - 1; i > 0; i--)); do
        j=$((RANDOM % (i + 1)))
        tmp="${arr[i]}"; arr[i]="${arr[j]}"; arr[j]="$tmp"
    done
    printf '%s\n' "${arr[@]}"
}

pick_random() {  # prints one of its arguments
    local arr=("$@")
    echo "${arr[$((RANDOM % ${#arr[@]}))]}"
}

# Backup the rendu folder into trace/ and remove it.
archive_rendu() {
    if [ -d "$RENDU_DIR" ] && [ -n "$(find "$RENDU_DIR" -type f -size +0 2>/dev/null)" ]; then
        local stamp
        stamp="$(date +%Y%m%d_%H%M%S)"
        mkdir -p "$TRACE_DIR"
        cp -r "$RENDU_DIR" "$TRACE_DIR/rendu_$stamp"
        printf "${DIM}Your work was saved in trace/rendu_%s${RESET}\n" "$stamp"
    fi
    rm -rf "$RENDU_DIR"
}

check_python() {
    if ! command -v cc >/dev/null 2>&1; then
        printf "${YELLOW}Warning: no C compiler (cc) found: Rank 02 tests will not work.${RESET}\n"
        sleep 2
    fi
    if ! command -v "$PYTHON" >/dev/null 2>&1; then
        printf "${RED}python3 is required but was not found.${RESET}\n"
        exit 1
    fi
    if ! "$PYTHON" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)'; then
        printf "${YELLOW}Warning: Python >= 3.9 is recommended (found %s).${RESET}\n" \
            "$("$PYTHON" --version 2>&1)"
        sleep 2
    fi
}

format_duration() {  # seconds -> HH:MM:SS
    printf '%02d:%02d:%02d' $(($1 / 3600)) $(($1 % 3600 / 60)) $(($1 % 60))
}
