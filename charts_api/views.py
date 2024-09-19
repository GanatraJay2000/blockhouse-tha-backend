from rest_framework.response import Response
from rest_framework.decorators import api_view
from .raw_data import candlestick_chart, line_chart, bar_chart, pie_chart, allData


@api_view(['GET'])
def candlestick_data(request):
    data = candlestick_chart
    return Response(data)


@api_view(['GET'])
def line_chart_data(request):
    data = line_chart
    return Response(data)


@api_view(['GET'])
def bar_chart_data(request):
    data = bar_chart
    return Response(data)


@api_view(['GET'])
def pie_chart_data(request):
    data = pie_chart
    return Response(data)


@api_view(['GET'])
def all_data(request):
    data = allData
    return Response(data)
