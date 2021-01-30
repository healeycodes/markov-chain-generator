# markov-chain-generator

Use this library to generate random realistic text via Markov chain models.

<br>

See the example by running `python generate.py`.

<br>

Pass in a corpus, a state size, and a minimum length. Make sure the corpus uses capital letters and full-stops.

```python
state_size = 2
length = 100
source = get_source('poe') # or some corpus as a string
poe = build_model(source, state_size)
text = generate_text(poe, state_size, 100)
print(text)

'''
And really between two and three, there is no comfortable feeling. But the little spalpeen Mounseer Maiter-di-dauns that plumped his silf right down by the pond. Upon his own house, when wit and jollity reigned supreme-dampened a little, of course, expressed in regard to his conscience and himself. But although Hop-Frog, through the nose; the intestines through an avenue two miles long, and might have been a little amused. When we had great reason to congratulate ourselves upon our good fortune. Approaching the table, and in the way of indemnification inserted his left thumb in the external world, when, with many a fine thing.
'''
```

<br>

<sub>The Edgar Allen Poe and Oscar Wilde text corpuses were taken from https://github.com/nlp-compromise/nlp-corpus and I'm unsure of their license. The code is MIT.</sub>
