#!/usr/bin/env python3

from roman_numerals import convert_to_numeral

WORK_LIST = [
    "preface-first",
    "preface-second",
    "main",
]

TITLES = {
    "preface-first": "Preface 1st Edition",
    "preface-second": "Preface 2nd Edition",
    "main": "Main Text",
}

for WORK in WORK_LIST:
    print("processing: " + WORK)
    SRC = f"../text/young-tutorial-greek-{WORK}.txt"
    DEST = f"../docs/young-tutorial-greek-{WORK}.html"

    TITLE = TITLES[WORK]

    HEADER = f"""\
    <!DOCTYPE html>
    <html lang="grc">
    <head>
    <title>{TITLE}</title>
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,700&amp;subset=greek,greek-ext" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/alpheios-components@latest/dist/style/style-components.min.css"/>
    <link href="style.css" rel="stylesheet">
    </head>
    <body>
      <div class="container alpheios-enabled" lang="grc">
      <nav>&#x2191; <a href="./">Young's The Tutorial Greek Reader</a></nav>
    """

    FOOTER = """\
        <br/><br/>
        <nav>&#x2191; <a href="./">Young's The Tutorial Greek Reader</a></nav>
        <br/>
        <p>This work is licensed under a <a href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.</p>
        <p>The source is available at <a href="https://github.com/sleeptillseven/youngs-tutorial-greek-reader">https://github.com/sleeptillseven/youngs-tutorial-greek-reader</a>.</p>
      </div>
      <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", function(event) {
            import ("https://cdn.jsdelivr.net/npm/alpheios-embedded@latest/dist/alpheios-embedded.min.js").then(embedLib => {
                window.AlpheiosEmbed.importDependencies({
                mode: 'cdn'
                }).then(Embedded => {
                new Embedded({
                    clientId: 'sleeptillseven_youngs_tutorial_greek'
                }).activate();
                }).catch(e => {
                console.error(`Import of Alpheios embedded library dependencies failed: ${e}`)
                })
            }).catch(e => {
                console.error(`Import of Alpheios Embedded library failed: ${e}`)
            })
            });
        </script>
    </body>
    </html>
    """

    with open(SRC) as f:
        with open(DEST, "w") as g:
            prev_section = None
            prev_chapter = None
            print(HEADER, file=g)
            for line in f:
                parts = line.strip().split(maxsplit=1)
                ref = parts[0].split(".")
                if len(ref) == 2:
                    section = None
                    chapter, verse = ref
                else:
                    section, chapter, verse = ref
                if prev_section != section:
                    if prev_section is not None:
                        print("   </div>""", file=g)
                        print("   </div>""", file=g)
                    print("""   <div class="section">""", file=g)
                    prev_section = section
                    prev_chapter = None
                if prev_chapter != chapter:
                    if prev_chapter is not None:
                        if prev_chapter == "0":
                            if section is None:
                                print("""    </div>""", file=g)
                        else:
                            print("""    </div>""", file=g)
                    if chapter == "0":
                        if section is None:
                            print("""    <div class="preamble">""", file=g)
                    else:
                        if chapter == "title":
                            print("""    <div class="subscription">""", file=g)
                        elif chapter == "subtitle":
                            print("""    <div class="epilogue">""", file=g)
                        else:
                            if not chapter == "text":
                                print("""    <div class="chapter">""", file=g)
                                print(f"""      <h3 class="chapter_ref">{chapter} {parts[1]}</h3>""", file=g)
                            else:
                               print("""    <div class="chapter">""", file=g) 
                    prev_chapter = chapter
                    next
                if chapter == "0" and verse == "0":
                    print(f"""    <h2 class="section_title">{parts[1]}</h2>""", file=g)
                else:
                    if chapter != "0" and verse == "0":
                        print(f"""<h3 class="epilogue_title">{parts[1]}</h3>""", file=g)
                    else:
                        # HANDLE VERSE
                        if not (verse == "title" or chapter == "0" or chapter == "text"):
                            print(f"""      <span class="verse_ref">{verse}</span>""", end="&nbsp;", file=g)
                            print(parts[1], file=g)
                            print(f"""      <br/>""", file=g)
                        else:
                            if chapter == "text":
                                print(f"""   <p>{parts[1]}</p>""", file=g)

            print("""    </div>""", file=g)

            if section is not None:
                print("""    </div>""", file=g)
            print(FOOTER, file=g)

