![image](https://github.com/user-attachments/assets/082ce04e-4506-449c-aa71-c4a547fb77b0)

A fun python text encoder/decoder for a cipher i invented that uses morse-code based rules.
Perfect for:
- Learning and practicing Morse-Code
- Secret Messages/Notes
- Confusing people

---
## ⭐ What is Morse Code? ⭐

Before you understand this cipher, you have to generally understand how morse code works. 

Morse code was invented my Samuel Morse for communicating long distances using the telegraph. In Morse Code, every single letter is made up of 'Dots' and 'Dashes'. For example, the world "Hello" would be ".... . .-.. .-.. ---". Using this system, you can communicate in english soley using dots and dashes- even though its a little slower.

## ⭐ How My Cipher Works ⭐

Morse code is very well known and recognizable- so for my cipher, I wanted to use the same idea, but make it unrecognizable.

For my cipher, every letter in the english 'abc' alphabet is assigned to either a 'dash' category or a 'dot' catergory. The factor that determines which category they are in is based on how the letter looks while in lowercase.
- A Dot (`.`) is assigned a random letter from: `aweiruoszxcvnm`. These are all the short looking letters in the alphabet.
- A Dash (`-`) is assigned a random letter from: `qtypdfghjklb`. These are all the long looking letters with "tails" or "necks".
For example, in morse code '-..' is the letter 'd'. In my cipher if you entered '-..' it could return something like 'bio', 'puu', 'lnm', 'qia,' etc.

Then for readability and to show where a letter starts and ends:
- Every "word" is separated by a comma, and Morse-character letters are separated by a space.
An example:
- The word "cat" in my cipher could be "dilo ml q"
- The sentence "cat in the hat" could be "dilo ml q, mn po, b oiua e, eeim ol d"

To decode, the program reverses this process using the categories to re-identify dots and dashes, then matches them to the original letters in morsecode.

To someone that doesnt know the cipher, all of this will look like absolute gibberish. But, a trained eye that knows morse code can read it!

---

## ⭐ Usage ⭐

Commands:
- Encode (e) a plain english word or phrase into gibberish 

- Decode (d) gibberish back into readable English (if you're decoding a phrase, make sure to put commas between the words or itll all blend together!)

- View (m) the Morse code letter reference

- Quit (q) the program


Run the script:

```bash
python morsedecoder.py







