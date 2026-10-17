# SVN

## SVN

Die Abkürzung SVN steht für [Subversion](http://de.wikipedia.org/wiki/Subversion_%28Software%29). Dabei handelt es sich um eine [Versionsverwaltung](http://de.wikipedia.org/wiki/Versionsverwaltung) für Quellcodes von Software dient. Die alternative Firmware [Boop](Boop.md "Boop") verwendet ein SVN Repository (=Projektarchiv) zum verwalten des ihres Quelltextes.

Der Quelltext kann auf der [Sourceforge Projektseite](http://boopfirmware.svn.sourceforge.net/) im Browser betrachtet werden. Für arbeiten am Quelltext (Patches, Mods, ...) wird der Download per SVN-Client empfohlen.

## Quelltext Download

### Linux (Ubuntu)

Via Terminal:  
ggf. Subversion installieren:

    $ sudo apt-get install subversion

Download (checkout) in ein Unterverzeichnis namens *boopfirmware*:

    $ svn checkout svn://svn.code.sf.net/p/boopfirmware/code/boop/trunk boopfirmware

### Windows

- z.b. <http://tortoisesvn.tigris.org/>

### MacOS

- tba

---

[Startseite](Main%20Page.md) · [Index](../index.md) · [Kategorien](../categories.md)

