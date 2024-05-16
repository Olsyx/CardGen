# CardGen
Generate cards in bulk for your TTRPGs! 

Have you ever needed to generate a hundred cards that looked all the same (or almost!)? 

I have!

And I couldn't find a way that did not involve spending a thousand hours, tirelessly customizing card after card, using something like Photoshop or Gimp.

So I came up with this! Using CardGen, you can input **templates** and **data sets**, and the program will do the rest! 

Templates are highly customizable, but what if that specific card has a name that is just _a tad_ too big for that title box? 

No worries, I got you! 

Data sets can override anything in a template if needed, or even adapt the space they take up based on surrounding elements.

See more in the How to use section!

## Dependencies
I'm working on a web solution so we do not have to run anything in our computers, but until then, this is what you will need: 

- Python - I'm using 3.10.11, but any version will probably work!
- PIL (pillow)
- urllib3
- Selenium, using the Chrome web driver - but you may change the driver in the WebBrowser.py file.
- pdfimages - for pdf image and font extraction.

## How to use
Open a command shell and run:

`python card-gen.py <output_folder> <template_file> <data_file>`

Optionally, you can name the resulting HTML file by appending its name at the end:

`python card-gen.py <output_folder> <template_file> <data_file> "index"`

Adding `--debug` at the end will enable debug mode.
Adding `--sort` or `--sorted` at the end will sort cards by their type name.

You can add both flags in any order (either `--debug --sort` or `--sort --debug`).

If you add any flags, specifying an HTML name becomes mandatory.

After executing this command, a new browser window will appear. I have chosen Chrome because that is what I use in my day to day, but feel free to modify WebBrowser.py to work with your own. 

That's all! Now you can open your template and data set, and modify them. The browser will show you all your cards filled in the templates, and it will refresh live as you make your changes!

Once you are done, press Ctrl+P to generate a PDF and print away!

Closing the browser window will also stop the running process.

## Templates & Data Sets
This section is WIP! There's lots of stuff in there. I intend to make a full wiki about it, stay tuned!

## Future Work
These are a number of features I would like to add to this tool in the future:
- Better flag handling for the main command.
- Selectable browser through a settings.json, maybe?
- Making it a web, so you don't have to run it in your PC.


