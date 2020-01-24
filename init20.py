from aqt.editor import *

def saveTags(self):
    if not self.note:
        return
    tagsTxt = unicodedata.normalize("NFC", self.tags.text())
    tagsTxt = self.mw.col.tags.canonify(self.mw.col.tags.split(tagsTxt))
    if self.note.tags != tagsTxt:
        self.note.tags = tagsTxt
        self.tags.setText(self.mw.col.tags.join(self.note.tags).strip())
        if not self.addMode:
            self.note.flush()
        gui_hooks.editor_did_update_tags(self.note)
    
def onBridgeCmd(self, cmd) -> None:
    if not self.note:
        # shutdown
        return
    # focus lost or key/button pressed?
    if cmd.startswith("blur") or cmd.startswith("key"):
        (type, ord, nid, txt) = cmd.split(":", 3)
        ord = int(ord)
        try:
            nid = int(nid)
        except ValueError:
            nid = 0
        if nid != self.note.id:
            print("ignored late blur")
            return
        txt = unicodedata.normalize("NFC", txt)
        txt = self.mungeHTML(txt)
        # misbehaving apps may include a null byte in the text
        txt = txt.replace("\x00", "")
        # reverse the url quoting we added to get images to display
        txt = self.mw.col.media.escapeImages(txt, unescape=True)
        if self.note.fields[ord] != txt:
            self.note.fields[ord] = txt
            if not self.addMode:
                self.note.flush()
                self.mw.requireReset()
        if type == "blur":
            self.currentField = None
            # run any filters
            if gui_hooks.editor_did_unfocus_field(False, self.note, ord):
                # something updated the note; update it after a subsequent focus
                # event has had time to fire
                self.mw.progress.timer(100, self.loadNoteKeepingFocus, False)
            else:
                self.checkValid()
        else:
            gui_hooks.editor_did_fire_typing_timer(self.note)
            self.checkValid()
    # focused into field?
    elif cmd.startswith("focus"):
        (type, num) = cmd.split(":", 1)
        self.currentField = int(num)
        gui_hooks.editor_did_focus_field(self.note, self.currentField)
    elif cmd in self._links:
        self._links[cmd](self)
    else:
        print("uncaught cmd", cmd)
Editor.onBridgeCmd = onBridgeCmd
Editor.saveTags = saveTags
