from aqt.reviewer import Reviewer
from anki.hooks import wrap

def hide_underline(self: Reviewer):
    self.bottom.web.eval("""

    const underlineStyle = document.createElement("style");
    underlineStyle.innerHTML = "u {text-decoration: none;}";
    document.body.appendChild(underlineStyle);
                         
    """)

Reviewer._initWeb = wrap(Reviewer._initWeb, hide_underline)