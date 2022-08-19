let canvas = document.querySelector("#canvas");
let ctx = canvas.getContext("2d");

const INPUTS_SIZE_ID = ["a-side", "b-side", "c-side"];
const drawTriangle = () => {
    // Get user inputs
    let [AB, BC, AC] = INPUTS_SIZE_ID.map((id) =>
        parseFloat(document.querySelector(`#${id}`).value)
    );

    // Stop if user input is no good
    if (!AB || !BC || !AC) return;

    // Stop if sum of small sides is exceeded by large side
    let [max, min1, min2] = [AB, BC, AC].sort((a, b) => b - a);
    if (max > min1 + min2) return;

    // We define `A` as being at (0, 0), `B` as being a distance `AB`
    // to the east of `A`, and `C` as the point which is a distance
    // `AC` from `A` and `BC` from `B` (and north of both `A` and `B`)
    // Note we do not require a rotate transformation!! We simply
    // define our initial points differently to allow `AB` to be the
    // bottom of the triangle, and parallel to the x-axis.

    // Solve for C:
    let Cx = (AB * AB + AC * AC - BC * BC) / (2 * AB);
    let Cy = -Math.sqrt(AC * AC - Cx * Cx);

    // Now define our points:
    let [A, B, C] = [
        [0, 0],
        [AB, 0],
        [Cx, Cy],
    ];

    // Get width+height of canvas. Really we could hardcode these values
    // based on our CSS, but using `getBoundingClientRect` makes this code
    // more maintainable.
    let { width: canvasWidth, height: canvasHeight } =
        canvas.getBoundingClientRect();
    let canvasMid = [canvasWidth / 2, canvasHeight / 2];

    // Get center of mass of triangle (average x coord, average y coord)
    let mid = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];

    // We'll translate all points. The following can be simplified;
    // I've done things in two steps to make the logic more apparent:
    [A, B, C] = [A, B, C].map(([x, y]) => {
        // First shift backwards by the triangle's midpoint.
        // This centers the triangle at the origin (top-left corner)
        [x, y] = [x - mid[0], y - mid[1]];

        // Now shift forwards by half the canvas' size.
        // This centers the triangle at the center of the canvas!
        return [x + canvasMid[0], y + canvasMid[1]];
    });

    ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    ctx.beginPath();
    // ctx.fillStyle = "#000";
    ctx.moveTo(A[0], A[1]);
    ctx.lineTo(B[0], B[1]);
    ctx.lineTo(C[0], C[1]);
    ctx.fill();
};

// ---------------- ARROW FUNCTION vs ANONYMOUS

// Changing the inputs redraws the triangle

for (let id of INPUTS_SIZE_ID) {
    document.querySelector(`#${id}`).addEventListener("input", drawTriangle);
}
drawTriangle();

const INPUTS_SIZE_ID_GOTTEN = INPUTS_SIZE_ID.map((id) => {
    return document.getElementById(id);
});
//TODO: relembrar map vs reduce vs filter

// keys for shortcuts

window.addEventListener("keyup", keyup);
function keyup(evt) {
    // alert(evt.key);
    if (evt.altKey) {
        if (evt.key == "a" || evt.key == "1") {
            INPUTS_SIZE_ID_GOTTEN[0].focus();
            INPUTS_SIZE_ID_GOTTEN[0].value = "";
        } else if (evt.key == "b" || evt.key == "2") {
            INPUTS_SIZE_ID_GOTTEN[1].focus();
            INPUTS_SIZE_ID_GOTTEN[1].value = "";
        } else if (evt.key == "c" || evt.key == "3") {
            INPUTS_SIZE_ID_GOTTEN[2].focus();
            INPUTS_SIZE_ID_GOTTEN[2].value = "";
        }
    }
}
//
let buttons = [
    ...document.querySelectorAll(
        "#interactive-actions > .canvas-actions.column-item > div > button"
    ),
]; // spread operator

// 3 para 1

buttons.map((el) => {
    el.addEventListener("click", function () {
        alert("sasasa");
    });
});

// KeyPress is now deprecated.
