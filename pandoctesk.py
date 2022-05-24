from sys import stderr
import panflute

headers = []

def upperHeaders(i, doc):
    if isinstance(i, panflute.Header):
        if i.level <= 3:
            return panflute.Header(panflute.Str(panflute.stringify(i).upper()), level=i.level)

def replaceBold(doc):
    doc.replace_keyword('BOLD', panflute.Strong(panflute.Str('BOLD')))

def findSimHeaders(i, doc):
    if isinstance(i, panflute.Header):
        if panflute.stringify(i) in headers:
            stderr.write(f"Внимание: Текст уже содержит заголовок {i}!\n")
        else:
            headers.append(panflute.stringify(i))

if __name__ == '__main__':
    panflute.run_filters([upperHeaders, findSimHeaders], prepare=replaceBold)
