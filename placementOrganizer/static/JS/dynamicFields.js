/*function checkBacklogHistory(form) {
    //var ele = document.getElementsById('BacklogHistory');
    if (form.BacklogHistory[1].checked == true && form.BacklogHistory[0].checked == false) {
        document.getElementById("backlogDetails").innerHTML = `<h2>Backlog Details</h2><br><br>
                <b>Yes if you have/ had backlog</b>
                1<sup>st</sup> Semester<br>
                <input type="radio" name "1semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "1semBacklogHistory" value="yes">Yes<br><br>
                1<sup>st</sup> Semester Completed?<br>
                <input type="radio" name "1semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "1semStatus" value="stillBacklog">Still Backlog<br><br>
                2<sup>nd</sup> Semester<br>
                <input type="radio" name "2semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "2semBacklogHistory" value="yes">Yes<br><br>
                2<sup>nd</sup> Semester Completed?<br>
                <input type="radio" name "2semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "2semStatus" value="stillBacklog">Still Backlog<br><br>
                3<sup>rd</sup> Semester<br>
                <input type="radio" name "3semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "3semBacklogHistory" value="yes">Yes<br><br>
                3<sup>rd</sup> Semester Completed?<br>
                <input type="radio" name "3semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "3semStatus" value="stillBacklog">Still Backlog<br><br>
                4<sup>th</sup> Semester<br>
                <input type="radio" name "4semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "4semBacklogHistory" value="yes">Yes<br><br>
                4<sup>th</sup> Semester Completed?<br>
                <input type="radio" name "4semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "4semStatus" value="stillBacklog">Still Backlog<br><br>
                5<sup>th</sup> Semester<br>
                <input type="radio" name "5semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "5semBacklogHistory" value="yes">Yes<br><br>
                5<sup>th</sup> Semester Completed?<br>
                <input type="radio" name "5semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "5semStatus" value="stillBacklog">Still Backlog<br><br>
                6<sup>th</sup> Semester<br>
                <input type="radio" name "6semBacklogHistory" value="no" checked required>No<br>
                <input type="radio" name "6semBacklogHistory" value="yes">Yes<br><br>
                6<sup>th</sup> Semester Completed?<br>
                <input type="radio" name "6semStatus" value="completed" checked required>Completed<br>
                <input type="radio" name "6semStatus" value="stillBacklog">Still Backlog<br><br>
                7<sup>th</sup> Semester<br>
                <input type="radio" name "7semBacklogHistory" value="no">No<br>
                <input type="radio" name "7semBacklogHistory" value="yes">Yes<br><br>
                7<sup>th</sup> Semester Completed?<br>
                <input type="radio" name "7semStatus" value="completed">Completed<br>
                <input type="radio" name "7semStatus" value="stillBacklog">Still Backlog<br><br>
                8<sup>th</sup> Semester<br>
                <input type="radio" name "8semBacklogHistory" value="no">No<br>
                <input type="radio" name "8semBacklogHistory" value="yes">Yes<br><br>
                8<sup>th</sup> Semester Completed?<br>
                <input type="radio" name "8semStatus" value="completed">Completed<br>
                <input type="radio" name "8semStatus" value="stillBacklog">Still Backlog<br><br>
                <h3>Present No. of Backlogs</h3><br>
                <input type="number" min="0" max="15" name="presentBacklogs"><br><br>`;
    }
    else {
        document.getElementById("backlogDetails").innerHTML = '';
    }
}*/

var counter = 1;
var limit = 10;
function addCertificate(divName) {
    if (counter == limit) {
        alert("You have reached the limit of adding " + counter + " inputs");
    }
    else {
        document.getElementsByName("hidden").value = counter + 1;
        var newdiv = document.createElement('div');
        certificate = 'Certificate' + (counter + 1)
        let name = "name = " + certificate
        newdiv.innerHTML = "Certificate " + (counter + 1) + " <br><input type='file' " + name + "accept='.pdf'>";
        document.getElementById(divName).appendChild(newdiv);
        counter++;

    }
}

