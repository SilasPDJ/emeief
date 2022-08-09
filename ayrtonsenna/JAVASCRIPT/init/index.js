const prefix = "/produtos/";
let link_prefix = [".html"][0];
let links = ["domestico", "moda", "eletronicos", "variados"];

links = links.map(function (val, e) {
    return val + link_prefix;
});
let compras = document.querySelector("#comprasSorted");
compras.setAttribute(
    "href",
    prefix + links[Math.floor(Math.random() * links.length)]
);
// Randomiza página de produtoss

const imgPro = document.getElementById("add-pro-imgUploaded");
const btPro = document.getElementById("add-pro-adicionarArquivo");

btPro.addEventListener("change", function (event) {
    imgPro.style = "max-width:100%; max-height:90%;";
    imgPro.src = URL.createObjectURL(this.files[0]); // set src to blob url
});
