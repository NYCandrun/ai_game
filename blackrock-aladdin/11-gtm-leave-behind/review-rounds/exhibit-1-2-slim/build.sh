set -e
Y=/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/slim12
python3 -I $Y/edit.py && python3 -I $Y/finalize.py
cd /home/user/ai_game && node /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/htmlrev/tools/render_chromium.js $Y/preview.html $Y/preview.pdf | tail -1
pdfinfo $Y/preview.pdf | grep Pages
rm -f $Y/pg-*.png; pdftoppm -r 90 -f ${1:-3} -l ${2:-4} -png $Y/preview.pdf $Y/pg
