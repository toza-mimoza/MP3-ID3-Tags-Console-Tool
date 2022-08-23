# MP3-ID3-Tags-Console-Tool

A console tool for setting artist and title MP3 tags (ID3 v2.3) tags directly from file names. The tool also sets the covers for MP3 files.

File names need to have the following pattern: 

- `[artist] - [title].mp3` **(notice the whitespaces around the '-' character)**

If this pattern is not found in the file name, the tool will ask the user to submit the appropriate artist and the file name of the song as title suggestion. 

If there is no present tag for the cover, the tool will first ask if a cover is needed with `'yes'` as suggestion. Every other answer will skip setting the cover.

If answered with `'yes'`, tool will prompt the user for the cover file location using the an appropriate file manager window. The cover file as of now needs to be a PNG file. 

The tool changes the MP3 file name to the above pattern once the artist and title is known.

The exact usage of the tool can be retrieved using `--help` argument.

TO DO:
- [x] - Windows support
- [ ] - cover file can also be .jpg or .jpeg 