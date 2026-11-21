#!/bin/bash
# Level Mode (practice) and Real Exam Mode.

quit_shell() {
    clear_screen
    archive_rendu
    printf "${GREEN}${BOLD}Good luck for your exam! 🍀${RESET}\n"
    exit 0
}

print_commands() {
    printf "${YELLOW}Commands: ${BOLD}test${RESET}${YELLOW} · ${BOLD}next${RESET}${YELLOW} · ${BOLD}sub${RESET}${YELLOW} (show again) · "
    printf "${BOLD}menu${RESET}${YELLOW} · ${BOLD}exit${RESET}\n"
}

# ------------------------------------------------------------- Level Mode
level_mode() {  # $1 = rank, $2 = level
    local rank="$1" level="$2" subjects=() s i n dir input
    while IFS= read -r s; do subjects+=("$s"); done < <(shuffle_words $(list_subjects "$rank" "$level"))
    n=${#subjects[@]}
    i=0
    clear_screen
    spinner "$level is being prepared"
    while [ "$i" -lt "$n" ]; do
        dir="$(subject_dir "$rank" "$level" "${subjects[$i]}")"
        prepare_rendu "$dir"
        clear_screen
        printf "${CYAN}${BOLD}Rank %s · %s · subject %d/%d${RESET}   ${DIM}write your code in rendu/%s/ (%s)${RESET}\n" \
            "$(rank_label "$rank")" "$level" $((i + 1)) "$n" "${subjects[$i]}" "$(expected_file "$dir")"
        printf "${BLUE}%s${RESET}\n" "================================================================================"
        show_subject "$dir"
        printf "${BLUE}%s${RESET}\n" "================================================================================"
        print_commands
        read -rp "/> " input || quit_shell
        case "$input" in
            test)
                clear_screen
                if run_test "$dir"; then
                    printf "\n${GREEN}${BOLD}✔ Passed! Type 'next' for another subject.${RESET}\n"
                else
                    printf "\n${RED}${BOLD}✘ Failed. Fix your code and test again.${RESET}\n"
                fi
                echo
                pause "Press enter to continue your practice."
                ;;
            next) i=$((i + 1)) ;;
            menu) archive_rendu; return ;;
            exit) quit_shell ;;
            *) ;;  # 'sub' or anything else: redisplay the subject
        esac
    done
    clear_screen
    printf "${GREEN}${BOLD}All subjects of %s %s are done! 🎉${RESET}\n\n" "$rank" "$level"
    pause "Press enter to return to the menu."
}

choose_level() {  # $1 = rank
    local rank="$1" levels=() l opt idx
    while IFS= read -r l; do levels+=("$l"); done < <(list_levels "$rank")
    while true; do
        clear_screen
        label
        printf "${BLUE}%s${RESET}\n" "┌─────────────────────────────────────────────────────────┐"
        printf "${BLUE}│${GREEN}  🎯 Choose your practice level for Exam Rank %s (%s) ${BLUE}│${RESET}\n" "$(rank_label "$rank")" "$(rank_lang "$rank")"
        printf "${BLUE}%s${RESET}\n" "└─────────────────────────────────────────────────────────┘"
        idx=1
        for l in "${levels[@]}"; do
            printf "${YELLOW}${BOLD}%d. %s${RESET}  ${DIM}(%s)${RESET}\n" "$idx" "$l" \
                "$(list_subjects "$rank" "$l" | tr '\n' ' ' | sed 's/ $//; s/ /, /g')"
            idx=$((idx + 1))
        done
        printf "${YELLOW}${BOLD}%d. Back${RESET}\n" "$idx"
        read -rp "${GREEN}${BOLD}Enter your choice (1-$idx): ${RESET}" opt || quit_shell
        case "$opt" in
            exit) quit_shell ;;
            menu|"$idx") return ;;
        esac
        if [[ "$opt" =~ ^[0-9]+$ ]] && [ "$opt" -ge 1 ] && [ "$opt" -lt "$idx" ]; then
            level_mode "$rank" "${levels[$((opt - 1))]}"
            return
        fi
        printf "${RED}Wrong input${RESET}\n"
        sleep 1
    done
}

