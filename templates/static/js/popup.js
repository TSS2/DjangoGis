// var text = new ol.Overlay({
      //   position:address,
      //   element:document.getElementById('popup')
      // });

      // map.addOverlay(text);
      // text.getElement().innerText = market.getElement().title;

       // popup标注
      // var popup = new ol.Overlay({
      //   element: document.getElementById('popup')
      // });
      // popup.setPosition(address);
      // map.addOverlay(popup);
      // var overlay = new ol.Overlay({
			// 	element: document.getElementById('popup')
			// });

      // ************* //
      // 1 获取标注点详细信息
      // 2 添加popup标注
      // ************* //
      //标注点信息
      // var featureInfo = {
      //       geo = add_name,
      //       att:{
      //           title:"成都 你好！",      //标注信息的标题内容
      //           titleURL:"#",            //标注信息的链接
      //           text:"成都市双流县常乐小区菜市场",//标注内容简介
      //           imgURL:"#",//标注的图片
      //       }
      // }

      // 添加popup标注

      // 创建样式
    //   var createLabelStyle  = function(feature){
    //     // 返回样式
    //     return new ol.style.Style({
    //       // 点的样式
    //       image: new ol.style.Icon({
    //           // 标注文本域图片之间的距离
    //           anchor:[0.5,60],
    //           // 标注样式起点位置
    //           anchorOrigin:'top-right',
    //           // X方向单位
    //           anchorXUnits:'fraction',
    //           // Y方向单位
    //           anchorYUnits:'pixels',
    //           // 偏移起点位置的方向
    //           offsetOrigin: 'top-right',
    //           // 透明度
    //           opacity:0.75,
    //           // 图标的url
    //           src:'#',
    //       }),
    //       // 文本样式
    //       text: new ol.style.Text({
    //           //对其方式  
    //           textAlign: 'center',  
    //           //基准线  
    //           textBaseline: 'middle',  
    //           //文字样式  
    //           font: 'normal 14px 微软雅黑',  
    //           //文本内容  
    //           text: feature.get('name'),  
    //           //文本填充样式  
    //           fill: new ol.style.Fill({ color: '#aa3300' }),  
    //           //笔触  
    //           stroke: new ol.style.Stroke({ color: '#ffcc33', width: 2 })  
    //       })

    //     })
    //   }
    //   //实例化Vector要素，通过矢量图层添加到地图容器中  
    //   var iconFeature = new ol.Feature({  
    //     //几何样式  
    //     geometry: new ol.geom.Point(address),  
    //     //名称属性  
    //     name: add_name,  
    //     //人口属性  
    //     population: 2115   
    // }); 

    // //设置样式  
    // iconFeature.setStyle(createLabelStyle(iconFeature));  
    // //矢量标注的数据源  
    // var vectorSource = new ol.source.Vector({  
    //   features: [iconFeature]  
    // });
    // //矢量标注图层  
    // var vectorLayer = new ol.layer.Vector({  
    //   source: vectorSource  
    // });
    // //将矢量标注图层添加到map中  
    // map.addLayer(vectorLayer);

    // // 在地图中创建一个Overlay 初始化一个覆盖层
    // var popup = new ol.Overlay(({
    //   // 元素内容
    //   element:$('#popup'),
    //   autoPan:true,
    //   // 位置曾如何与位置坐标匹配
    //   positioning:'bottom-center',
    //   // 事件传播到地图视点的时候是否应该停止
    //   stopEvent:false,
    //   autoPanAnimation:{
    //     // 动画持续时间
    //     duration:250
    //   }
    // }));
    // // 将覆盖层添加到map中
    // map.addOverlay(popup);

    // //为要素添加信息的函数  
    // function addFeatureInfo(info) {  
    //   //创建一个a标签元素  
    //   var elementA = document.createElement('a');  
    //   //设置a标签的样式类  
    //   elementA.className = 'markerInfo';  
    //   //设置a标签的超链接地址  
    //   elementA.href = info.att.titleURL;  
    //   //设置a标签的文本内容  
    //   setInnerText(elementA, info.att.title);  
    //   //将a标签元素添加到内容div标签中  
    //   content.appendChild(elementA);  

    //   //创建一个div标签元素  
    //   var elementDiv = document.createElement('div');  
    //   //设置div标签的内容  
    //   setInnerText(elementDiv, info.att.text);  
    //   //将div标签加入到内容div标签中  
    //   content.appendChild(elementDiv);  

    //   //创建一个图像标签  
    //   var elementImg = document.createElement('img');  
    //   //指定图像标签的URL  
    //   elementImg.src = info.att.imgURL;  
    //   //将img标签加入到内容div标签中  
    //   content.appendChild(elementImg);  
    //  };
     
    //  //设置文本函数  
    //  function setInnerText(element,text) {  
    //   if (typeof element.textContent == 'string') {  
    //       element.textContent = text;  
    //   } else {  
    //       element.innerText = text;  
    //   }  
    //  } 
