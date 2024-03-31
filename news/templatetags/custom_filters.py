from django import template


register = template.Library()


@register.filter()
def censor(text):
    try:
        censorship = ['редиска', 'Редиска']
        for cens in censorship:
            text = text.replace(cens, f"{cens[0]}" + ''.join(["*" for i in cens[1:]]))
        return text
    except AttributeError:
        print("Ошибка атрибута ожидается тип str")
        return text



