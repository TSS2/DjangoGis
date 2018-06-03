  
  $(document).ready(function(){
    // 信息采集员添加小区人口信息
  
    var id =0;
      $('button').bind({
          mouseenter:function(){
              id = $(this).attr('id')
          },
          mouseleave:function(){
  
          },
          click:function(){
              if (id.search('d')){
                  layer.open({
                  type: 2,    // iframe窗口
                  title: '添加流量及摊位',
                  area: ['600px', '360px'],
                  shadeClose: true, //点击遮罩关闭
                  content: "/mygis/markettanweiadd/?id="+id
                });
              }
              
          }
      });
    $('div > a').click(function(){
      var people_flow = $('#people_flow').val()
      var tanwei_num = $('#tanwei_num').val()
      var tanwei_use_num = $('#tanwei_use_num').val()
      var id = $('a').attr('id')
      $.post('/mygis/markettanweiadd/?id='+id,{'people_flow':people_flow,'tanwei_num':tanwei_num,'tanwei_use_num':tanwei_use_num},function(){          
        // somthing
      })
  
  })
  })