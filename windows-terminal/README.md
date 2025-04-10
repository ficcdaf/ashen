# Windows Terminal

1. Open `settings.json` from Windows Terminal.
2. In the `schemes` section of the file, paste the contents of.
   [ashen.scheme.json](https://git.sr.ht/~ficd/ashen/blob/main/windows-terminal/ashen.scheme.json).
3. Update `colorScheme` within the profiles section to use `ashen`.

```json
{
    "profiles": {
        "defaults": {
            "colorScheme": "ashen"
        }
    }
}
```
