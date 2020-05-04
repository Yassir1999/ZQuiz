        var number_of_questions_id = document.getElementById("number-of-questions");
        var number_of_questions = parseInt(number_of_questions_id.innerHTML);
        var isTest = document.getElementById("isTest").innerHTML;
        var results = {};
        var answers = {};
        function select(i,qw,j,w){
        saveResult(i,parseInt(qw),parseInt(w));
        saveAnswer(i,j);
        let b = "button-" + i + "-" + j;
        if(document.getElementById(b).style.filter == "brightness(1)" && document.getElementById(b).style.borderColor == "white"){
        document.getElementById(b).style.filter = "brightness(0.5)";
        document.getElementById(b).style.borderColor = "black";
        } else {
        let r = document.getElementsByClassName(i);
        for(var k=0; k < r.length ;k++) {
        r[k].style.filter = "brightness(0.5)";
        r[k].style.borderColor = "black";
        }
        document.getElementById(b).style.filter = "brightness(1)";
        document.getElementById(b).style.borderColor = "white";
        }
        }
        function saveAnswer(questionId, answerId) {
        answers[ questionId ] = answerId;
        }
        function saveResult(questionId, questionWorth, answerWorth) {
        results[ questionId ] = [ questionWorth, answerWorth ];
        }
        function getFinalResult_notTest() {
        let finalResults = {"1" : 0 , "2" : 0 , "3" : 0 , "4" : 0 , "5" : 0 , "6" : 0 , "7" : 0 , "8" : 0 , "9" : 0};
        for(var i=1;i<=9;i++){
        for(var qst in results) {
        if(i == parseInt(results[qst][1])){
        finalResults[i.toString()] = parseInt(finalResults[i]) + parseInt(results[qst][0]);
        }
        }
        }
        let finalResult = 0;
        let finalAnswer = 1;
        for(var v in finalResults) {
        if(finalResults[v.toString()] > finalResult){
        finalResult = finalResults[v];
        finalAnswer = parseInt(v);
        }
        }
        return finalAnswer;
        }
        function getFinalResult_Test() {
        if(Object.keys(results).length == 0){return 0;}
        let base = 0;
        let top = 0;
        for( var qst in results){
        base = base + parseInt(results[qst][0]);
        top = top + parseInt(results[qst][1]);
        }
        return Number(top) / Number(base);
        }
        function getResults() {
        document.getElementById("result").style.visibility = "visible";
        document.getElementById("submit-button").style.visibility = "hidden";
        if(isTest == 1){
        fr = getFinalResult_Test() * 100;
        if(fr > 10){
        document.getElementById("bm1").style.display = "none";
        }
        if(fr <= 10 || fr > 25){
        document.getElementById("bm2").style.display = "none";
        }
        if(fr <= 25 || fr > 40){
        document.getElementById("bm3").style.display = "none";
        }
        if(fr <= 40 || fr > 75){
        document.getElementById("bm4").style.display = "none";
        }
        if(fr <= 75 || fr > 95){
        document.getElementById("bm5").style.display = "none";
        }
        if(fr <= 95 || fr > 100){
        document.getElementById("bm6").style.display = "none";
        }
        document.getElementById("result-answer").innerHTML = fr.toFixed(2) + "%";
        var buttons = document.getElementsByTagName("button");
        var i = 1;
        while(buttons[i+2] != null){
        buttons[i].style.cursor = 'default';
        buttons[i].disabled = "disabled";
        buttons[i].style.filter = "brightness(0.75)";
        buttons[i].classList.add("opacity");
        i++;
        }
        var imgsrc;
        if(fr <= 10){imgsrc = document.getElementById("bm1").src;}
        else if(fr > 10 && fr <= 25){imgsrc = document.getElementById("bm2").src;}
        else if(fr > 25 && fr <= 40){imgsrc = document.getElementById("bm3").src;}
        else if(fr > 40 && fr <= 75){imgsrc = document.getElementById("bm4").src;}
        else if(fr > 75 && fr <= 95){imgsrc = document.getElementById("bm5").src;}
        else {imgsrc = document.getElementById("bm6").src;}
        var meta_img = document.createElement('meta');
        meta_img.setAttribute('property', 'og:image');
        meta_img.setAttribute('content', imgsrc);
        document.getElementsByTagName('head')[0].appendChild(meta_img);
        var meta_desc = document.createElement('meta');
        meta_desc.setAttribute('property', 'og:description');
        meta_desc.setAttribute('content', document.getElementsByClassName("main-question-a")[0].innerHTML);
        document.getElementsByTagName('head')[0].appendChild(meta_desc);
        var meta_type = document.createElement('meta');
        meta_type.setAttribute('property', 'og:type');
        meta_type.setAttribute('content', 'website');
        document.getElementsByTagName('head')[0].appendChild(meta_type);
        var meta_title = document.createElement('meta');
        meta_title.setAttribute('property', 'og:title');
        meta_title.setAttribute('content', fr.toString());
        document.getElementsByTagName('head')[0].appendChild(meta_title);
        } else if (isTest == 0) {
        var fs = getFinalResult_notTest();
        for(var i=1;i<=9;i++){
        if(i != fs && document.getElementById("img"+i) != null){
        document.getElementById("img"+i).style.display = "none";
        }
        }
        document.getElementById("result-answer").innerHTML = document.getElementById("result"+fs).innerHTML;
        var meta_img = document.createElement('meta');
        meta_img.setAttribute('property', 'og:image');
        meta_img.setAttribute('content', document.getElementById("img"+fs).src);
        document.getElementsByTagName('head')[0].appendChild(meta_img);
        var meta_desc = document.createElement('meta');
        meta_desc.setAttribute('property', 'og:description');
        meta_desc.setAttribute('content', document.getElementsByClassName("main-question-a")[0].innerHTML);
        document.getElementsByTagName('head')[0].appendChild(meta_desc);
        var meta_type = document.createElement('meta');
        meta_type.setAttribute('property', 'og:type');
        meta_type.setAttribute('content', 'website');
        document.getElementsByTagName('head')[0].appendChild(meta_type);
        var meta_title = document.createElement('meta');
        meta_title.setAttribute('property', 'og:title');
        meta_title.setAttribute('content', document.getElementsByClassName("categorie-text")[0].innerHTML);
        document.getElementsByTagName('head')[0].appendChild(meta_title);
        } else {
        alert("Something went wrong !!!");
        }
        }

        function revealanswers(){
        var allbuttons = document.getElementsByTagName("button");
        var i = 1;
        while(allbuttons[i+1] != null){
        allbuttons[i].style.borderWidth = "thick";
        allbuttons[i].style.filter = "brightness(0.9)";
        i++;
        }
        var b;
        for(var qst in answers){
        b = "button-" + qst.toString() + "-" + answers[qst].toString();
        if(results[qst][1] == 0){
        document.getElementById(b).style.borderColor = "red";
        } else if(results[qst][1] == results[qst][0]){
        document.getElementById(b).style.borderColor = "green";
        } else {
        document.getElementById(b).style.borderColor = "yellow";
        }
        }
        document.getElementById("revealanswers").style.display = "none";
        }

        function sharetofacebook() {
        let a= document.createElement('a');
        a.target= '_blank';
        a.href= "https://www.facebook.com/sharer/sharer.php?u=" + document.URL;
        a.click();
        }