# 📝 PY-MD2WEB
![Static Badge](https://img.shields.io/badge/Python-3.14-e9f23d?logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Jinja2-red?style=flat&logo=Jinja&labelColor=black)
<br>
A static website generator that converts Markdown files to HTML files.

## ⭐️ Main Features
- [x] Multiple webpage themes (using CSS stylesheets)
- [x] Easily convert multiple webpages from a folder and maintain their original file structure
- [x] Custom navigation bar syntax 
- [ ] Custom text styling syntax (foreground color, background color, font)

## ⚙️ Requirements
- `markdown` (pip)
- `jinja2` (pip)

## 🚀 Running the script
```
python3 md2web/main.py [--input-path] [--output-path] [--theme-name]
```

## 🎨 Themes
- [x] `Readme Pro` - Github README like theme
- [x] `Superminimal` - Extremely minimalistic, white on pure black
- [ ] `XT Simplistic` (Color Variants) - Simple, flat and modern theme
- [x] `alnwlsn` (Color Variants) - Simple styling, big padding inspired by [alnwlsn's website](https://alnwlsn.com/)

## Custom Syntax
### Navigation bar
> [!WARNING]
> Multiple navigation bars currently do not get handled correctly. Please only use one navigation bar per file to avoid unexpected behaviour.
```
:::
- [Link 1](https://website1.com/);
- [Link 2](https://website2.com/);
- [Link 3](https://website3.com/);
:::
```