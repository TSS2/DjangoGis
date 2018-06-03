$(document).ready(function(){

    $('#register_btn').click(function(){
        var name = $('#username').val();
        var password = $('#password').val();
        var phone = $('#phone').val();

        $.post('/register/',{'name':name,'password':password,'phone':phone},function(){
            
        })
    });

    $('#store_id').click(function(){
        // var context = $('#store_id').text();
        // $.post('/message_manage/',{'context':context},function(data){
        //     data = JSON.parse(data);
        //     $('#second_daohang').text(data['context']);
        // })
    });
    $('#food_id').click(function(){
        // var context = $('#food_id').text();
        // $.post('/message_manage/',{'context':context},function(data){
        //     data = JSON.parse(data);
        //     $('#second_daohang').text(data['context']);
        // })
    });
    $('#community_id').click(function(){
        // var context = $('#community_id').text();
        // $.post('/message_manage/',{'context':context},function(data){
        //     data = JSON.parse(data);
        //     $('#second_daohang').text(data['context']);
        // })
    });
    $('#message_id').click(function(){
        // var context = $('#message_id').text();
        // $.post('/message_manage/',{'context':context},function(data){
        //     data = JSON.parse(data);
        //     $('#second_daohang').text(data['context']);
        // });
    });
    $('#gis_store_id').click(function(){
        var context = $('#gis_store_id').text();
        $.post('/gis/',{'context':context},function(){

        })
    });
    $('#gis_food_id').click(function(){
        var context = $('#gis_food_id').text();
        $.post('/gis/',{'context':context},function(){
            
        })
    });
    $('#gis_community_id').click(function(){
        var context = $('#gis_community_id').text();
        $.post('/gis/',{'context':context},function(){          
            
        })
    });
    $('#gis_message_id').click(function(){
        
    });

    //信息采集员查看菜品信息
    var id =0;
    $('td > a').bind({
        mouseenter:function(){
            id = $(this).attr('id')
            // alert(id)
        },
        mouseleave:function(){

        },
        click:function(){
            if (id.search('d') == -1){
                layer.open({
                type: 2,    // iframe窗口
                title: '查看菜品',
                area: ['600px', '360px'],
                shadeClose: true, //点击遮罩关闭
                content: "/mygis/marketfoodshow/?id="+id
              });
            }
            if (id.search('d') > -1){
                layer.open({
                type: 2,    // iframe窗口
                title: '添加菜品',
                area: ['600px', '360px'],
                shadeClose: true, //点击遮罩关闭
                content: "/mygis/marketfoodadd/?id="+id
              });
            }
            
        }
    });
  
})