$(document).ready(function(){
    
    var raster = new ol.layer.Tile({
      source: new ol.source.XYZ({           //加载高德地图
        url:'http://webst0{1-4}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}'  
      })
    });
      
      var map = new ol.Map({
        target: 'map',
        layers: [raster
          // new ol.layer.Tile({
          //   source: new ol.source.XYZ({           //加载高德地图
          //     url:'http://webst0{1-4}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}'  
          //   })  
          // })
        ],
        view: new ol.View({
          // center: ol.proj.fromLonLat([103.98845,30.581839]),
          center: [11575931.700277366,3578569.073827034],
          zoom: 16
        }),
        controls: ol.control.defaults().extend([  //获取坐标点
        //   new ol.control.FullScreen(),   // 地图全屏控件
          new ol.control.MousePosition()   // 鼠标位置控件
        ]),
      });
    
     var view = map.getView();
     var zoom = view.getZoom();
     var map_center = view.getCenter();
    
    
     map.on('click',function(evt){  // 点击获取坐标
       x = evt.coordinate[0]
       y = evt.coordinate[1]
       $('#eX').val(x);
       $('#eY').val(y);
     });
    
     $('#btn_submit_01').click(function(){ // 添加菜市场信息 点击提交按钮 将位置信息传给后台 
       var province = $('#province2').val();
       var city = $('#city2').val();
       var district = $('#district2').val();
       var eX = $('#eX').val();
       var eY = $('#eY').val();
       var phone = $('#phone').val();
       var name = $('#name').val();
       if(eX==''||name==''||phone==''){
            alert('请完善信息')
            // $('#btn_submit_01').attr('disabled',true)
        }else{
            // $('#btn_submit_01').attr('disabled',false)
            $.post('/mygis/addmessage',{'province':province,'city':city,'district':district,'eX':eX,'eY':eY,'market_phone':phone,'market_name':name},function(){
                alert('成功')
            });
        }
     });
      
     
     $('#btn_submit_02').click(function(){ // 添加小区
        var province = $('#province2').val();
        var city = $('#city2').val();
        var district = $('#district2').val();
        var eX = $('#eX').val();
        var eY = $('#eY').val();
        var phone = $('#phone').val();
        var name = $('#name').val();
  
        if(eX==''||name==''||phone==''){
            alert('请完善信息')
            // $('#btn_submit_02').attr('disabled',true)
        }else{
            // $('#btn_submit_02').attr('disabled',false)
            $.post('/mygis/addcommunity',{'province':province,'city':city,'district':district,'eX':eX,'eY':eY,'community_phone':phone,'community_name':name},function(){
                alert('成功')
            });
        }
      });

      $('#btn_submit_03').click(function(){ // 添加小区
        var province = $('#province2').val();
        var city = $('#city2').val();
        var district = $('#district2').val();
        var eX = $('#eX').val();
        var eY = $('#eY').val();
        var phone = $('#phone').val();
        var name = $('#name').val();
        if(eX==''||name==''||phone==''){
            alert('请完善信息')
            // $('#btn_submit_03').attr('disabled',true)
        }else{
            // $('#btn_submit_03').attr('disabled',false)
             $.post('/mygis/addrest',{'province':province,'city':city,'district':district,'eX':eX,'eY':eY,'rest_phone':phone,'rest_name':name},function(){
         alert('成功')
       });
        }
      
      });
    });
    
      