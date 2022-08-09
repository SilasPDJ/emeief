let part1 = () => {
    document
        .querySelector(
            "#section-directions-trip-0 > div.MespJc > div:nth-child(3) > div:nth-child(4) > button"
        )
        .click();
};

let part2 = () => {
    document
        .querySelector(
            "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.O7gcad.Hk4XGb > div.MyVbZc.Hk4XGb > div:nth-child(3) > button"
        )
        .click();
};

let part3 = () => {
    document
        .querySelector(
            "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.O7gcad.Hk4XGb > div.MyVbZc.Hk4XGb > div:nth-child(3) > div > div > button:nth-child(2)"
        )
        .click();
};

//let part4 = () => {document.querySelector("#tabelaDados > tbody > tr > td:nth-//child(7) > a > i").click();}

let part4 = () => {
    document
        .querySelector(
            "#print > div > div.l0m6zd > div.gYUjoc > div.O0cjFc.gMdnfc > button.L6gKoc.Ab1Xue.IdAxLe"
        )
        .click();
};

let part5 = () => {
    document
        .querySelector(
            "#print > div > div.l0m6zd > div.gYUjoc > div.O0cjFc.gMdnfc > button:nth-child(1)"
        )
        .click();
};

part1();
setTimeout(part2, 1000);
setTimeout(part3, 2000);
setTimeout(part4, 3000);
setTimeout(part5, 10000);

//  REPAT PROCESS
////////////////////////////////
/////////////////////////

function startAgain() {
    /*const ENDERECO = "R. Rio Pardo, 460 - Vila Helena, Santo André - SP, 09175-460"; 
    document.querySelector("#sb_ifc50 > input").value = ENDERECO;*/
    window.history.back();
}
setTimeout(startAgain, 20000);
setTimeout(startAgain, 22000);

setTimeout(function () {
    document
        .querySelector(
            "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.szK3Wb.Hk4XGb > button"
        )
        .click();
}, 4000);
