function panelek(db){
    const panelek=document.getElementById('panelek');
    const tetofelulet = document.getElementById('tetofelulet');
    panelek.innerHTML="";
    var felulet = 0;
    for (i = 0; i < db; i++) {
        panelek.innerHTML += "<img src='napelem_ikon.png'>"; 
        felulet += 3.5;
    }
    panelek.innerHTML += "<br>"+"("+db+" db)";
    tetofelulet.value = felulet;
    document.getElementById('osszteljesitmeny').value = db * 275;
}