#!/bin/bash
# Pull the latest version of the exam shell from git.
cd "$(dirname "$0")" || exit 1
source .resources/main/colors.sh

printf '\033[H\033[2J'
printf "${CYAN}%s${RESET}\n" "╔═══════════════════════════════════════════════════════════╗"
printf "${CYAN}%s${RESET}\n" "║                 🔄 UPDATING 42 EXAM SHELL                 ║"
printf "${CYAN}%s${RESET}\n\n" "╚═══════════════════════════════════════════════════════════╝"

back_to_menu() {
    read -rp "${CYAN}Press enter to return to the menu.${RESET}" _
    exec bash .resources/main/menu.sh
}

if ! command -v git >/dev/null 2>&1; then
    printf "${RED}❌ Error: git is not installed${RESET}\n"; back_to_menu
fi
if ! git rev-parse --git-dir >/dev/null 2>&1; then
    printf "${RED}❌ Error: not a git repository (clone it with git to enable updates)${RESET}\n"; back_to_menu
fi

branch=$(git rev-parse --abbrev-ref HEAD)
printf "${BLUE}📍 Current branch: ${YELLOW}%s${RESET}\n\n" "$branch"
printf "${BLUE}📥 Fetching latest changes...${RESET}\n"
if ! git fetch origin "$branch"; then
    printf "${RED}❌ Failed to fetch${RESET}\n"; back_to_menu
fi

behind=$(git rev-list --count "HEAD..origin/$branch" 2>/dev/null || echo 0)
if [ "$behind" -eq 0 ]; then
    printf "${GREEN}✅ You are up to date!${RESET}\n\n"
else
    printf "${YELLOW}📦 %s update(s) available:${RESET}\n" "$behind"
    git log "HEAD..origin/$branch" --oneline | sed 's/^/   /'
    echo
    if git pull --ff-only origin "$branch"; then
        printf "${GREEN}✅ Update complete!${RESET}\n\n"
    else
        printf "${RED}❌ Failed to pull (do you have local changes?)${RESET}\n\n"
    fi
fi
back_to_menu
