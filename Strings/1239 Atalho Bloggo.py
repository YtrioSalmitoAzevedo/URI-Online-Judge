def shortcutBloggo( str ):
    ci=0;cb=0
    for j in range(len(str)):
        if str[j] is "*":
            if cb % 2 == 0:
                str[j]="<b>"
            else:
                str[j]="</b>"
            cb+=1
        if str[j] is "_":
            if ci % 2 == 0:
                str[j]="<i>"
            else:
                str[j]="</i>"
            ci+=1
    return "".join(str)

while True:
    try:
        print shortcutBloggo(list(raw_input()))
    except:
        break