function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
function getElementsByText(str, tag = "button") {
    return Array.prototype.slice
        .call(document.getElementsByTagName(tag))
        .filter((el) => el.textContent.trim() === str.trim());
}

let script = document.createElement("script");
script.setAttribute(
    "src",
    "https://cdn.jsdelivr.net/npm/html2canvas@1.0.0-rc.5/dist/html2canvas.min.js"
);
document.head.appendChild(script);
// listar matrícula por turma, escola....
let toclicks = document.querySelectorAll(".icone-tabela-visualizar");
for (i = 1; i < toclicks.length; i++) {
    toclicks[i].click();
    await sleep(5000);
    document.querySelector("#aba5 > a").click();
    await sleep(6000);
    input = document.querySelectorAll("#tabelaDados_filter > label > input")[1];
    input.value = 202;
    dispatchEvent2Element(input);
    await sleep(8000);

    //
    const CONTENT = document.querySelectorAll(".decor-body")[0];
    const CONTENT_GAMBIARRA =
        document.querySelectorAll(".decor-body")[0].innerHTML;
    CONTENT.innerHTML = "";

    takescreenshot();
    await sleep(10000);
    CONTENT.innerHTML = CONTENT_GAMBIARRA;
    // break;
}

function dispatchEvent2Element(element) {
    var ev = document.createEvent("Event");
    ev.initEvent("keyup");
    // TODO: Descobrir como remover o depreciador...
    ev.which = ev.keyCode = 13;
    element.dispatchEvent(ev);
}

// gets the script...

// taking screenshots
function takescreenshot() {
    const screenshotTarget = document.querySelectorAll(".modal-content")[0];
    text = document.querySelector(".modal-title").textContent;
    // TODO: o numero acima fica incrementando toda hora, preciso selecionar dinamicamente
    text = text.slice(16).split(" -")[0];

    // gets the script...

    html2canvas(screenshotTarget).then((canvas) => {
        let a = document.createElement("a");
        a.download = text + ".png";
        a.href = canvas.toDataURL("image/png");
        a.click();
    });
    getElementsByText("Voltar")[0].click();
}
