from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .models import ACTION
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

    # conn = df.sqlite3.connect("db.sqlite3")
    if action_id == 1:
        list = []
        rm = df.visa.ResourceManager()
        # conn = df.sqlite3.connect('db.sqlite3')
        reading = rm.list_resources()
        for item in reading:
            try:
                inst = rm.open_resource(item)
                id = inst.query("*IDN?")

                str = "Hello, I am " + id
                list.append(str)
            except BaseException:
                print(f"{item} is not reachable.")
                list.append(item + " is not reachable")
        rm.close()

    # for item in list

        # conn.close()

        # conn.execute('''insert into manual_equipment(id, equipment_name)
        #                  values(?,?)''', (1, id)
        #             )
        # conn.commit()

        return HttpResponse(list)

    elif action_id == 2:
        return HttpResponse("You are looking at hehe")

    else:
        return HttpResponse("You are looking at haha")






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
