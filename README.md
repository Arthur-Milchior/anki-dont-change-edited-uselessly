# "Edited" value not updated unless there is really an edition
This add-on is depretaced !!!

It seems it is correcting a bug I imagined and which never existed.

I don't understand why.

Keeping it online until I make sens of it.


## Rationale
The value "edited" is supposed to show the last time a note was
edited. The trouble here being that the card is assumed to be edited
as soon as it has been shown in the browser/editor.  (More precisely,
as soon as you clicked on a field of the note). 

Sometime, I see card in the browser but don't actually edit them; in
this case, I would really like the "edited" value not to change. This
is what this add-on does.

As a side effect, cards are displayed longer in the reviewer. Card
used to be removed from the reviewer because Anki believed falsely
that the note was updated. Since it does not believe it, it keep
showing the card.

## Warning
The value may still be updated uselessly by other means. This add-on
only deal with wrong update in editor/browser.

## Internal
This add-on replace the methods:
* aqt.Editor.onBridgeCmd
* aqt.Editor.saveTags

## Version 2.0
None


## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-dont-change-edited-uselessly
Addon number| [153450853](https://ankiweb.net/shared/info/153450853)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
