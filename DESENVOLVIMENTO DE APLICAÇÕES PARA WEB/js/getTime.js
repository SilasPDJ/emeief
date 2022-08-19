const GET_DATE = (texto = "Last Sync: ", sep = " ", option = 0) => {
    // default = todos
    // 1 = somente horas
    // 2 = somente dia
    let currentdate = new Date();
    let day, month, year;
    let hour, minutes, seconds;

    day = currentdate.getDate();
    month = currentdate.getMonth() + 1;
    year = currentdate.getFullYear();

    hour = currentdate.getHours();
    minutes = currentdate.getMinutes();
    seconds = currentdate.getSeconds();

    let dia =
        day.toString().padStart(2, "0") +
        "/" +
        month.toString().padStart(2, "0") +
        "/" +
        year;
    let horario =
        hour.toString().padStart(2, "0") +
        ":" +
        minutes.toString().padStart(2, "0") +
        ":" +
        seconds.toString().padStart(2, "0");

    let tutti;
    if (option == 1) {
        tutti = texto + horario;
    } else if (option == 2) {
        tutti = texto + dia;
    } else {
        tutti = texto + dia + sep + horario;
    }
    // alert(tutti);
    return tutti;
};

setInterval(function () {
    // GET_DATE()
    let gd = GET_DATE("Horário de agora: ", " @ ", 1);
    document.querySelector(".horario").textContent = gd;
}, 1000);
