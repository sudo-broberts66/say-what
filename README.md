# Say What

An interactive answer to one question: **why do we say "what?" when we already heard it?**

The short answer: your mouth has a deadline and your understanding doesn't. In conversation
you get about a fifth of a second to respond. When the meaning hasn't arrived by then, your
brain sends out the one word that needs no planning, and you finish decoding the sentence
from a few-second memory of its sound just after "what?" has left.

## The site

The site is two static pages at the root of this repository, with no dependencies beyond
web fonts.

| Page | What it is |
| --- | --- |
| [`index.html`](index.html) | The main page, the immersive version. Six scenes with sound: a staged dinner-table moment, the same three seconds in slow motion, a reaction test, "huh?" in eleven languages, three intonations of "what", and the sources. |
| [`text.html`](text.html) | The same answer as a single scrolling page, linked from the main one. |

To view it, open `index.html` in a browser. To host it with GitHub Pages, go to
**Settings → Pages**, choose **Deploy from a branch**, and pick the default branch with the
`/ (root)` folder.

The voices are generated in the browser by a small formant synthesizer. They carry the pitch
and vowel shape of each word and are not recordings of real speech.

## Editing

`index.html` and `text.html` are built files. Edit the sources in `src/` instead:

- `src/inside-what.html` is the source of `index.html`
- `src/say-what.html` is the source of `text.html`

Then rebuild:

```bash
python3 build.py
```

## Sources

The timings come from published research on conversation, listed on each page:
turn-taking gaps (Stivers et al., 2009), speech planning (Levinson & Torreira, 2015),
the timing of repair requests (Kendrick, 2015), echoic memory (Darwin, Turvey & Crowder,
1972), and "huh?" across languages (Dingemanse et al., 2013 and 2015). How the sliders
move the moment of understanding is a simplified model, and the pages say so.
