  
  $(document).ready(function(){
    var star1 = 0;
    var star2 = 0;
    var star3 = 0;
    var star4 = 0;
    var star5 = 0;
    $('#result1').hide()
    $('#market_id').hide()
    $('#market_name').hide()
    $('#page').hide()
    // 菜品新鲜程度
    $('#star1').raty({ 
        path:"/static/dafen/lib/img/",             //图片地址
        hints:["差","一般",'良好','满意','优秀'],   // 评分等价文本
        score: 4,   // 默认评分
        number:5,   // 评分
        size:100,
        click:function(score,evt){
            // alert(score+$('#result1').val())
            star1 = score
        },
        target:"#result1",   // 存放用户评分
        targetKeep:true     
    });
    // 乱认杂物
    $('#result2').hide()
    $('#star2').raty({ 
        path:"/static/dafen/lib/img/",             //图片地址
        hints:["差","一般",'良好','满意','优秀'],   // 评分等价文本
        score: 4,   // 默认评分
        number:5,   // 评分
        size:100,
        click:function(score,evt){
            // alert(score+$('#result2').text())
            star2 = score
        },
        target:"#result2",   // 存放用户评分
        targetKeep:true     
    });
    // 摊位整洁
    $('#result3').hide()
    $('#star3').raty({ 
        path:"/static/dafen/lib/img/",             //图片地址
        hints:["差","一般",'良好','满意','优秀'],   // 评分等价文本
        score: 4,   // 默认评分
        number:5,   // 评分
        size:100,
        click:function(score,evt){
            // alert(score+$('#result3').text())
            star3 = score
        },
        target:"#result3",   // 存放用户评分
        targetKeep:true     
    });
    // 从业人员工作衣帽洁净
    $('#result4').hide()
    $('#star4').raty({ 
        path:"/static/dafen/lib/img/",             //图片地址
        hints:["差","一般",'良好','满意','优秀'],   // 评分等价文本
        score: 4,   // 默认评分
        number:5,   // 评分
        size:100,
        click:function(score,evt){
            // alert(score+$('#result4').text())
            star4 = score
        },
        target:"#result4",   // 存放用户评分
        targetKeep:true     
    });
    // 厕所卫生
    $('#result5').hide()
    $('#star5').raty({ 
        path:"/static/dafen/lib/img/",             //图片地址
        hints:["差","一般",'良好','满意','优秀'],   // 评分等价文本
        score: 4,   // 默认评分
        number:5,   // 评分
        size:100,
        click:function(score,evt){
            // alert(score+$('#result5').text())
            star5 = score
        },
        target:"#result5",   // 存放用户评分
        targetKeep:true     
    });

    $('#btn_star').click(function(){
        start1 = star1+'_'+$('#result1').text() //菜品新鲜程度
        start2 = star2+'_'+$('#result2').text() //乱认杂物
        start3 = star3+'_'+$('#result3').text() //摊位整洁
        start4 = star4+'_'+$('#result4').text() //从业人员工作衣帽洁净
        start5 = star5+'_'+$('#result5').text() // 厕所卫生
        market_id = $('#market_id').text()
        page = $('#page').text()
        market_name = $('market_name').text()
        $.post('/mygis/marketdetailasses/?page='+page+'&market_name'+market_name,{'start1':start1,'start2':start2,'start3':start3,'start4':start4,'start5':start5,'market_id':market_id},function(){          
            alert('success')
        })
    })
  })