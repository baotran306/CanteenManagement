
let activeForm = (classClick,typeClick) => {
    let push = document.getElementsByClassName(classClick)
    for (let i=0;i<push.length;i++)
    {
        if (push[i].textContent === typeClick)
        push[i].onclick = () => {
            let c = document.getElementById("modal");
            c.style.display = "flex";
        }
    }
}

let closeForm = (classClick,typeClick) => {
    let push = document.getElementsByClassName(classClick)
    for (let i=0;i<push.length;i++)
    {
        if (push[i].textContent === typeClick)
        push[i].onclick = () => {
            let c = document.getElementById("modal");
            c.style.display = "none";
        }
    }
}