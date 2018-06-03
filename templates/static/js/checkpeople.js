$(document).ready(function(){
    // alert('hello')
    
    $('#page').hide()
    
    $('td > a').click(function(){
        var task_id = $(this).attr('id')
        var page = $('#page').text()
        
        $.post('/mygis/querycommunitymessage/',{'task_id':task_id},function(){          
            alert('success')
        })
    })
})