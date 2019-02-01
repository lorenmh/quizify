# Future Dev
* Rewrite in python
* Dir of input words
* Sqlite
* Built in import from Kindle, text files

## Outline
* For each word in input, insert into sqlite (optional import?)
* For quizing, select a word at random
* If word doesn't have a definition, use API call to get definition, etymology, roots, synonyms, pronunciation
* Ask for user definition, get text input for synonyms, definition, or select option for "I know this" "I don't know this"
   * Example: "histrionics" -> user inputs "theatrical display" -> outputs "Definition: XXX (etymology, etc). You said: "theatrical display", correctness 1-5" -> user inputs 5, or, another option to select that this word is known and no longer needs to be quizzed
* store all of this in DB
* quiz word selection based on correctness\_factor, last\_time\_quizzed, and randomness
* quiz until exit
