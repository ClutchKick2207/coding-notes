# Some info on MarkDown before I begin:

---

Markdown is the most popular markup language used to make all sorts of things, such as e-mails, essays, and other documents. It is completely open-source, and also does not lock you into any specific editor or file format. It can be used on any OS, through applciations made purely for it, and also through editors through extensions. It can also use HTML snippets to allow for some extensibilty. If you want some serious horsepower for graphs, and other tools, use RMarkDown, which integrates R into the MarkDown process. I'll probably dabble into that if I ever need to use some serious graphing.

## Why MarkDown?

This is a question that I have been asking myself for a bit, but it allows for a distraction free way to write down something quickly, and make it look aesthetically pleasing. It can then be exported into a document that can be shared easily (such as a PDF). This can also be done to make efficient notes (through applications such as Notion, as well as your editor of choice and Git).

# A Guide to MarkDown

-----

Now I will break down the basics of MarkDown, and who knows, maybe I'll throw in some cool stuff as well.

## Using HTML:

Throughout this document, you may have seen some HTML, such as `<br>`. Different rendering engines will render this differently, but GitHub's and many others, will have syntax highlighting enabled. To activate this, write the name of the programming language with the opening part, like below

```python
print("Hello, World!")
```

## The Different Headings:

These headings can be used to signify different levels (such as points, sub-points, chapters, etc.). For best practice, have a space betwen the '#' and the first character.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Paragraphs:

Paragraphs do not require any special formatting, just typing gets it to work.

## **Bold** and _italics_ and ~~strikethrough~~:

To **Bold** a phrase/sentence but '**' infront and behind the piece of text. To use _italics_ put underscores infront and behind the text. ~~Strikethrough~~ is donw by putting 2 tildes before and after the text. You can also do all three simultaneously, such as **_~~Bold and Italic and Strikethrough~~_**, by just adding in all three.

## Different Lists:

Lists are often used in MarkDown during note-taking, and can be beneficial to summarize any points.

### Unordered Lists:

- This is a list , it is cool
- This is also unordered, and uses bullet points

### Ordered Lists:

1. This is an ordered list, it is cool
2. It also is able to make pretty shopping lists

### Layered Lists:

- This is a layered list
  
  - You are able to make sub-lists for each point
    - Layers can be navigated through the use of 'tab' and 'backspace'
1. The same thing can be done using an ordered list
   1. It works in the same way
   2. But now you have numbers
      1. That you can make into cool things

## Quotes

> "This is a block-quote, it is made using '>'"
> 
> You can make them have multiple lines

## Links

Links are done with this syntax:

[Link text] (URL):

[Google - The Search Engine](google.com)

A random image:

![Google Search Engine](https://th.bing.com/th/id/R54e7b473441b8183e37c8ce05ca60f93?rik=mx7TsuLeaAN%2bkw&riu=http%3a%2f%2fbpi-canada.com%2fwp-content%2fuploads%2f2014%2f11%2fLaboratory_Technology-_Testing.jpg&ehk=c90c0rML%2b%2bKiZIcocQ9IKAqeSJfeL4Kv1iFV6Jw%2fb40%3d&risl=&pid=ImgRaw)
