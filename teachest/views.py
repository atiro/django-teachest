from django.shortcuts import render, render_to_response
import influxdb
import json
from teagraphs.forms import TeaForm

# Create your views here.

def addtea(request):
        client = influxdb.InfluxDBClient('HOSTNAME', 8086, 'USER', 'PASS', 'DB')

        form = TeaForm()

        if request.method=='POST':
            form = TeaForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                client = influxdb.InfluxDBClient('HOSTNAME', 8086, 'USER', 'PASS', 'DB')
                json = [
                    { "points": [
                        [   cd["maker"], cd["quantity"] ,
                            cd["type"], cd["sprint"],
                            2015
                        ]
                    ], "name": "made",
                       "columns": ["maker", "cups", "type", "sprint", "year"]}]

                client.write_points(json)

            form = TeaForm()

        data = {
                'form': form,
        }

        data.update(teamakers(client))
        data.update(teadaily(client))
        data.update(teasprint(client))
        data.update(teatypes(client))

        return render(request, 'teagraphs/tea.html', data)

def teamakers(client):
        # Tea Makers PieChart
        results = client.query('select sum(cups) from made where year = 2015 group by maker')
        xdata = [x[2] for x in results[0]["points"]]
        ydata = [x[1] for x in results[0]["points"]]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'tm_container'
        graph = {
                    'tm_chartdata': chartdata,
                    'tm_charttype': charttype,
                    'tm_chartcontainer': chartcontainer,
                    'tm_extra': {
                        'x_is_date': False,
                        'x_axis_format': '',
                        'tag_script_js': True,
                        'jquery_on_ready': False,
                    }
                 }

        return graph

        #return render_to_response('teagraphs/teamakers.html', data)
        return (chartdata, charttype, chartcontainer)

def teadaily(client):

        results = client.query('select sum(cups) from made where year = 2015 group by time(1d) fill(0)')
        xdata = [x[0]*1000 for x in results[0]["points"]]
        ydata = [x[1] for x in results[0]["points"]]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "discreteBarChart"
        chartcontainer = 'td_container'
        graph = {
                'td_charttype': charttype,
                'td_chartdata': chartdata,
                'td_chartcontainer': chartcontainer,
                'td_extra': {
                    'x_is_date': True,
                    'tag_script_js': True,
                    'jquery_on_ready': False
                    }
                }

        return graph
        #return render_to_response('teagraphs/teadaily.html', data)

def teasprint(client):
        results = client.query('select sum(cups) from made where year = 2015 group by sprint fill(0)')
        xdata = [x[2] for x in results[0]["points"]]
        ydata = [x[1] for x in results[0]["points"]]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "discreteBarChart"
        chartcontainer = 'ts_container'
        graph = {
                'ts_charttype': charttype,
                'ts_chartdata': chartdata,
                'ts_chartcontainer': chartcontainer,
                'ts_extra': {
                    'x_is_date': False,
                    'tag_script_js': True,
                    'jquery_on_ready': False
                    }
                }

        #return render_to_response('teagraphs/teasprint.html', data)
        return graph

def teatypes(client):
        results = client.query('select sum(cups) from made where year = 2015 group by type')
        xdata = [x[2] for x in results[0]["points"]]
        ydata = [x[1] for x in results[0]["points"]]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'tt_container'
        graph = {
                'tt_charttype': charttype,
                'tt_chartdata': chartdata,
                'tt_chartcontainer': chartcontainer,
                'tt_extra': {
                    'x_is_date': False,
                    'x_axis_format': '',
                    'tag_script_js': True,
                    'jquery_on_ready': False,
                    }
        }

        return graph


def teastrength(request):
        pass
