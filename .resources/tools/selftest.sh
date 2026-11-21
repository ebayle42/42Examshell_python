#!/bin/bash
# Maintainer self-test: every reference solution must pass its own tester,
# and a dummy solution must fail it.  Run with:  make test
cd "$(dirname "$0")/../.." || exit 1
tmp="$(mktemp -d)"
printf 'def nothing():\n    return None\n' > "$tmp/wrong.py"
ok=0; ko=0
for t in $(find .resources -name tester.py | sort); do
    d="$(dirname "$t")"
    ex="$(basename "$d")"
    if [ -d "$d/ref" ]; then  # C exercise
        mkdir -p "$tmp/c/$ex"
        echo "int g_dummy;" > "$tmp/c/$ex/$ex.c"
        cp "$d"/ref/*.h "$tmp/c/$ex/" 2>/dev/null
        good=(env EXAM_STUDENT_DIR="$d/ref")
        bad=(env EXAM_STUDENT_DIR="$tmp/c/$ex")
    else
        file="$(sed -n 's/^Expected files *: *//p' "$d/sub.txt" | head -1)"
        good=(env EXAM_STUDENT_FILE="$d/$file")
        bad=(env EXAM_STUDENT_FILE="$tmp/wrong.py")
    fi
    if out=$("${good[@]}" python3 "$t" 2>&1); then
        if "${bad[@]}" python3 "$t" >/dev/null 2>&1; then
            echo "BROKEN  $ex: a dummy solution passes"; ko=$((ko + 1))
        else
            printf "ok      %-34s %s\n" "$ex" "$(echo "$out" | tail -1)"; ok=$((ok + 1))
        fi
    else
        echo "BROKEN  $ex: reference fails -> $out"; ko=$((ko + 1))
    fi
done
rm -rf "$tmp"
find .resources -name __pycache__ -type d -prune -exec rm -rf {} +
echo "----"
echo "$ok ok, $ko broken"
[ "$ko" -eq 0 ]
