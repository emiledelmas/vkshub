from django import template

register = template.Library()


@register.simple_tag
def list_index(mylist,index):
    return mylist[index]


@register.simple_tag
def truncatebegin(word, index):
    return word[index:]


@register.simple_tag
def percent(number):
    return 100-(number*2)

@register.simple_tag
def onetwo(number):
    if number%2 == 0:
        return '<li class="comment user-comment">'
    else:
        return '<li class="author user-comment">'


@register.simple_tag
def percent2(number):
    return number*2

@register.simple_tag
def replace(name):
    return name.replace(" ", "_")

@register.simple_tag
def date(name):
    if name[5:7] == '01':
        month = 'Janvier'
    elif name[5:7] == '02':
        month = 'Fevrier'
    elif name[5:7] == '03':
        month = 'Mars'
    elif name[5:7] == '04':
        month = 'Avril'
    elif name[5:7] == '05':
        month = 'Mai'
    elif name[5:7] == '06':
        month = 'Juin'
    elif name[5:7] == '07':
        month = 'Juillet'
    elif name[5:7] == '08':
        month = 'Août'
    elif name[5:7] == '09':
        month = 'Septembre'
    elif name[5:7] == '10':
        month = 'Obtobre'
    elif name[5:7] == '11':
        month = 'Novembre'
    elif name[5:7] == '12':
        month = 'Décembre'   
    name = name[8:10] + ' ' + month + ' ' + name[0:4]
    return name



@register.simple_tag
def graph_main(array, month):
    if month < 10:
        month = '0'+str(month)
    else:
        month = str(month)
    count = array.count(month)
    outofhundred = count*10
    print(outofhundred)
    return str(outofhundred)


@register.simple_tag
def list_index_cut(mylist,index):
    el = mylist[index]
    if el == 'application/x-msdownload':
        return 'windows'
    elif el == 'application/pdf':
        return 'file-pdf-o'
    elif el == 'application/pdf':
        return 'file-pdf-o'
    elif el == 'application/zip' or el == 'application/x-rar-compressed' or el == 'application/x-7z-compressed' :
        return 'file-archive-o'
    elif el == 'application/x-sqlite3':
        return 'database'
    elif el == 'application/font-woff' or el == 'application/font-sfnt':
        return 'font'
    elif el.split('/')[0] == 'audio':
        return 'music'
    elif el.split('/')[0] == 'epub+zip':
        return 'book'
    elif el.split('/')[0] == 'image':
        return 'image'
    elif el == 'code':
        return 'code'
    elif el == 'excel':
        return 'file-excel-o'
    elif el == 'word':
        return 'file-word-o'
    elif el == 'css3':
        return 'css3'
    elif el == 'excel':
        return 'file-excel'
    elif el == 'presentation':
        return 'file-powerpoint-o'
    elif el == 'html5':
        return 'html5'
    elif el == 'settings':
        return 'settings'
    elif el == 'android':
        return 'android'
    elif el == 'chart-area':
        return 'table'
    elif el == 'file-csv':
        return 'file-csv'
    elif el.split('/')[0] == 'video':
        return 'film'
    else:
        return 'file'

@register.simple_tag
def tentime(number):
    number = int(number)
    return 10*number