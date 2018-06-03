  
  $(document).ready(function(){
    // 信息采集员添加小区人口信息
  
    var id =0;
      $('td > a').bind({
          mouseenter:function(){
              id = $(this).attr('id')
                // alert(id.search('d'))
                // alert(id)
          },
          mouseleave:function(){
  
          },
          click:function(){
              if (id.search('d')){
                  layer.open({
                  type: 2,    // iframe窗口
                  title: '添加人口',
                  area: ['600px', '360px'],
                  shadeClose: true, //点击遮罩关闭
                  content: "/mygis/marketpeopleadd/?id="+id
                });
              }
              
          }
      });
    $('div > a').click(function(){
      var num = $('#num_input').val()
      var id = $('a').attr('id')
      $.post('/mygis/marketpeopleadd/?id='+id,{'id':id,'people_num':num},function(){          
        // somthing
        alert('success')
      })
  
  })
  })