Hunspell dictionary for German, traditional orthography
=======================================================

This repository contains the dictionary and affixes files for use with
Hunspell.  They help spell checking documents in German with the traditional
orthography officially in use until 1996.

The files were derived from the files ``de_DE.dic`` and ``de_DE.aff`` contained
in the package ``hunspell-de-de`` of Ubuntu 20.04.  I back-ported them to the
traditional orthography:

1. Conversion from ISO-8859-1 to UTF-8.  This helps with various Hunspell bugs,
   e.g. https://github.com/hunspell/hunspell/issues/688 or using “ō” or “ſ” in
   documents.  It’s not a bad idea anyway.
2. ss → ß in many places.
3. Removal of support for the “Binnen-I”.
4. Application of the items of https://www.korrekturen.de/wortliste.shtml for
   migration to traditional orthography, with the following exceptions:

   - tripple consonants in all cases (“Betttuch”)
   - kept modern words (e.g. “Aftershave”)
