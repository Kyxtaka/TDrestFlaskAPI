$(function() {

    $("#button").click(refreshQuestionnaireList);

    function remplirQuestionnaires(repjson) {
        console.log(JSON.stringify(repjson));
        $('#questionnaires').empty();
        $('#listquestions').empty();
        $('#currentquestion').empty();
        $('#listanswers').empty();
        $('#questionnaires').append($('<ul>'));
        for(question of repjson.questionnaires){
            console.log(question);
            $('#questionnaires ul')
                .append($('<li>')
                .append($('<a>')
                .text(question.name))
                .on("click", question, details)
            );
        }
    }

    function remplirQuestions(repjson) {
        console.log(JSON.stringify(repjson));
        $('#listquestions').empty();
        $('#listquestions').append($('<ul>'));
        for(question of repjson.questions){
            console.log(question);
            $('#listquestions ul')
                .append($('<li>')
                .append($('<a>')
                .text(question.title))
                .on("click", question, detailsQuestion)
            );
        }
    }

    function onerror(err) {
        $("#questionnaires").html("<b>Impossible de récupérer les questionnaires à réaliser !</b>"+err);
    }

    function onerrorQuestion(err) {
        $("#listquestions").html("<b>Impossible de récupérer les questions à réaliser !</b>"+err);
    }

    function refreshQuestionnaireList(){
        $("#currentquestionnaire").empty();
        requete = "http://127.0.0.1:5000/todo/api/v1.0/quiz";
        fetch(requete)
        .then( response => {
                  if (response.ok) return response.json();
                  else throw new Error('Problème ajax: '+response.status);
                }
            )
        .then(remplirQuestionnaires)
        .catch(onerror);
      }

    function refreshQuestionList(){
        $("#currentquestion").empty();
        id = $("#currentquestionnaire #turi").val().split("/").pop();
        console.log(id);
        requete = "http://127.0.0.1:5000/todo/api/v1.0/question/byquiz/"+id;
        fetch(requete)
        .then( response => {
                  if (response.ok) return response.json();
                  else throw new Error('Problème ajax: '+response.status);
                }
            )
        .then(remplirQuestions)
        .catch(onerrorQuestion);
    }


    function details(event){
        $("#currentquestionnaire").empty();
        $("#questionnairetools").empty();
        $("#listquestions").empty();
        $("#currentquestion").empty();
        $("#listanswers").empty();
        formQuestionnaire();
        fillformQuestionnaire(event.data);
    }

    
    function detailsQuestion(event){
        // $("#listquestion").empty();
        $("#currentquestion").empty();
        $("#listanswers").empty();
        formQuestion();
        fillformQuestion(event.data);
        completeFormQuestion(event.data.questionType, event.data); 
    }

    class Questionnaire{
        constructor(name, uri) {
            this.name = name;
            this.uri = uri;
            console.log(this.uri);   
        }
    }

    class Question{
        constructor(title, questionType, questionnaire_id, uri) {
            this.title = title;
            this.questionType = questionType;
            this.questionnaire_id = questionnaire_id;
            this.uri = uri;
            console.log("question uri: ",this.uri);   
        }
    }

    class QuestionChoixMultiple extends Question{
        constructor(title, questionType, questionnaire_id, uri, choix1, choix2, choix3, choix4, reponse) {
            super(title, questionType, questionnaire_id, uri);
            this.choix1 = choix1;
            this.choix2 = choix2;
            this.choix3 = choix3;
            this.choix4 = choix4;
            this.reponse = reponse;
            console.log("questionChoixMultiple uri: ",this.uri);   
            console.log("questionChoixMultiple: ",this); 
        }
    }

    class QuestionOpen extends Question{
        constructor(title, questionType, questionnaire_id, uri, reponse) {
            super(title, questionType, questionnaire_id, uri);
            this.reponse = reponse;
            console.log("questionOpen uri: ",this.uri); 
            console.log("questionOpen: ",this);  
        }
    }


    $(".tools #add").on("click", formQuestionnaire);
    $('.tools #del').on('click', delQuestionnaire);
 

    // ========================================================================Questionnaire========================================================================

    function formQuestionnaire(isnew){
        $("#currentquestionnaire").empty();
        $("#questionnairetools").empty();
        $("#listquestions").empty();
        $("#currentquestion").empty();
        $("#listanswers").empty();
        $("#currentquestionnaire")
            .append($('<span>Name <input type="text" id="name"><br></span>'))
            .append($('<span><input type="hidden" id="turi"><br></span>'))
            .append(
                isnew
                    ?$('<span><input type="button" value="Save Questionnaire"><br></span>').on("click", saveNewQuestionnaire)
                    :$('<span><input type="button" value="Recuperer questions"><br></span>').on("click", refreshQuestionList),
                    $('<span><input type="button" value="Modify questionnaire"><br></span>').on("click", saveModifiedQuestionnaire)
                    
            );
        $('#questionnairetools')
            .append($('<img id="addQuestion" src="img/new.png" alt="Nouvelle question"/>').on("click", formQuestion));
        }

    function fillformQuestionnaire(t){
        $("#currentquestionnaire #name").val(t.name);
        t.uri=(t.uri == undefined)?"http://127.0.0.1:5000/todo/api/v1.0/quiz/"+t.id:t.uri;
        $("#currentquestionnaire #turi").val(t.uri);
    }

    function saveNewQuestionnaire(){
        var questionnaire = new Questionnaire($("#currentquestionnaire #name").val());
        console.log(JSON.stringify(questionnaire));
        fetch("http://127.0.0.1:5000/todo/api/v1.0/quiz", {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(questionnaire)
        })
        .then(res => { 
            console.log('Save Success') ;
            $("#result").text(res['contenu']);
            refreshQuestionnaireList();
        })
        .catch( res => { console.log(res) });
    }

    function saveModifiedQuestionnaire(){
        var questionnaire = new Questionnaire(
            $("#currentquestionnaire #name").val(),
            $("#currentquestionnaire #turi").val()
        );
        console.log("PUT");
        console.log(questionnaire.uri);
        console.log(JSON.stringify(questionnaire));
        fetch(questionnaire.uri,{
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "PUT",
            body: JSON.stringify(questionnaire)
        })
        .then(res => { console.log('Update Success');  refreshQuestionnaireList();} )
        .catch( res => { console.log(res) });
    }

    function delQuestionnaire(){
        if ($("#currentquestionnaire #turi").val()){
            url = $("#currentquestionnaire #turi").val();
            fetch(url,{
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            })
            .then(res => { console.log('Delete Success:' + res); } )
            .then(refreshQuestionnaireList)
            .catch( res => { console.log(res);  });
        }
    }

    // ========================================================================Question========================================================================

    function formQuestion(isnew){
        var currentQuestionSecion = $("#currentquestion");
        questionnaire_id = $("#currentquestionnaire #turi").val().split("/").pop();
        console.log(questionnaire_id);
        currentQuestionSecion.empty();
        currentQuestionSecion
            .append($('<span>Title <input type="text" id="title"><br></span>'))
        

            .append($('<span> QuestionType : </span>')
                .append($('<input type="radio" class="questionTypeRadio" id="questionTypeOpen" name="questionType" value="open" disabled=false>Open</input>'))
                .append($('<input type="radio" class="questionTypeRadio" id="questionTypeMultiple" name="questionType" value="multiple">Multiple</input><br>'))
            )

            .append($('<span>Questionnaire_id <input type="text" id="questionnaire_id" value='+questionnaire_id+' disabled><br></span>'))
            .append($('<span><input type="hidden" id="turi"><br></span>'))
            .append($('<h3>Reponses</h3><div id="listanswers"></div>'))
            .append(
                isnew?
                $('<span><input type="button" value="Save Question"><br></span>').on("click", saveNewQuestion)
                :$('<span><input type="button" value="Modify Question"><br></span>').on("click", saveModifiedQuestion)
            );

        if (isnew) {
            $("#currentquestion #questionTypeOpen").prop('checked', true);
            Array.prototype.forEach.call($('.questionTypeRadio'), (radio) => {
                radio.disabled = false;
            });
            var radioValue = $('input[name="questionType"]:checked').val();
            console.log("radio value1",radioValue);
            completeFormQuestion(radioValue);
        }
        else {
            Array.prototype.forEach.call($('.questionTypeRadio'), (radio) => {
                radio.disabled = true;
            });
            console.log($('.questionTypeRadio'))
            console.log("radio value2",radioValue);
            // completeFormQuestion(radioValue);
        }
        $(".questionTypeRadio").on("change", function() { completeFormQuestion($(this).val());});
    }

    function completeFormQuestion(type, data) {
        var radioValue = $('input.questionTypeRadio[name="questionType"]:checked').val();
        console.log("radio value inside func",radioValue);
        var formQuestionAnswerSection = $("#currentquestion #listanswers");
        formQuestionAnswerSection.empty();
        var responseElement = $('<span>Reponse </span>').append($('<input type="text" id="reponse">')); 
        if (type === "open") {
            console.log("open");
            formQuestionAnswerSection.append(responseElement);
        } else if (type === "multiple") {
            console.log('multiple');
            for (var i = 1; i < 5; i++) {
                formQuestionAnswerSection.append(
                        $('<span>Choix '+i+'</span>')
                        .append($('<input type="text" id="choix'+i+'">'))
                        .append($('<br>')
                    )
                );
                formQuestionAnswerSection.append(responseElement);
            }
        }else {
            $("#currentquestion").append($('<span>Question type not defined</span>'));
        }
        if (data != undefined) {
            responseElement.find('input').val(data.reponse);
            if (type === "multiple") {
                for (var i = 1; i < 5; i++) {
                    formQuestionAnswerSection.find('#choix'+i).val(data['choix'+i]);
                }
            }
        }
    }

    function fillformQuestion(t){
        $("#currentquestion #title").val(t.title);
        var input = $('input[name="questionType"][value="'+t.questionType+'"]');
        console.log("fillformQuestion inputRadio:", input);
        $('input[name="questionType"][value="'+t.questionType+'"]').prop('checked', true);
        $("#currentquestion #questionnaire_id").val(t.questionnaire_id);
        t.uri=(t.uri == undefined)?"http://127.0.0.1:5000/todo/api/v1.0/question/"+t.id:t.uri;
        $("#currentquestion #turi").val(t.uri);
    }

    function saveNewQuestion(){
        var radioHtmlElementChecked = $('input[name="questionType"]:checked');
        console.log(radioHtmlElementChecked); 
        if (radioHtmlElementChecked.val() == "open") {
            var question = new QuestionOpen(
                $('#currentquestion #title').val(),
                radioHtmlElementChecked.val(),
                $('#currentquestion #questionnaire_id').val(),
                null,
                $('#currentquestion #reponse').val()
            );
        }else if (radioHtmlElementChecked.val() == "multiple") {
            var question = new QuestionChoixMultiple(
                $("#currentquestion #title").val(),
                radioHtmlElementChecked.val(),
                $("#currentquestion #questionnaire_id").val(),
                null,
                $("#currentquestion #choix1").val(),
                $("#currentquestion #choix2").val(),
                $("#currentquestion #choix3").val(),
                $("#currentquestion #choix4").val(),
                $("#currentquestion #reponse").val()
            );
        }else {
            console.log("Question type not defined");
            return;
        }
        console.log(JSON.stringify(question));
        fetch("http://127.0.0.1:5000/todo/api/v1.0/question", {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(question)
        })
        .then(res => { 
            console.log('Save Success') ;
            $("#result").text(res['contenu']);
            refreshQuestionList();
        })
        .catch( res => { console.log(res) });
    }

    function saveModifiedQuestion(){
        var radioHtmlElementChecked = $('input[name="questionType"]:checked');
        console.log("Modifying quesiton readioChecked",radioHtmlElementChecked); 
        if (radioHtmlElementChecked.val() == "open") {
            var question = new QuestionOpen(
                $('#currentquestion #title').val(),
                radioHtmlElementChecked.val(),
                $('#currentquestion #questionnaire_id').val(),
                $('#currentquestion #turi').val(),
                $('#currentquestion #reponse').val()
            );
        }else if (radioHtmlElementChecked.val() == "multiple") {
            var question = new QuestionChoixMultiple(
                $("#currentquestion #title").val(),
                radioHtmlElementChecked.val(),
                $("#currentquestion #questionnaire_id").val(),
                $('#currentquestion #turi').val(),
                $("#currentquestion #choix1").val(),
                $("#currentquestion #choix2").val(),
                $("#currentquestion #choix3").val(),
                $("#currentquestion #choix4").val(),
                $("#currentquestion #reponse").val()
            );
        }else {
            console.log("Question type not defined");
            return;
        }
        console.log("PUT");
        console.log(question.uri);
        console.log(JSON.stringify(question));
        fetch(question.uri,{
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "PUT",
            body: JSON.stringify(question)
        })
        .then(res => { console.log('Update Success');  refreshQuestionList();} )
        .catch( res => { console.log(res) });
    }

    function delQuestion(){
        if ($("#currentquestion #turi").val()){
            url = $("#currentquestion #turi").val();
            fetch(url,{
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            })
            .then(res => { console.log('Delete Success:' + res); } )
            .then(refreshQuestionList)
            .catch( res => { console.log(res);  });
        }
    }

    
    $('.tools #addQuestion').on('click', formQuestion);
    $('.tools #delQuestion').on('click', delQuestion);
});
