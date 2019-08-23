from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .models import ACTION, EQUIPMENT
from manual import definition as df
from django.http import Http404


def index(request):
    output = ACTION.objects.all()
    # output = ','.join([a.action_name for a in ACTION.objects.all()])
    # return HttpResponse(output)
    template = loader.get_template('manual/index.html')
    context = {
        'output': output,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'manual/index.html', context) # shortcut using render

def detail(request, action_id):

    conn = df.sqlite3.connect("db.sqlite3")

    if action_id == 1:
        list1 =[]; list2 = []; i = 0
        rm = df.visa.ResourceManager()
        # conn = df.sqlite3.connect('db.sqlite3')
        reading = rm.list_resources()
        for item in reading:
            try:
                inst = rm.open_resource(item)
                id = inst.query("*IDN?")
                list1.append(item)
            except BaseException:
                list2.append(item)
        rm.close()

        for item in list1:
            conn.execute(''' update manual_equipment set equipment_yes = ? where id = ?  ''',
            (list1[i], i+1)
                         )
            # conn.execute('''insert into manual_equipment(id, equipment_yes)
            #              values(?,?)''', (i+3, 'null')
            #              )
            i += 1
            conn.commit()
        conn.close()

        output = EQUIPMENT.objects.all()
        # output = ','.join([a.action_name for a in ACTION.objects.all()])
        # return HttpResponse(output)
        template = loader.get_template('manual/detail.html')
        context = {
            'output': output,
        }
        # return HttpResponse(template.render(context, request))
        return render(request, 'manual/detail.html', context) # shortcut using render





        # return HttpResponse(f"equipment found:{list1}, equipment not reachable:{list2}")

    elif action_id == 2:
        return HttpResponse("You are looking at hehe")

    else:
        return HttpResponse("You are looking at haha")

def vote(request, equipment_id):
    return HttpResponse("You are looking at hehe")




    # inst = rm.open_resource('TCPIP0::10.0.22.24::inst0::INSTR')
    # reading = inst.query("*IDN?")
    # conn.execute("insert into SPECAN(id, read) values(?,?)", (1, inst.query("*IDN?"))
    # conn.commit()
    # conn.close()








    # try:
    #     action = ACTION.objects.get(pk=action_id)
    # except ACTION.DoesNotExist:
    #     raise Http404("ACTION does not exist")
    #
    # return render(request, 'manual/detail.html', {'action':action})
