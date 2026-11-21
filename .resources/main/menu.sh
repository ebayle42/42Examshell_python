#!/bin/bash
# Entry point of the exam shell: main menu.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"
source "$MAIN_DIR/modes.sh"

check_python
mkdir -p "$RENDU_DIR"

open_rendu() {
    mkdir -p "$RENDU_DIR"
    if command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$RENDU_DIR" >/dev/null 2>&1 &
    elif command -v open >/dev/null 2>&1; then
        open "$RENDU_DIR"
    else
        printf "Rendu folder: %s\n" "$RENDU_DIR"
        sleep 2
    fi
}

main_menu() {
    local ranks=() r opt idx n_ranks lang
    while IFS= read -r r; do ranks+=("$r"); done < <(list_ranks)
    n_ranks=${#ranks[@]}
    while true; do
        lang="$(get_lang)"
        clear_screen
        label
        printf "${CYAN}%s${RESET}\n" "╔═══════════════════════════════════════════════════════════╗"
        printf "${CYAN}║${GREEN}%s${CYAN}║${RESET}\n" "      ⚡ EXAM 42 PRACTICE · C & PYTHON (NEW CURRICULUM) ⚡     "
        printf "${CYAN}%s${RESET}\n" "╠═══════════════════════════════════════════════════════════╣"
        printf "${YELLOW}${BOLD}%s${RESET}\n" "📖 1. Commands"
        idx=2
        for r in "${ranks[@]}"; do
            printf "${YELLOW}${BOLD}%s %d. Exam Rank %s (%s)${RESET}  ${DIM}(%s subjects, %s levels)${RESET}\n" \
                "$( [ "$(rank_lang "$r")" = C ] && echo "⚙️ " || echo "🐍")" "$idx" "$(rank_label "$r")" \
                "$(rank_lang "$r")" "$(count_subjects "$r")" "$(list_levels "$r" | wc -l | tr -d ' ')"
            idx=$((idx + 1))
        done
        printf "${YELLOW}${BOLD}📁 %d. Open Rendu Folder${RESET}\n" "$idx"
        printf "${YELLOW}${BOLD}🌐 %d. Subject language: %s${RESET}  ${DIM}(switch EN/FR)${RESET}\n" \
            $((idx + 1)) "$(echo "$lang" | tr '[:lower:]' '[:upper:]')"
        printf "${YELLOW}${BOLD}🔄 %d. Update ExamShell${RESET}\n" $((idx + 2))
        printf "${CYAN}%s${RESET}\n" "╚═══════════════════════════════════════════════════════════╝"
        printf "${DIM}Type 'exit' to quit.${RESET}\n"
        read -rp "${GREEN}${BOLD}Enter your choice (1-$((idx + 2))): ${RESET}" opt || quit_shell
        case "$opt" in
            1) help_screen; continue ;;
            exit) quit_shell ;;
        esac
        if [[ "$opt" =~ ^[0-9]+$ ]]; then
            if [ "$opt" -ge 2 ] && [ "$opt" -lt $((2 + n_ranks)) ]; then
                rank_menu "${ranks[$((opt - 2))]}"
                mkdir -p "$RENDU_DIR"
                continue
            fi
            case $((opt - idx)) in
                0) open_rendu; continue ;;
                1) toggle_lang; continue ;;
                2) exec bash "$ROOT_DIR/update.sh" ;;
            esac
        fi
        printf "${RED}Invalid choice.${RESET}\n"
        sleep 1
    done
}

main_menu
