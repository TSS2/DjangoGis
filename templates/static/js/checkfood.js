$(document).ready(function(){
    // alert('hello')
    
    $('#page').hide()
    $('#market_name').hide()
    $('td > a').click(function(){
        var task_id = $(this).attr('id')
        var page = $('#page').text()
        var market_name = $('#market_name').text()
        $.post('/mygis/marketdetail/?page='+page+'&market_name'+market_name,{'task_id':task_id},function(){          
            alert('success')
        })
    })
})