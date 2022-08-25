function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
let toclicks = document.querySelectorAll(".icone-tabela-visualizar");
for (i = 1; i < toclicks.length; i++) {
    toclicks[i].click();
    await sleep(i * 5000);
    document.querySelector("#aba5 > a").click();
    await sleep(i * 6000);
    input = document.querySelectorAll("#tabelaDados_filter > label > input")[1];
    input.value = 2023;
    dispatchEvent2Element(input);
    await sleep(i * 7000);
    takescreenshot();
    break;
}

function dispatchEvent2Element(element) {
    var ev = document.createEvent("Event");
    ev.initEvent("keyup");
    // TODO: Descobrir como remover o depreciador...
    ev.which = ev.keyCode = 13;
    element.dispatchEvent(ev);
}

// taking screenshots
function takescreenshot() {
    const screenshotTarget = document.getElementById("frmFicha");
    text = document.querySelector("#sedUiModalWrapper_11title").textContent;
    text = text.slice(16).split(" -")[0];

    // gets the script...
    let script = document.createElement("script");
    script.setAttribute(
        "src",
        "https://cdn.jsdelivr.net/npm/html2canvas@1.0.0-rc.5/dist/html2canvas.min.js"
    );
    document.head.appendChild(script);
    // gets the script...

    html2canvas(screenshotTarget).then((canvas) => {
        let a = document.createElement("a");
        a.download = text + ".png";
        a.href = canvas.toDataURL("image/png");
        a.click();
    });
}
