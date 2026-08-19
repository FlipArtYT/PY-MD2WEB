# 📝 PY-MD2WEB
A static website generator that converts Markdown files to HTML files.

## ⭐️ Main Features
- [ ] Multiple webpage themes (using CSS stylesheets)
- [ ] Easily convert multiple webpages from a folder and maintain their original file structure
- [x] Custom navigation bar syntax 
- [ ] Custom text styling syntax (foreground color, background color, font)"

## 🎨 Themes
- [x] `Readme Pro` - Github README like theme
- [ ] `Superminimal` - Extremely minimalistic, white on pure black
- [ ] `XT Simplistic` (Color Variants) - Simple, flat and modern theme
- [ ] `alnwlsn-style` (Color Variants) - Simple styling, big padding inspired by [alnwlsn's website](https://alnwlsn.com/)

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