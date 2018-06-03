  
  $(document).ready(function(){
  // 信息采集员添加菜品信息

  var id =0;
    $('button').bind({
        mouseenter:function(){
            id = $(this).attr('id')
            // alert(id)
        },
        mouseleave:function(){

        },
        click:function(){
            // if (id.search('d') == -1){
            //     layer.open({
            //     type: 2,    // iframe窗口
            //     title: '查看菜品',
            //     area: ['600px', '360px'],
            //     shadeClose: true, //点击遮罩关闭
            //     content: "/mygis/marketfoodshow/?id="+id
            //   });
            // }
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
  $('div > a').click(function(){
    var food = $('#food_input').val()
    var price = $('#price_input').val()
    var id = $('a').attr('id')
    $.post('/mygis/marketfoodadd/?id='+id,{'food':food,'price':price},function(){          
        alert('success')
    })

})
})