# --------------------------------------------------------- Real Exam Mode
real_mode() {  # $1 = rank
    local rank="$1" levels=() subs=() l s k n chosen dir input start attempts total_attempts=0 elapsed
    while IFS= read -r l; do levels+=("$l"); done < <(list_levels "$rank")
    n=${#levels[@]}
    rm -rf "$RENDU_DIR"
    clear_screen
    label
    printf "${GREEN}${BOLD}🧪 Welcome to the Exam Rank %s (%s) — Real Exam Mode${RESET}\n" "$(rank_label "$rank")" "$(rank_lang "$rank")"
    printf "%s\n" "=================================================="
    printf "You will get one random subject per level: %d levels to validate.\n" "$n"
    printf "Pass a subject to unlock the next level. Your work goes in ${BOLD}rendu/${RESET}.\n\n"
    pause "Press enter to start the exam."
    start=$(date +%s)

    for ((k = 0; k < n; k++)); do
        l="${levels[$k]}"
        subs=()
        while IFS= read -r s; do subs+=("$s"); done < <(list_subjects "$rank" "$l")
        chosen="$(pick_random "${subs[@]}")"
        attempts=0
        clear_screen
        spinner "Level $((k + 1)) is being prepared"
        while true; do
            dir="$(subject_dir "$rank" "$l" "$chosen")"
            prepare_rendu "$dir"
            elapsed=$(( $(date +%s) - start ))
            clear_screen
            printf "${MAGENTA}${BOLD}REAL EXAM · Rank %s · Level %d/%d${RESET}   ${DIM}time %s · attempts %d${RESET}\n" \
                "$(rank_label "$rank")" $((k + 1)) "$n" "$(format_duration "$elapsed")" "$attempts"
            printf "${DIM}write your code in rendu/%s/ (%s)${RESET}\n" "$chosen" "$(expected_file "$dir")"
            printf "${BLUE}%s${RESET}\n" "================================================================================"
            show_subject "$dir"
            printf "${BLUE}%s${RESET}\n" "================================================================================"
            print_commands
            read -rp "/> " input || quit_shell
            case "$input" in
                test)
                    clear_screen
                    attempts=$((attempts + 1))
                    total_attempts=$((total_attempts + 1))
                    if run_test "$dir"; then
                        printf "\n${GREEN}${BOLD}✔ Level %d passed!${RESET}\n" $((k + 1))
                        sleep 2
                        break
                    fi
                    printf "\n${RED}${BOLD}✘ Failed. Try again.${RESET}\n\n"
                    pause "Press enter to retry Level $((k + 1))..."
                    ;;
                next)
                    if [ "${#subs[@]}" -gt 1 ]; then
                        s="$chosen"
                        while [ "$s" = "$chosen" ]; do s="$(pick_random "${subs[@]}")"; done
                        chosen="$s"
                    fi
                    ;;
                menu) archive_rendu; return ;;
                exit) quit_shell ;;
                *) ;;
            esac
        done
    done

    elapsed=$(( $(date +%s) - start ))
    clear_screen
    label
    printf "${GREEN}${BOLD}🎉 Congratulations! You've completed Exam Rank %s!${RESET}\n" "$(rank_label "$rank")"
    printf "%s\n" "=================================================="
    printf "Levels passed : %d/%d\n" "$n" "$n"
    printf "Total time    : %s\n" "$(format_duration "$elapsed")"
    printf "Test attempts : %d\n\n" "$total_attempts"
    archive_rendu
    pause "Press enter to return to the menu."
}

rank_menu() {  # $1 = rank
    local rank="$1" opt title pad
    while true; do
        clear_screen
        printf "${CYAN}%s${RESET}\n" "╔═══════════════════════════════════════════════════════════╗"
        title="EXAM RANK $(rank_label "$rank") ($(rank_lang "$rank")) - MODE SELECTION"
        pad=$(( (59 - ${#title}) / 2 ))
        printf "${CYAN}║${GREEN}%*s%s%*s${CYAN}║${RESET}\n" "$pad" "" "$title" $((59 - pad - ${#title})) ""
        printf "${CYAN}%s${RESET}\n" "╚═══════════════════════════════════════════════════════════╝"
        printf "${YELLOW}${BOLD}%s${RESET}\n" "1. Level Mode      (practice every subject of a level)"
        printf "${YELLOW}${BOLD}%s${RESET}\n" "2. Real Exam Mode  (one random subject per level, in order)"
        printf "${YELLOW}${BOLD}%s${RESET}\n" "3. Back to Main Menu"
        read -rp "${GREEN}${BOLD}Enter your choice (1-3): ${RESET}" opt || quit_shell
        case "$opt" in
            1) choose_level "$rank" ;;
            2) real_mode "$rank" ;;
            3|menu) return ;;
            exit) quit_shell ;;
            *) printf "${RED}Invalid choice. Please enter 1, 2, or 3.${RESET}\n"; sleep 1 ;;
        esac
    done
}

help_screen() {
    clear_screen
    label
    printf "${GREEN}${BOLD}Commands${RESET}\n"
    echo "============================="
    echo "Type ${BLUE}'test'${RESET} to test your code."
    echo "Type ${BLUE}'next'${RESET} to move on to the next subject (Real mode: get another subject of the same level)."
    echo "Type ${BLUE}'sub'${RESET}  to display the subject again."
    echo "Type ${BLUE}'menu'${RESET} to return to the menu."
    echo "Type ${BLUE}'exit'${RESET} to exit the exam practice."
    echo "============================="
    echo
    echo "Your files go in ${BOLD}rendu/<subject>/${RESET} (the expected files are created for you)."
    echo "Tests compare your code with a reference solution on the subject examples"
    echo "plus many random inputs. Forbidden functions/modules are detected."
    echo "C (Rank 02) is compiled with: cc -Wall -Wextra -Werror"
    echo "When you leave, your rendu/ folder is saved in ${BOLD}trace/${RESET}."
    echo
    pause "Press enter to return to the menu: "
}
