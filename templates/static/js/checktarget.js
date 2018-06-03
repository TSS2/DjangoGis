$(document).ready(function(){
    $('#page').hide()
    $('#pages').hide()
    $('#market_name').hide()
    $('td > a').click(function(){
        var task_id = $(this).attr('id')
        var page = $('#page').text()
        var pages = $('#pages').text()
        var market_name = $('#market_name').text()
        $.post('/mygis/marketdetailasses/?page='+page+'&market_name='+market_name+'&pages='+pages,{'task_id':task_id},function(data){          
            alert(data)
        })
    })
})