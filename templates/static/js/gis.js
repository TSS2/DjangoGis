$(document).ready(function(){

//起始位置
// var center = [11575931.700277366,3578569.073827034];

//标记数据集
var source = new ol.source.Vector();

//获取样式
var styleFunction = function(feature,colors) {
    var geometry = feature.getGeometry();
    //线段样式
    var styles = [
    new ol.style.Style({
        fill: new ol.style.Fill({     //矢量图层填充颜色，以及透明度
            color: '#0044CC'
        }), 
        stroke: new ol.style.Stroke({  //边界样式
            lineDash:[1],
            width: 1,  
            color: colors  
        })  
    })
    ];
    //箭头样式
    geometry.forEachSegment(function(start, end) {
        var arrowLonLat = [(end[0]+start[0])/2,(end[1]+start[1])/2];
        var dx = end[0]- start[0]; 
        var dy = end[1] - start[1];
        var rotation = Math.atan2(dy, dx);
        styles.push(new ol.style.Style({
            geometry: new ol.geom.Point(arrowLonLat),
            image: new ol.style.Icon({
                src: 'https://openlayers.org/en/v4.6.5/examples/data/arrow.png',
                anchor: [0.75, 0.5],
                rotateWithView: true,
                rotation: -rotation
            })
        }));
    });
    return styles;
};

//标记层
var layers = new ol.layer.Vector({
    source: new ol.source.Vector()
});

function line(coordinate1,coordinate2,colors){
  var coordinate = new Array();
  coordinate.push(coordinate1);
  coordinate.push(coordinate2);
  var geometry = new ol.geom.LineString();
  for (var i = 0; i < coordinate.length; i++) {
      geometry.appendCoordinate(coordinate[i]);
      // 创建一个Feature，并设置好在地图上的位置
      var anchor = new ol.Feature({
          geometry: new ol.geom.Point(coordinate[i])
      });  
      // 设置样式，在样式中就可以设置图标
      anchor.setStyle(new ol.style.Style({
          image: new ol.style.Circle({  
              radius: 10,  
              stroke: new ol.style.Stroke({  
                  color: '#fff'  
              }),  
              fill: new ol.style.Fill({  
                  color: '#3399CC'  
              })  
          })
      }));
      // 添加到之前的创建的layer中去
      layers.getSource().addFeature(anchor);
}

  var feature = new ol.Feature({  
    geometry:geometry
  });
  source.addFeature(feature);

  //标记点集
  var vector = new ol.layer.Vector({
    source: source,
    style: styleFunction(feature,colors)
  });
  map.addOverlay(vector);
}


// var feature = new ol.Feature({  
//     geometry:geometry
// });
// source.addFeature(feature);

// //标记点集
// var vector = new ol.layer.Vector({
//     source: source,
//     style: styleFunction
// });

//地图层
// var raster = new ol.layer.Tile({
//     source: new ol.source.OSM()
// });
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
      // new ol.control.FullScreen(),   // 地图全屏控件
      new ol.control.MousePosition()   // 鼠标位置控件
    ]),
  });
  

  // 鼠标交互画直线
  // map.addInteraction(new ol.interaction.Draw({
  //   source: source,
  //   type: 'LineString'
  // }));

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
   var market_phone = $('#market_phone').val();
   var market_name = $('#market_name').val();
  $.post('/mygis/addmessage',{'province':province,'city':city,'district':district,'eX':eX,'eY':eY,'market_phone':market_phone,'market_name':market_name},function(){
    alert('成功')
  });
 });

 $('#district2').bind("change",function(){
  var province = $('#province2').val();
  var city = $('#city2').val();
  var district = $('#district2').val();

  // 搜索地址 显示该区域菜市场popup标注

  $.post('/mygis/querymessage',{'province':province,'city':city,'district':district},function(data){

    var x =0;
    var y = 0;
    var id_array = new Array();   // 存储创建的div id
    var i = 0;

    $.each(data,function(index,value){
      var add_name = index;
      var x = value[0];
      var y = value[1];
      var address = [x,y];
      var id = 'popup'+x.replace('.','')
      id_array.push(id);

      if (i==0)
      {
        if (address)
        {
          // alert(add_name)
          map_center_tran = ol.proj.transform(address, 'EPSG:3857' ,'EPSG:4326');   // 设置第一个查询点为地图中心点
          map_center = address;
          center_name = add_name;
        }
      }
      center =  ol.proj.transform(address, 'EPSG:3857' ,'EPSG:4326');
      i++;
      // 4326坐标系中计算两点之间的距离
      var wgs84Sphere = new ol.Sphere(6378137); 
      var distance = wgs84Sphere.haversineDistance(map_center_tran,center);
      
      // 创建新的div
      if (parseInt(distance) <= 500)
      {
        $("#popup").after("<div id = "+id+" class = 'ol-popup'></div>");
        line(map_center,address,'red')
      }
      if (parseInt(distance) > 500)
      {
        $("#popup").after("<div id = "+id+" class = 'ol-popup-01'></div>");
        line(map_center,address,'yellow')
      }
      // $("#popup").after("<div id = "+id+" class = 'ol-popup'></div>");
      
      // 画线
      
      // line(map_center,address)
      // 新建图层
      var market = new ol.Overlay({
        id:x,
        position:address,
        positioning:'center-center',
        element: document.getElementById(id),     // 将动态生成的div添加到图层
        stopEvent:false
      });
      map.addOverlay(market);
      // 添加路线图层
      // map.addOverlay(vector);
      // market.getElement().title = [add_name,address];
      // var market_id = market.getElement().id
      $("#"+id).attr("title",add_name);
      $("#"+id).bind({
        
        mouseenter:function(){      // 鼠标移动到点上时显示信息
          id_n = id + '1'
          $('#'+id).append("<div id = "+id_n+" class = 'popup-content list-group'><ul class='list-group'><li id='li_name' class='list-group-item'><span class='label label-default'>Default</span>插入项</li><li id='li_address' class='list-group-item'>插入项</li><li id='li_address' class='list-group-item'>插入项</li></ul></div>");
          // $('#'+id_n).text(add_name);
          $('#li_name').text(add_name);
          $('#li_address').text(x+"---"+y);
        },
        mouseleave:function(){      // 鼠标移走时删除div
          id_n = id + '1'
          $("#"+id_n).remove()
        },
      });

      // layer弹出层
      $('#'+id).on('click', function(){
        layer.open({
          type: 2,    // iframe窗口
          title: '菜市场信息',
          area: ['600px', '360px'],
          shadeClose: true, //点击遮罩关闭
          content: "/mygis/marketmessage/?name="+add_name+"&distance="+distance
        });
      });
    });
    console.log(id_array)
  });
  });
  
});

  